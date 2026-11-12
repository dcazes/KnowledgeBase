# AGENTS.md

Guidance for humans and AI agents editing this repository.

## What this repo is

A **Markdown knowledge base** (not a software project) on the self-hostable AI stack, organised as an Obsidian vault. It is general knowledge: it documents what tools are and how to use them, not any particular machine or deployment. There is no build system; work here is editing Markdown.

## Layout

```
index.md                      root hub (categories, tools, concepts)
landscape.md                  dated overview of the AI landscape
concepts/                     cross-cutting concept hubs + concepts/index.md
<category>/alternatives.md    comparison and decision guide per category
<category>/<tool>/            one folder per tool
    index.md                  tool hub: summary, facts table, contents, related links
    overview.md               how it works
    installation.md           install / deploy
    configuration.md          (optional) settings
    snippets.md               copy-paste examples
    ai-integration.md         how it connects to the rest of the stack
    <topic>.md                (optional) deeper topics
scripts/check_vault.py        link / frontmatter / privacy checker (CI)
```

Categories: `runtime`, `memory`, `databases`, `agents`, `browsers`, `ingestion`, `apps`, `editors`, `observability`, `tools`.

## Doc conventions (Open Knowledge Format, trust-signals subset)

Every note except `README.md` and `AGENTS.md` starts with YAML frontmatter:

```yaml
---
type: Software | Concept | Playbook | Reference | Comparison | Hub
title: ...
description: one or two sentences
resource: official URL
tags: [lowercase, hyphenated]
generated: { by: "agent:<tool>" | "human:<name>", at: "YYYY-MM-DDT00:00:00Z" }
verified: [ { by: ..., at: ... } ]
status: stable | draft
stale_after: YYYY-MM-DD          # 180 days after verification
sources:
  - id: unique-kebab-id
    resource: "https://..."
    title: "..."
    author: "site:example.com" | "Author et al., arXiv XXXX.XXXXX"
---
```

* **Verify, don't assume.** Check versions, commands and claims against the upstream repo, release notes, package registry or paper, and cite them in `sources:`. Mark vendor-reported benchmark numbers as such.
* **General, not personal.** No home-directory paths, private IPs, hostnames, credentials, or "on this machine" statements. Use placeholders like `change-me` and `localhost`.
* **Responsible framing** for dual-use tools (anti-detection browsers, scrapers): state permitted-use expectations.

## Links

* Use **relative Markdown links** resolved from the linking file's directory (e.g. `../../concepts/rag.md`). No wikilinks, no absolute or bare cross-folder paths.
* Each tool `index.md` should link to relevant concept hubs and peer tools; each concept hub should link to the tools that implement it. Every note should have at least one inbound and one outbound link.

## Checks

```bash
python3 scripts/check_vault.py     # must report 0 errors
```

## Do not touch

* `*/secrets.md` and `*/README_TOCONTINUE.md` — local, gitignored files. Never read or commit them.
