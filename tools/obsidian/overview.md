---
type: Concept
title: Obsidian Overview
description: Obsidian's core ideas — vaults of Markdown files, internal links and backlinks, YAML properties, graph and local graph views, Bases for filtered table and card views, Canvas, and Mermaid diagrams.
resource: https://help.obsidian.md
tags: [obsidian, overview, graph-view, bases]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: obsidian-help
    resource: "https://help.obsidian.md"
    title: "Obsidian Help"
    author: "site:help.obsidian.md"
  - id: obsidian-changelog
    resource: "https://obsidian.md/changelog/"
    title: "Obsidian changelog"
    author: "site:obsidian.md"
---

# Obsidian — Overview

* **Vault:** any folder of Markdown files; Obsidian keeps its settings in `.obsidian/`.
* **Links:** `[[wikilinks]]` or standard `[text](relative/path.md)` Markdown links; Obsidian tracks backlinks and updates links when files move.
* **Properties:** YAML frontmatter (like this vault's OKF fields) shown as typed properties, searchable and usable in Bases.
* **Graph view:** every note is a node, every link an edge. Filters, groups (coloured by path or tag), and the *local graph* around one note make structure visible — a hand-built [knowledge graph](../../concepts/knowledge-graphs.md).
* **Bases:** database-like table and card views over notes filtered by properties (reorderable filters in 1.15).
* **Canvas:** infinite whiteboard of notes, media and links.
* **Diagrams:** Mermaid rendered by Obsidian's own library since 1.15, themed and zoomable.

## Related

[Obsidian index](index.md) · [Plugins & features](plugins-features.md) · [Vault structure](vault-structure.md)
