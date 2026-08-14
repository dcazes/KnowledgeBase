---
type: Reference
title: Dify — Model Providers
description: Connecting LLMs to Dify, including OpenAI-API-compatible endpoints like your local :4000 OpenRouter/NIM failover proxy.
resource: https://docs.dify.ai/guides/model-configuration
tags: [dify, models, openai-compatible, openrouter, providers, configuration]
generated: { by: "human:daniel", at: "2026-07-09T00:55:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:55:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: model-configuration-docs
    resource: "https://docs.dify.ai/guides/model-configuration"
    title: "Model configuration (docs)"
    author: "site:docs.dify.ai"
  - id: supported-providers
    resource: "https://docs.dify.ai/getting-started/readme/model-providers"
    title: "Supported providers"
    author: "site:docs.dify.ai"
  - id: architecture-proxy-fit
    resource: "model-providers.md"
    title: "Architecture / proxy fit"
---

# Model support

Dify integrates **hundreds** of proprietary/open LLMs from dozens of providers, plus **any OpenAI-API-compatible model** (GPT, Mistral, Llama3, local servers, proxies).

# Adding a provider

In the UI: **Settings → Model Provider → Add**. Two common paths:

1. **Hosted provider** (OpenAI, Anthropic, etc.) — enter API key.
2. **OpenAI-API-compatible** — point at a base URL. **This is how you use your `:4000` proxy.**

# Using your `:4000` OpenRouter/NIM proxy

Your stack routes inference through a local failover proxy on `:4000` (per the KB plan). Add it as an OpenAI-compatible endpoint:

```
Provider type: OpenAI-API-compatible
Base URL:      http://localhost:4000/v1
API Key:       <any non-empty value the proxy accepts>
Model:         <model name exposed by the proxy, e.g. a free model>
```

Set the same in `docker/.env` if you want it as a default, or configure per-app in the UI. Both chat and **embedding** models can be pointed at compatible endpoints (needed for [RAG Pipeline](rag-pipeline.md)).

# Provider categories

* **LLM** — chat/completion models.
* **Embedding** — vectorization for RAG.
* **Rerank** — reorders retrieved chunks (improves relevance).
* **Text-to-speech / Speech-to-text** — optional modalities.
* **Moderation** — content filtering.

# Tips

* Match embedding model dimensions to your vector store.
* For heavy local use, prefer cloud endpoints via the proxy (your GTX 1060 can't run big models well).
* System models (OpenAI-compatible) are the simplest to wire to the proxy.
