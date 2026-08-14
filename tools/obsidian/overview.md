---
type: Software
title: Obsidian — Overview
description: Local-first Markdown knowledge-base / PKM app using plain-text .md files in a vault, with bidirectional links and a graph view.
resource: https://obsidian.md/
tags: [obsidian, pkm, notes, markdown, vault, knowledge-base, local-first]
timestamp: 2026-07-09T04:05:00Z
---

# What Obsidian is

Obsidian is a **local-first knowledge-base** app for personal notes, built on **plain-text Markdown** files in a *vault* (a folder). Notes link to each other with `[[wikilinks]]`, forming a network you can visualize in a **graph view**. The app itself is closed-source, but your data stays as portable `.md` files you own.

# Why it matters

* **Local-first** — files live on disk; no vendor lock-in of your data.
* **Bidirectional links** — `[[note]]` connects ideas; backlinks show what references a note.
* **Graph view** — see the structure of your knowledge (driven by `graph.json` in `.obsidian/`).
* **Extensible** — core + community plugins (dataview, templates, canvas, etc.).
* **Markdown-native** — readable in any editor (VSCode, etc.).

# How it fits your stack

| Layer | Tool |
|-------|------|
| Notes / PKM | **Obsidian** (vault at `~/Desktop/vault`) |
| Agent that reads notes | Hermes (`~/.hermes/`) |
| Knowledge graph from notes | Graphify (ingest vault → graph) |
| Editors | VSCode, OpenCode, Windsurf, Cursor |

Your vault is the second-brain source; Hermes can read it, and Graphify can turn it into a queryable graph.

# Notes

* `programs/Obsidian.desktop` launches it via `setsid obsidian`.
* The app stores view/layout state in `vault/.obsidian/` (git-ignorable config).

# Citations

[1] [Obsidian](https://obsidian.md/)
[2] [Help — What is Obsidian](https://help.obsidian.md/)
[3] [Local launcher](/../../programs/Obsidian.desktop)
