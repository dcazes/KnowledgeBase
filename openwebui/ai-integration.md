---
type: Reference
title: OpenWebUI — AI Integration
description: Connecting OpenWebUI to your stack — Ollama/OpenAI-compatible :4000 endpoint, built-in RAG, SearXNG web search, and Firecrawl extraction.
resource: https://docs.openwebui.com
tags: [openwebui, integration, ollama, openai-compatible, rag, searxng, firecrawl]
timestamp: 2026-08-12T00:00:00Z
---

# Models via Ollama / OpenAI-compatible endpoint

OpenWebUI connects to **Ollama** (`http://host.docker.internal:11434` or host bridge `172.17.0.1:11434`) and any **OpenAI-compatible** endpoint — e.g. your `:4000` proxy. The prebuilt image ships without bundled Ollama; both connection types are configured in the admin panel.

# RAG & web search

* **RAG** — built-in ingestion with configurable chunking/retrieval; see [RAG](rag.md).
* **Web search** — point OpenWebUI at **SearXNG** (`http://host.docker.internal:8088`) or use **Firecrawl** (`:3002`) as an extraction provider for grounded answers.

# Pipe functions & integrations

OpenWebUI's **pipe functions** (Python) can wrap arbitrary stack endpoints — e.g. Graphify ingestion or Dify workflow calls — as chat models/tools.

# Deployment status

Compose present at `programs/openwebui/docker-compose.yaml` (image `ghcr.io/open-webui/open-webui:main`, host port `3001` → container `8080`, upstream v0.11.0); **not currently running** as of 2026-08-12. See [Installation](installation.md).

# Citations

[1] [OpenWebUI docs](https://docs.openwebui.com)
[2] [OpenWebUI OpenAI API / Ollama connection](https://docs.openwebui.com/getting-started/env-configuration)
[3] [SearXNG API](https://docs.searxng.org/dev/search_api.html)
[4] [Firecrawl API](https://docs.firecrawl.dev/api-reference)
