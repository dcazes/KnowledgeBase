---
type: Playbook
title: LangGraph AI Integration
description: LangGraph with the rest of the stack — memory services as nodes or stores, MCP tool adapters, LangSmith or Langfuse tracing, local models via Ollama or vLLM, and serving graphs as APIs.
resource: https://docs.langchain.com/oss/python/langgraph/overview
tags: [langgraph, integration, memory, mcp, observability]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: langgraph-docs
    resource: "https://docs.langchain.com/oss/python/langgraph/overview"
    title: "LangGraph documentation"
    author: "site:docs.langchain.com"
---

# LangGraph — AI Integration

| Need | How |
|---|---|
| Long-term memory | Built-in store, or [Mem0](../../memory/mem0/ai-integration.md), [Zep](../../memory/zep/ai-integration.md), [Graphiti](../../memory/graphiti/ai-integration.md), [Hindsight](../../memory/hindsight/ai-integration.md) in retrieve/ingest nodes |
| Tools from MCP | `langchain-mcp-adapters` turns [MCP](../../concepts/mcp.md) servers into tools |
| RAG | Retriever nodes over [Qdrant](../../databases/qdrant/index.md), [pgvector](../../databases/pgvector/index.md), [LightRAG](../../memory/lightrag/index.md) |
| Observability | LangSmith, or [Langfuse](../../observability/langfuse/index.md) callback handler |
| Evals | LangSmith datasets, [Ragas](../../observability/ragas/index.md), [promptfoo](../../observability/promptfoo/index.md) |
| Local models | `langchain-ollama`, OpenAI-compatible [vLLM](../../runtime/vllm/index.md), [LiteLLM](../../runtime/litellm/index.md) |

Graphs can be served as APIs with the LangGraph server (self-hosted or LangSmith Deployment) and called from [n8n](../../apps/n8n/index.md) or front ends.

## Related

[LangGraph index](index.md) · [Agent frameworks](../../concepts/agent-frameworks.md)
