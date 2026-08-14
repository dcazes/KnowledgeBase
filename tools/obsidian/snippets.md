---
type: Playbook
title: Obsidian — Snippets & Cheat Sheet
description: Launch, vault location, link/graph syntax, and Graphify ingest for Obsidian.
resource: https://help.obsidian.md/
tags: [obsidian, snippets, cheat-sheet, wikilinks, graph, graphify]
generated: { by: "human:daniel", at: "2026-07-09T04:11:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:11:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: installation
    resource: "installation.md"
    title: "Installation"
  - id: vault-structure
    resource: "vault-structure.md"
    title: "Vault Structure"
  - id: ai-integration
    resource: "ai-integration.md"
    title: "AI Integration"
---

# Obsidian — Launch

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
