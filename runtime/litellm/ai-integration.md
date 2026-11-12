---
type: Playbook
title: LiteLLM AI Integration
description: Patterns for putting LiteLLM at the centre of an AI stack — one endpoint for chat UIs, coding agents, RAG and memory tools; local-first with cloud fallback; per-app keys and budgets; tracing to Langfuse.
resource: https://docs.litellm.ai
tags: [litellm, integration, gateway, coding-agents, open-webui]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: litellm-docs
    resource: "https://docs.litellm.ai"
    title: "LiteLLM documentation"
    author: "site:docs.litellm.ai"
---

# LiteLLM — AI Integration

## The hub pattern

```
Open WebUI ─┐
Dify, n8n  ─┤
Claude Code ┼──▶ LiteLLM :4000 ──▶ Ollama / vLLM (local)
Mem0, Graphiti ┤                 └─▶ Anthropic / OpenAI / Gemini (hosted)
LangGraph app ─┘          └─ logs ─▶ Langfuse
```

Every tool that speaks the [OpenAI API](../../concepts/openai-compatible-api.md) points at LiteLLM instead of a provider. Swapping models, adding fallbacks or cutting costs then happens in one `config.yaml`.

## Examples

* **Chat UIs:** add LiteLLM as an OpenAI connection in [Open WebUI](../../apps/openwebui/index.md) or a custom provider in [AnythingLLM](../../apps/anythingllm/index.md).
* **Coding agents:** [Claude Code](../../agents/claude-code/index.md) can use the Anthropic-format `/messages` endpoint via `ANTHROPIC_BASE_URL`; [OpenCode](../../agents/opencode/index.md), [Aider](../../agents/aider/index.md), [Codex](../../agents/codex/index.md) and [Continue](../../editors/continue/index.md) accept custom OpenAI-compatible base URLs.
* **Memory and RAG:** [Mem0](../../memory/mem0/configuration.md), [Graphiti](../../memory/graphiti/index.md), [LightRAG](../../memory/lightrag/configuration.md) and [Microsoft GraphRAG](../../memory/graphrag/snippets.md) work through a LiteLLM base URL; [Hindsight](../../memory/hindsight/snippets.md)'s LLM wrapper is built on LiteLLM.
* **Frameworks:** [LangGraph](../../agents/langgraph/index.md), [CrewAI](../../agents/crewai/index.md) (which uses LiteLLM internally) and [PydanticAI](../../agents/pydanticAI/index.md).

## Good practice

* One virtual key per application, with a budget — you see exactly which tool spends what.
* Local model first, hosted fallback for overflow and long contexts.
* Send traces to [Langfuse](../../observability/langfuse/index.md) for debugging and [evals](../../concepts/evals.md).
* Keep the proxy off the public internet or behind auth; the master key controls everything.

## Related

[LiteLLM index](index.md) · [LLM observability](../../concepts/llm-observability.md) · [Self-hosting](../../concepts/self-hosting.md)
