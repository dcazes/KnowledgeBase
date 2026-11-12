---
type: Reference
title: LiteLLM Configuration
description: LiteLLM proxy config.yaml — model_list with hosted and local deployments, router settings and fallbacks, general settings for keys and database, and logging callbacks.
resource: https://docs.litellm.ai/docs/proxy/configs
tags: [litellm, configuration, config-yaml, fallbacks, langfuse]
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

# LiteLLM — Configuration

```yaml
model_list:
  - model_name: smart                     # the name clients request
    litellm_params:
      model: anthropic/claude-sonnet-4-5
      api_key: os.environ/ANTHROPIC_API_KEY
  - model_name: local
    litellm_params:
      model: ollama_chat/qwen3:14b
      api_base: http://ollama:11434
  - model_name: local                     # second deployment = load balancing
    litellm_params:
      model: hosted_vllm/Qwen/Qwen3-14B
      api_base: http://vllm:8000/v1
  - model_name: embed
    litellm_params:
      model: ollama/nomic-embed-text
      api_base: http://ollama:11434

router_settings:
  routing_strategy: simple-shuffle        # or least-busy, latency-based-routing, usage-based-routing
  num_retries: 2
  fallbacks: [{ "local": ["smart"] }]     # if local fails, use smart
  context_window_fallbacks: [{ "local": ["smart"] }]

litellm_settings:
  success_callback: ["langfuse"]          # also otel, datadog, etc.
  cache: true

general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
  database_url: os.environ/DATABASE_URL
```

`os.environ/NAME` reads secrets from the environment so they stay out of the file.

Model names here are examples; use whatever your providers currently offer.

## Related

[LiteLLM index](index.md) · [Snippets](snippets.md) · [Langfuse](../../observability/langfuse/index.md) · [vLLM](../vllm/index.md)
