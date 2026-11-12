#!/usr/bin/env python3
"""Vault checker: links, frontmatter, and privacy hygiene.

Run from the repo root:  python3 scripts/check_vault.py
Exit code 1 if any ERROR is found; WARNINGs never fail the run.

Checks
  * every relative .md link resolves to a file in the vault (resolved from the linking file's folder)
  * no absolute-path or bare cross-folder link forms
  * required OKF frontmatter fields are present; source ids are unique per doc
  * no machine-specific content (home paths, private IPs, local checkout paths)
  * warnings: docs past stale_after, docs with no inbound links, docs with no outbound links
"""
from __future__ import annotations

import datetime as dt
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".obsidian", ".github", "scripts", "node_modules"}
NOT_FRONTMATTER = {"README.md", "AGENTS.md", "CONTRIBUTING.md", "LICENSE.md"}
REQUIRED = ["type", "title", "description", "resource", "tags", "generated",
            "verified", "status", "stale_after", "sources"]

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CODE_RE = re.compile(r"```.*?```|`[^`\n]*`", re.S)
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
PRIVATE = [
    (re.compile(r"(?<![:\w])/home/[a-z][a-z0-9_-]*/"), "home-directory path"),  # skips container mounts like :/home/node/
    (re.compile(r"/Users/[A-Za-z][A-Za-z0-9_-]*/"), "home-directory path"),
    (re.compile(r"\b192\.168\.\d{1,3}\.\d{1,3}\b"), "private IP address"),
    (re.compile(r"\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"), "private IP address"),
    (re.compile(r"\b100\.(6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.\d{1,3}\.\d{1,3}\b"), "Tailscale CGNAT IP"),
    (re.compile(r"\b[a-z0-9-]+\.[a-z0-9-]+\.ts\.net\b"), "tailnet hostname"),
    (re.compile(r"(?<![\w.-])programs/[a-z]"), "local checkout path"),
]


def md_files() -> list[pathlib.Path]:
    out = []
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT)
        if any(part in SKIP_DIRS or part.startswith(".") for part in rel.parts[:-1]):
            continue
        if p.name in {"secrets.md", "README_TOCONTINUE.md"}:
            continue
        out.append(p)
    return sorted(out)


def main() -> int:
    files = md_files()
    known = {f.relative_to(ROOT).as_posix() for f in files}
    errors: list[str] = []
    warns: list[str] = []
    inbound: dict[str, set[str]] = {k: set() for k in known}
    outbound: dict[str, set[str]] = {k: set() for k in known}
    today = dt.date.today()

    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        text = f.read_text(encoding="utf-8")
        body = CODE_RE.sub("", text)

        # links
        for m in LINK_RE.finditer(body):
            url = m.group(1)
            if re.match(r"^(https?:|mailto:|#)", url):
                continue
            target = url.split("#", 1)[0]
            if not target:
                continue
            if target.startswith("/"):
                errors.append(f"{rel}: absolute link form '{url}'")
                continue
            resolved = (f.parent / target).resolve()
            try:
                tgt = resolved.relative_to(ROOT).as_posix()
            except ValueError:
                errors.append(f"{rel}: link escapes the vault '{url}'")
                continue
            if tgt.endswith(".md"):
                if tgt not in known:
                    errors.append(f"{rel}: broken link '{url}'")
                elif tgt != rel:
                    outbound[rel].add(tgt)
                    inbound[tgt].add(rel)
            elif not resolved.exists():
                errors.append(f"{rel}: missing file '{url}'")

        # privacy
        for rx, label in PRIVATE:
            for m in rx.finditer(text):
                errors.append(f"{rel}: {label} '{m.group(0)}'")

        # frontmatter
        if f.name in NOT_FRONTMATTER and f.parent == ROOT:
            continue
        fm = FM_RE.match(text)
        if not fm:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        block = fm.group(1)
        for key in REQUIRED:
            if not re.search(rf"^{key}\s*:", block, re.M):
                errors.append(f"{rel}: frontmatter missing '{key}'")
        ids = re.findall(r"^\s*-\s*id:\s*(\S+)", block, re.M)
        dupes = {i for i in ids if ids.count(i) > 1}
        if dupes:
            errors.append(f"{rel}: duplicate source ids {sorted(dupes)}")
        sa = re.search(r"^stale_after:\s*['\"]?(\d{4}-\d{2}-\d{2})", block, re.M)
        if sa and dt.date.fromisoformat(sa.group(1)) < today:
            warns.append(f"{rel}: past stale_after ({sa.group(1)}), re-verify")

    for rel in sorted(known):
        if rel in {"README.md", "AGENTS.md", "CONTRIBUTING.md"}:
            continue
        if not inbound[rel] and rel != "index.md":
            warns.append(f"{rel}: no inbound links (orphan node in the graph)")
        if not outbound[rel]:
            warns.append(f"{rel}: no outbound links (dead end in the graph)")

    edges = sum(len(v) for v in outbound.values())
    for w in warns:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(files)} docs, {edges} internal links, {len(errors)} errors, {len(warns)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
