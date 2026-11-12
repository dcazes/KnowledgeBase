---
type: Software
title: LiteLLM
description: Open-source AI gateway and Python SDK that calls 100+ LLM providers through one OpenAI-format API — virtual keys, budgets and spend tracking, load balancing and fallbacks, auto-routing, guardrails, an MCP gateway, and logging to observability tools.
resource: https://github.com/BerriAI/litellm
tags: [litellm, ai-gateway, proxy, openai-compatible, routing, python]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: litellm-github
    resource: "https://github.com/BerriAI/litellm"
    title: "BerriAI/litellm on GitHub"
    author: "site:github.com"
  - id: litellm-docs
    resource: "https://docs.litellm.ai"
    title: "LiteLLM documentation"
    author: "site:docs.litellm.ai"
---

# LiteLLM

**LiteLLM** puts every model — OpenAI, Anthropic, Gemini, Bedrock, Azure, local [Ollama](../ollama/index.md) or [vLLM](../vllm/index.md) — behind a single [OpenAI-compatible API](../../concepts/openai-compatible-api.md). Use it as a Python library inside an app, or deploy the **AI Gateway** (proxy server) so a whole team or homelab shares one endpoint with keys, budgets, fallbacks and logs.

| | |
|---|---|
| Category | AI gateway · [OpenAI-compatible API](../../concepts/openai-compatible-api.md) |
| License | MIT (core); `enterprise/` directory under a separate licence |
| Language | Python SDK, Rust core |
| Latest release | v1.109.1 (2026-11-12) |
| Endpoints | `/chat/completions`, `/responses`, `/messages` (Anthropic), `/embeddings`, `/images`, `/audio`, `/batches`, `/rerank`, `/a2a`, MCP |

## Contents

* [Overview](overview.md) — SDK vs gateway, routing, keys and budgets, MCP and A2A
* [Installation](installation.md) — pip/uv, Docker, Postgres for the admin UI
* [Configuration](configuration.md) — `config.yaml` model list, fallbacks, callbacks
* [Snippets](snippets.md) — SDK calls, proxy requests, virtual keys
* [AI Integration](ai-integration.md) — putting coding agents, chat UIs and frameworks behind LiteLLM

## Related

* Concepts: [OpenAI-compatible API](../../concepts/openai-compatible-api.md) · [LLM observability](../../concepts/llm-observability.md) · [MCP](../../concepts/mcp.md) · [A2A](../../concepts/a2a.md)
* Backends: [Ollama](../ollama/index.md), [vLLM](../vllm/index.md), [llama.cpp](../llamacpp/index.md), [LM Studio](../lmstudio/index.md)
* Logs to: [Langfuse](../../observability/langfuse/index.md)
* Comparison: [Runtime alternatives](../alternatives.md)
