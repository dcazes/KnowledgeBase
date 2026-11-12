---
type: Playbook
title: Obsidian AI Integration
description: Using AI with an Obsidian vault — AI plugins with local or hosted models, MCP servers that let coding agents read and write notes, indexing a vault with Graphify, Cognee or LightRAG, and keeping a human-curated graph alongside machine-built ones.
resource: https://obsidian.md
tags: [obsidian, integration, mcp, rag, graphrag]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: obsidian-site
    resource: "https://obsidian.md"
    title: "Obsidian"
    author: "site:obsidian.md"
---

# Obsidian — AI Integration

* **In-app AI:** community plugins provide chat and semantic search over notes using [Ollama](../../runtime/ollama/index.md) or hosted models — [RAG](../../concepts/rag.md) over your vault.
* **Agents in the vault:** an [MCP](../../concepts/mcp.md) server or the Local REST API plugin lets [Claude Code](../../agents/claude-code/index.md), [Hermes](../../agents/hermes/index.md) or [OpenCode](../../agents/opencode/index.md) search and edit notes. Coding agents can also edit Markdown files directly.
* **Machine-built graphs:** point [Graphify](../../memory/graphify/index.md), [Cognee](../../memory/cognee/index.md) or [LightRAG](../../memory/lightrag/index.md) at the vault to extract an entity graph; compare it with Obsidian's hand-made link graph — see [GraphRAG](../../concepts/graphrag.md).
* **Memory sync:** [Hindsight](../../memory/hindsight/ai-integration.md) and others offer Obsidian integrations.

Plain Markdown plus consistent frontmatter (like this vault's) is what makes a vault easy for both people and agents.

## Related

[Obsidian index](index.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md)
