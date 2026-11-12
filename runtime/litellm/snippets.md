---
type: Reference
title: LiteLLM Snippets
description: LiteLLM snippets — SDK completion across providers, Router with fallbacks, proxy requests with curl, creating virtual keys with budgets, and loading MCP tools.
resource: https://docs.litellm.ai
tags: [litellm, snippets, python, curl, cheat-sheet]
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

# LiteLLM — Snippets

## SDK

```python
from litellm import completion
r = completion(model="openai/gpt-4o", messages=[{"role": "user", "content": "Hello"}])
r = completion(model="ollama_chat/qwen3:8b", api_base="http://localhost:11434",
               messages=[{"role": "user", "content": "Hello"}])
print(r.choices[0].message.content)
```

## Router with fallback

```python
from litellm import Router
router = Router(model_list=[
    {"model_name": "local", "litellm_params": {"model": "ollama_chat/qwen3:8b", "api_base": "http://localhost:11434"}},
    {"model_name": "cloud", "litellm_params": {"model": "openai/gpt-4o-mini"}},
], fallbacks=[{"local": ["cloud"]}])
resp = router.completion(model="local", messages=[{"role": "user", "content": "Hi"}])
```

## Proxy request

```bash
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_API_KEY" -H "Content-Type: application/json" \
  -d '{"model": "local", "messages": [{"role": "user", "content": "Hello"}]}'
```

## Virtual key with a budget

```bash
curl http://localhost:4000/key/generate -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"models": ["local", "smart"], "max_budget": 10, "budget_duration": "30d", "metadata": {"user": "alice"}}'
```

## MCP tools in OpenAI format

```python
from litellm import mcp_client      # with an open MCP ClientSession
tools = await mcp_client.load_mcp_tools(session=session, format="openai")
```

## Related

[LiteLLM index](index.md) · [Configuration](configuration.md)
