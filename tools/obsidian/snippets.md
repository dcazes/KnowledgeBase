---
type: Playbook
title: Obsidian — Snippets & Cheat Sheet
description: Launch, vault location, link/graph syntax, and Graphify ingest for Obsidian.
resource: https://help.obsidian.md/
tags: [obsidian, snippets, cheat-sheet, wikilinks, graph, graphify]
timestamp: 2026-07-09T04:11:00Z
---

# Launch

```bash
setsid obsidian          # via programs/Obsidian.desktop
# or just: obsidian
```

# Vault

Root: `~/Desktop/vault/` (config in `vault/.obsidian/`).

# Markdown syntax

```md
[[Note]]            # wikilink (creates backlink)
#tag                # tag
![[Embedded Note]]  # embed
```

# Graph view

Open via the Graph core plugin; settings in `vault/.obsidian/graph.json`.

# Ingest into Graphify

```bash
graphify add ~/Desktop/vault
python -m graphify.serve
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Launcher dead | binary missing | install obsidian; run `obsidian` |
| Wrong vault | folder not opened | Open Folder as Vault → `~/Desktop/vault` |

# Citations

[1] [Installation](installation.md)
[2] [Vault Structure](vault-structure.md)
[3] [AI Integration](ai-integration.md)
