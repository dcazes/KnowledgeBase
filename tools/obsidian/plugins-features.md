---
type: Reference
title: Obsidian — Plugins & Features
description: Obsidian's core features — bidirectional links, backlinks, graph view, core plugins, and community extensions (Dataview, Templates, Canvas).
resource: https://help.obsidian.md/
tags: [obsidian, plugins, features, graph-view, backlinks, dataview, canvas]
generated: { by: "human:daniel", at: "2026-07-09T04:08:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:08:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: help-core-plugins
    resource: "https://help.obsidian.md/"
    title: "Help — Core plugins"
    author: "site:help.obsidian.md"
  - id: graph-view
    resource: "https://help.obsidian.md/Plugins/Graph+view"
    title: "Graph view"
    author: "site:help.obsidian.md"
---

# Obsidian — Core features

* **Bidirectional links** — `[[Note]]` creates a link; the target shows **backlinks** automatically.
* **Tags** — `#tag` for lightweight categorization (drives search/filters).
* **Graph view** — visual network of notes (config in `.obsidian/graph.json`).
* **Search** — full-text across the vault.
* **Canvas** — free-form boards to map ideas.
* **Daily notes / Templates** — quick capture.

# Core plugins

Enabled via `.obsidian/core-plugins.json`. Common built-ins: Backlinks, Outline, Tag pane, Graph, Canvas, Templates, Daily notes, Note composer, Workspaces.

# Community plugins

Installed separately (bridge, dataview, etc.). Notable:
* **Dataview** — query notes as a database (YAML frontmatter → tables).
* **Templates** — insert reusable snippets.
* **Obsidian Git** — version-control the vault.

# Why it helps the stack

* Structured, linkable notes = a great knowledge source for **Graphify** (ingest → graph) and for **Hermes** to read.
* Frontmatter (like OKF `type:`) makes notes queryable via Dataview.
