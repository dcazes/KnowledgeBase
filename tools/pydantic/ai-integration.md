---
type: Playbook
title: Pydantic AI Integration
description: Where Pydantic shows up in AI engineering — structured outputs from OpenAI, Anthropic, Ollama and vLLM, tool schemas, Pydantic AI agents, ontologies in Graphiti and Zep, typed results in browser-use and CrewAI, and Logfire observability.
resource: https://docs.pydantic.dev
tags: [pydantic, integration, structured-output, tool-calling]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pydantic-docs
    resource: "https://docs.pydantic.dev"
    title: "Pydantic documentation"
    author: "site:docs.pydantic.dev"
---

# Pydantic — AI Integration

| Use | Example |
|---|---|
| Structured outputs | OpenAI/Anthropic SDK helpers, [Ollama](../../runtime/ollama/snippets.md) `format`, [vLLM](../../runtime/vllm/snippets.md) `json_schema` — pass `Model.model_json_schema()` |
| Tool schemas | Function parameters → JSON Schema in [Pydantic AI](../../agents/pydanticAI/index.md), LangChain/[LangGraph](../../agents/langgraph/index.md), MCP SDKs |
| Agent outputs | `output_type` in Pydantic AI, `output_model_schema` in [browser-use](../../browsers/browser-use/snippets.md), task outputs in [CrewAI](../../agents/crewai/index.md) |
| Knowledge ontologies | Custom entity and edge types in [Graphiti](../../memory/graphiti/concepts.md) and [Zep](../../memory/zep/snippets.md) |
| Extraction | Schemas for [Crawl4AI](../../browsers/crawl4ai/snippets.md) and [Firecrawl](../../browsers/firecrawl/snippets.md) JSON extraction |
| Config | `pydantic-settings` for API keys and endpoints |

See [Structured output](../../concepts/structured-output.md) and [Tool calling](../../concepts/tool-calling.md).

## Related

[Pydantic index](index.md) · [Pydantic AI](../../agents/pydanticAI/index.md)
