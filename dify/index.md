---
type: Reference
title: Dify
description: Open-source LLM application development platform — visual AI workflows, RAG pipelines, autonomous agents — documented as reference.
resource: https://github.com/langgenius/dify
tags: [dify, llmops, workflows, rag, agents]
timestamp: 2026-08-12T00:00:00Z
---

# Dify

Open-source **LLM application development platform** — visual AI workflows, RAG pipelines, autonomous agents, model management, and LLMOps in one self-hosted stack. Documented here as a **reference / available-to-deploy** app; the source is present at `programs/archive/dify/` but no container is currently running.

## Contents

* [Overview](overview.md) - what Dify is, key features, editions
* [Installation](installation.md) - Docker deploy from `docker/`, env, dashboard at :80
* [Architecture](architecture.md) - the container set: api, worker, web, db, redis, sandbox, plugin_daemon, ssrf_proxy, nginx, vector stores
* [RAG Pipeline](rag-pipeline.md) - document ingestion → indexing → retrieval
* [Workflows & Agents](workflows-agents.md) - visual canvas, agent types, 50+ tools
* [Model Providers](model-providers.md) - connecting LLMs (incl. your :4000 OpenRouter proxy)
* [API](api.md) - Backend-as-a-Service endpoints + API keys
* [Alternatives](alternatives.md) - Flowise, n8n, LangChain, AnythingLLM, OpenWebUI
* [Snippets](snippets.md) - deploy + common tasks cheat sheet

## Instance facts (from local source)

* **Source:** `programs/archive/dify/` (LangGenius/Dify monorepo — archived out of active programs; no container currently running)
* **Deploy path:** `programs/archive/dify/docker/` — `cp .env.example .env && docker compose up -d`
* **Dashboard:** `http://localhost/install` (nginx on :80) after first launch
* **Async:** Celery workers (`worker`, `worker_beat`) + Redis broker
* **Vector store:** configurable — weaviate / qdrant / pgvector / chroma / milvus (pick one)
* **Plugins:** `plugin_daemon` service serves tools/integrations

## Cross-references

* **AnythingLLM / OpenWebUI** — lighter turnkey RAG/chat — see [AnythingLLM Overview](../anythingllm/overview.md) & [OpenWebUI Overview](../openwebui/overview.md)
* **Graphify** — can structure Dify RAG outputs into a knowledge graph — see [Graphify AI Integration](../graphify/ai-integration.md)
* **SearXNG** — Dify can use SearXNG for web search — see [SearXNG AI Integration](../searxng/ai-integration.md)
* **Firecrawl** — Dify RAG can ingest Firecrawl-extracted content — see [Firecrawl AI Integration](../firecrawl/ai-integration.md)

## Last verified

**2026-08-12** — **v1.16.1** (2026-07-28) upstream; local compose (archive) pins `langgenius/dify-api:1.15.0`. Source path corrected to `programs/archive/dify/`. Prior verification 2026-07-09 against local docker/ and upstream docs.dify.ai.

# Citations

[1] [Dify GitHub](https://github.com/langgenius/dify)
[2] [Dify docs](https://docs.dify.ai)
[3] [Local source - programs/archive/dify/](/../../programs/archive/dify/)