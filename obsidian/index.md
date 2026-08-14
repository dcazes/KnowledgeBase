---
type: Reference
title: Obsidian
description: Local-first Markdown knowledge-base / PKM app (v1.13.7, closed-source) using plain-text .md files in a vault with bidirectional links and graph view.
resource: https://obsidian.md/
tags: [obsidian, pkm, notes, markdown, vault, knowledge-base, local-first]
timestamp: 2026-08-12T00:00:00Z
---

# Obsidian

A **local-first Markdown knowledge-base / PKM app** (closed-source app, open `.md` format; v1.13.7 as of 2026-08-12). On this machine it's your **second-brain note vault** — launched via `setsid obsidian`, with the vault at `~/Desktop/vault/` (config in `vault/.obsidian/`). It's where notes like *Hermes Setup* live, and it's a natural source for Graphify to ingest.

## Contents

* [Overview](overview.md) - what Obsidian is, local-first model
* [Installation](installation.md) - `setsid obsidian`, vault location
* [Vault Structure](vault-structure.md) - `vault/` layout + `.obsidian/` config
* [Plugins & Features](plugins-features.md) - core plugins, graph view, links, dataview
* [AI Integration](ai-integration.md) - Hermes reads vault, Graphify ingest, vs editors
* [Alternatives](alternatives.md) - Logseq, Joplin, VSCode, Notion
* [Snippets](snippets.md) - cheat sheet

## Instance facts (this machine)

* **Launcher:** `programs/Obsidian.desktop` → `Exec=setsid obsidian` (Terminal=true)
* **Vault:** `~/Desktop/vault/` (contains `03 - Reference/Hermes Setup.md`, etc.)
* **Config:** `vault/.obsidian/` — `graph.json`, `workspace.json`, `core-plugins.json`, `appearance.json`, `app.json`
* **Role:** personal knowledge base / second brain

## Cross-references

* **Hermes** reads the vault for grounding — see [Hermes AI Integration](../hermes/ai-integration.md)
* **Graphify** can ingest the vault into a queryable graph — see [Graphify AI Integration](../graphify/ai-integration.md) & [Obsidian AI Integration](ai-integration.md)
* **VSCode / OpenCode / Windsurf / Cursor** can edit vault `.md` files — see respective AI Integration docs

## Last verified

**2026-08-12** — Launcher, vault path, `.obsidian/` config files, and integration docs verified. Obsidian v1.13.7 (2026-08-12); closed-source (free personal, paid Sync/Publish).

# Citations

[1] [Obsidian](https://obsidian.md/)
[2] [Help/docs](https://help.obsidian.md/)
[3] [Local launcher - programs/Obsidian.desktop](/../../programs/Obsidian.desktop)