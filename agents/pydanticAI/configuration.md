---
type: Reference
title: Pydantic AI Configuration
description: Choosing models in Pydantic AI — provider-prefixed model strings, explicit model and provider objects for local or gateway endpoints, fallback models, and model settings such as temperature and token limits.
resource: https://pydantic.dev/docs/ai/
tags: [pydantic-ai, configuration, models, providers, ollama]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pydantic-ai-docs
    resource: "https://pydantic.dev/docs/ai/"
    title: "Pydantic AI documentation"
    author: "site:pydantic.dev"
---

# Pydantic AI — Configuration

## Model strings

`"openai:gpt-5-mini"`, `"anthropic:claude-sonnet-4-5"`, `"google-gla:gemini-2.5-flash"`, `"groq:llama-3.3-70b-versatile"`, `"bedrock:…"` — the prefix selects the provider. Model names here are examples.

## Local and gateway endpoints

```python
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider

model = OpenAIChatModel("qwen3:8b", provider=OllamaProvider(base_url="http://localhost:11434/v1"))
agent = Agent(model)
```

Use `OpenAIProvider(base_url=...)` for [vLLM](../../runtime/vllm/index.md), [LM Studio](../../runtime/lmstudio/index.md) or a [LiteLLM](../../runtime/litellm/index.md) gateway.

## Fallback and settings

```python
from pydantic_ai.models.fallback import FallbackModel
agent = Agent(FallbackModel("openai:gpt-5-mini", "anthropic:claude-haiku-4-5"),
              model_settings={"temperature": 0.2, "max_tokens": 2000})
```

## Related

[Pydantic AI index](index.md) · [Snippets](snippets.md) · [Local inference](../../concepts/local-inference.md)
