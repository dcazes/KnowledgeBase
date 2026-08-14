---
type: Reference
title: Obsidian — Vault Structure
description: The ~/Desktop/vault layout and the .obsidian/ config directory (graph.json, workspace.json, core-plugins.json) on this machine.
resource: https://help.obsidian.md/
tags: [obsidian, vault, structure, obsidian-config, graph-json, workspace-json]
generated: { by: "human:daniel", at: "2026-07-09T04:07:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:07:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: help-vault
    resource: "https://help.obsidian.md/"
    title: "Help — Vault"
    author: "site:help.obsidian.md"
  - id: local-launcher
    resource: "/../../programs/Obsidian.desktop"
    title: "Local launcher"
---

# Obsidian — Vault location

Your vault root is **`~/Desktop/vault/`**. Everything inside is a normal file/folder — portable and git-friendly.

# Obsidian config — `.obsidian/`

Obsidian keeps its settings in `vault/.obsidian/`:

| File | Purpose |
|------|---------|
| `graph.json` | Graph view settings (filters, groups, display) |
| `workspace.json` | Workspace/layout state (panes, split, open files) — ~6KB here |
| `core-plugins.json` | Which built-in plugins are enabled/disabled |
| `appearance.json` | Theme + CSS snippet settings |
| `app.json` | Misc app settings |

These are machine/UI state — generally safe to git-ignore but useful to back up.

# Typical layout (this vault)

```
vault/
├── .obsidian/            # config (graph.json, workspace.json, core-plugins.json, ...)
├── 03 - Reference/       # e.g. "Hermes Setup.md"
├── (other topic folders) # notes organized by area
└── ...
```

# Tips

* Organize by topic folders; use `[[wikilinks]]` to connect notes.
* `core-plugins.json` tells you which built-ins are on (backlinks, graph, tags, etc.).
* The vault is plain Markdown → Graphify can ingest it (see [AI Integration](ai-integration.md)).
