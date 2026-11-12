---
type: Playbook
title: Docling AI Integration
description: Docling in AI pipelines — LangChain, LlamaIndex, CrewAI and Haystack loaders, the Docling MCP server for agents, parser for LightRAG, Open WebUI and Dify, and feeding vector or graph stores.
resource: https://docling-project.github.io/docling/integrations/
tags: [docling, integration, mcp, rag, lightrag]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: docling-docs
    resource: "https://docling-project.github.io/docling/"
    title: "Docling documentation"
    author: "site:docling-project.github.io"
---

# Docling — AI Integration

| Where | How |
|---|---|
| Frameworks | Loaders for LangChain/[LangGraph](../../agents/langgraph/index.md), LlamaIndex, [CrewAI](../../agents/crewai/ai-integration.md), Haystack |
| Agents | Docling [MCP](../../concepts/mcp.md) server — convert and query documents from [Claude Code](../../agents/claude-code/index.md) and others |
| Chat / RAG apps | Extraction engine in [Open WebUI](../../apps/openwebui/rag.md); parsing plugin in [Dify](../../agents/dify/rag-pipeline.md); multimodal parsing in [LightRAG](../../memory/lightrag/overview.md) |
| Storage | Chunks → [Qdrant](../../databases/qdrant/index.md) / [pgvector](../../databases/pgvector/index.md); structured output → [Cognee](../../memory/cognee/index.md) or [Neo4j](../../databases/neo4j/index.md) graphs |

Parsing quality often matters more than the embedding model for RAG accuracy on PDFs with tables.

## Related

[Docling index](index.md) · [Document parsing](../../concepts/document-parsing.md)
