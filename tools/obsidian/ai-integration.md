---
type: Reference
title: Obsidian — AI Integration
description: How Obsidian's vault connects to the stack — Hermes reads notes, Graphify ingests the vault into a graph, and how it compares to code editors.
resource: https://help.obsidian.md/
tags: [obsidian, integration, hermes, graphify, vault, knowledge-graph]
generated: { by: "human:daniel", at: "2026-07-09T04:09:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:09:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: vault-structure
    resource: "vault-structure.md"
    title: "Vault structure"
  - id: graphify
    resource: "/../../graphify/index.md"
    title: "Graphify"
  - id: hermes
    resource: "/../../hermes/index.md"
    title: "Hermes"
---

# Hermes reads the vault

Hermes (`~/.hermes/`) can read files in `~/Desktop/vault/` to ground answers in your notes (e.g. *Hermes Setup.md* informs this very KB). Treat the vault as a readable knowledge source for agents.

# Graphify ingests the vault

Graphify can turn the vault into a **queryable knowledge graph**:
```bash
graphify add ~/Desktop/vault
# then serve: python -m graphify.serve
```
Notes + their `[[links]]` become graph nodes/edges — a structured layer over plain Markdown.

# Copilot / AI plugins (optional)

Community AI plugins can chat over your vault. Alternatively, copy vault context into OpenWebUI / AnythingLLM workspaces for RAG.

# Obsidian vs code editors

| Tool | Primary use |
|------|-------------|
| **Obsidian** | Notes / PKM (Markdown vault) |
| VSCode / OpenCode / Windsurf / Cursor | Code editing |

Obsidian is for *knowledge*, the editors are for *code* — though all read `.md`.
