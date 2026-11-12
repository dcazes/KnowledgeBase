---
type: Playbook
title: MarkItDown AI Integration
description: Using MarkItDown with agents and RAG — the markitdown-mcp server for Claude Desktop and coding agents, quick ingestion before chunking and embedding, and when to switch to Docling.
resource: https://github.com/microsoft/markitdown
tags: [markitdown, integration, mcp, rag]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: markitdown-github
    resource: "https://github.com/microsoft/markitdown"
    title: "microsoft/markitdown on GitHub"
    author: "site:github.com"
---

# MarkItDown — AI Integration

* **MCP:** `markitdown-mcp` exposes a `convert_to_markdown` tool to any [MCP](../../concepts/mcp.md) client, so an agent can read PDFs or Office files on demand.
* **Pipelines:** convert → chunk → embed into [Qdrant](../../databases/qdrant/index.md) or [pgvector](../../databases/pgvector/index.md), or hand Markdown to [LightRAG](../../memory/lightrag/index.md), [Cognee](../../memory/cognee/index.md) or [Mem0](../../memory/mem0/index.md).
* **Switch to [Docling](../docling/index.md)** when tables, reading order or scanned pages matter.

## Related

[MarkItDown index](index.md) · [Document parsing](../../concepts/document-parsing.md)
