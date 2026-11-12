---
type: Concept
title: Obsidian Vault Structure (this vault)
description: How this knowledge base is organised as an Obsidian vault — category folders, a standard doc set per tool, concept hubs, comparison docs, OKF frontmatter, relative Markdown links, graph colour groups, and the link checker.
resource: https://help.obsidian.md
tags: [obsidian, vault-structure, okf, knowledge-base]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: obsidian-help
    resource: "https://help.obsidian.md"
    title: "Obsidian Help"
    author: "site:help.obsidian.md"
---

# Obsidian — Vault Structure (this vault)

```
index.md, landscape.md            hubs at the root
concepts/                         cross-cutting concept hubs (RAG, MCP, agent memory, …)
runtime/ memory/ browsers/ agents/ apps/ editors/ tools/ databases/ observability/ ingestion/
  <category>/alternatives.md      comparison for the category
  <category>/<tool>/index.md      tool hub
                  overview.md, installation.md, configuration.md, snippets.md, ai-integration.md, topic docs
scripts/check_vault.py            link, frontmatter and privacy checker (runs in CI)
```

## Conventions

* **Relative Markdown links** (`../../concepts/rag.md`) so links work on GitHub and in Obsidian alike.
* **OKF frontmatter** on every doc: type, title, description, resource, tags, lifecycle dates and `sources:` with official references.
* **Three link layers** create the graph's shape: tool docs ↔ their tool index; tool index ↔ concept hubs and peers; concept hubs ↔ each other and the root index.
* **Graph colour groups** (committed in `.obsidian/graph.json`) colour nodes by category folder.

## Related

[Obsidian index](index.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md)
