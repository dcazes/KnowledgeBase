---
type: Playbook
title: Qdrant AI Integration
description: Qdrant in AI stacks — vector store for Mem0, MemOS, Open WebUI, AnythingLLM, Cognee, LightRAG, Dify and n8n; framework integrations; an MCP server for agent memory; and FastEmbed for local embeddings.
resource: https://qdrant.tech/documentation/
tags: [qdrant, integration, rag, mcp, memory]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: qdrant-docs
    resource: "https://qdrant.tech/documentation/"
    title: "Qdrant documentation"
    author: "site:qdrant.tech"
---

# Qdrant — AI Integration

* **Memory and RAG tools:** [Mem0](../../memory/mem0/configuration.md), [MemOS](../../memory/memos/configuration.md), [Cognee](../../memory/cognee/configuration.md), [LightRAG](../../memory/lightrag/configuration.md), [Open WebUI](../../apps/openwebui/configuration.md), [AnythingLLM](../../apps/anythingllm/rag-embeddings.md), [Dify](../../agents/dify/architecture.md), [n8n](../../apps/n8n/ai-integration.md).
* **Frameworks:** LangChain/[LangGraph](../../agents/langgraph/index.md), LlamaIndex, Haystack, [CrewAI](../../agents/crewai/index.md).
* **MCP:** the official Qdrant MCP server gives agents "store" and "find" tools — simple semantic [agent memory](../../concepts/agent-memory.md).
* **FastEmbed:** Qdrant's lightweight local embedding library (dense, sparse, late-interaction) avoids a separate embedding service.

## Related

[Qdrant index](index.md) · [RAG](../../concepts/rag.md)
