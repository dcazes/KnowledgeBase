---
type: Reference
title: Dify — AI Integration
description: Connecting Dify to your stack — model providers via the :4000 proxy, SearXNG web search, Firecrawl web ingestion, and Graphify structuring of RAG outputs.
resource: https://docs.dify.ai
tags: [dify, integration, searxng, firecrawl, graphify, openai-compatible, rag]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: dify-docs
    resource: "https://docs.dify.ai"
    title: "Dify docs"
    author: "site:docs.dify.ai"
  - id: dify-model-providers
    resource: "https://docs.dify.ai/guides/model-configuration"
    title: "Dify model providers"
    author: "site:docs.dify.ai"
  - id: firecrawl-api
    resource: "https://docs.firecrawl.dev/api-reference"
    title: "Firecrawl API"
    author: "site:docs.firecrawl.dev"
  - id: searxng-api
    resource: "https://docs.searxng.org/dev/search_api.html"
    title: "SearXNG API"
    author: "site:docs.searxng.org"
---

# Models via the :4000 proxy

Dify's **model providers** panel accepts any **OpenAI-compatible** endpoint. Point Dify at your `:4000` LiteLLM/OpenRouter proxy for chat, completion, and embedding models — see [Model Providers](model-providers.md).

# Web search via SearXNG

Dify apps can use **SearXNG** as a search tool for agent steps and knowledge fetching:

* Configure a custom tool or HTTP request node pointing at `http://localhost:8088/search?q={{query}}&format=json` (host port `8088` → container `8080`; in-network, use `http://searxng:8080` on the `backend` network — verified 2026-08-12).
* The JSON API returns results that Dify's workflow nodes can parse directly.

# Web content via Firecrawl

Dify RAG pipelines and workflows can ingest web content through **Firecrawl** (self-hosted on `:3002`):

* Use Firecrawl's `/v2/scrape` or `/v2/crawl` endpoints from a workflow **HTTP request** node or a custom tool.
* Feed extracted Markdown into Dify's knowledge-base ingestion step.

# Knowledge graph via Graphify

Graphify can structure the outputs of Dify RAG pipelines into a knowledge graph — see [Graphify AI Integration](../../memory/graphify/ai-integration.md).

# Deployment status

Source is at `programs/archive/dify/` (archived; upstream v1.16.1, local compose pins `langgenius/dify-api:1.15.0`). No container is currently running. See [Installation](installation.md) to bring it up.
