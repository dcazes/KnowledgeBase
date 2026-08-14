---
type: Playbook
title: AGENTS
description: Working conventions for the kbv2 markdown knowledge base — layout, OKF doc format, verification rules, link conventions, and what not to touch.
resource:
tags: [meta, kbv2, conventions, okf]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
---

# AGENTS.md

## What this repo is

`kbv2` is a **markdown knowledge base** (not a software project): it documents a self-hosted AI/agent software stack in plain `.md` files following "Open Knowledge Format v0.2 (trust-signals subset)". There is **no build system, package manifest, or test suite** — work here is editing/adding markdown. `IDEA.md` sets the goal: accurate, standards-adherent, research-backed docs.

## Layout

- **One top-level folder per program** (`runtime/docker/`, `browsers/firecrawl/`, `browsers/camofox/`, `memory/memos/`, ...). Each has a standard doc set: `index.md`, `overview.md`, `installation.md`/`configuration.md`, `snippets.md`, `ai-integration.md`, plus topic docs. Cross-program comparison lives in one category-level `alternatives.md` per category (e.g. `memory/alternatives.md`), consolidating the former per-program `alternatives.md`.
- **`index.md` at root** is the master index with a build-status table. Update it when adding a program or changing doc counts.
- **`meta/architecture/`** holds meta/comparison docs (search backends, memory, blueprint). It may still contain **stale program copies** (e.g. `meta/architecture/memos/`) left over from the 2026-07-16 flatten to top-level folders — **top-level folders are authoritative**.
- **`agents/agent-stack/` is a NOT-deployed compose prototype** (template with `CHANGE_ME`/placeholder secrets). Treat `docker-compose.yml` there as a design doc, not live config.

## Doc conventions (OKF v0.2, trust-signals subset)

- Every concept doc carries YAML frontmatter: `type` (Software | Playbook | Reference | ...), `title`, `description`, `resource` (official URL), `tags`, `generated`/`verified`/`status`/`stale_after` (OKF v0.2 lifecycle fields).
- Every doc lists official/trusted sources in a `sources:` frontmatter block (id, resource, title, author). Keep ids sequential and unique.
- Author identity uses `human:daniel` (or `agent:<tool>` for agent-generated docs); `stale_after` defaults to 180 days after `generated.at`.
- **Local source paths use `/../../programs/<name>/`** — these resolve to the actual checkouts at `/home/daniel/Desktop/programs/` (outside this repo). Read those checkouts to verify commands/versions before writing docs.
- Facts must be **verified, not assumed**: docs distinguish live state ("currently running") from config-derived notes ("from config, not live state"). Use a `## Last verified` dated line in `index.md`; update it and the root build table when you change a program's docs.

## Do not touch

- **`*/secrets.md`** — real credentials, gitignored. Never read or commit them.
- **`*/README_TOCONTINUE.md`** — tracker files, gitignored.

## Environment

- This is an Obsidian vault (`.obsidian/` present) — keep relative `foo.md` links valid; do not restructure folders casually.

## Link conventions (resolution semantics)

- **All internal links are relative `.md` links resolved from the linking file's directory.** A doc in `foo/` pointing at `bar/index.md` must use `../bar/index.md` (P3 standard, 2026-08-13).
- **Do not use bare cross-folder names** (`bar/index.md` from inside `foo/`) or absolute `/../../bar/index.md` forms — the former breaks, the latter only passes a lenient resolver. Adopt the `../`-relative form everywhere.
- **The audit script** (`/tmp/opencode/audit_kbv2.py`) resolves links relative to each file's dir; because it globs with Python `glob`, hidden directories (`.slim/`) are excluded from its total — `271` audited md = `272` find-total minus the `.slim/` tracker. Keep this in mind when reconciling counts.
- **Doc-count convention:** the root build table counts every md in a program folder **including `secrets.md`** (SearXNG 10, Firecrawl 16, Dify 12, Frigate 9 each include their `secrets.md`). The stated total "261 program docs" is the sum of table rows; the vault holds 272 md total (261 + 7 category-level `alternatives.md` + root `index.md`, `IDEA.md`, `AGENTS.md`, and the `.slim/` refresh tracker).
- The stack's real deployments/configs referenced in docs live in `programs/` on the same machine (`docker compose`, running services), not in this repo.
