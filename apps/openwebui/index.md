---
type: Reference
title: OpenWebUI
description: Self-hosted AI chat platform with RAG + web search — documented as reference; compose present locally, not currently running.
resource: https://github.com/open-webui/open-webui
tags: [openwebui, chat, rag, self-hosted]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: openwebui-github
    resource: "https://github.com/open-webui/open-webui"
    title: "OpenWebUI GitHub"
    author: "site:github.com"
  - id: openwebui-docs
    resource: "https://docs.openwebui.com/"
    title: "OpenWebUI docs"
    author: "site:docs.openwebui.com"
---

# OpenWebUI

Self-hosted AI chat platform (served on `:3001`); RAG + web search. Documented here as a **reference / available-to-deploy** app — no deployment directory is currently present on this machine, so it is not running.

## Contents

* [Overview](overview.md) - what OpenWebUI is, key features
* [Installation](installation.md) - Docker deploy, env, admin setup
* [Features](features.md) - pipelines, RAG, web search, model management
* [RAG](rag.md) - document ingestion, chunking, retrieval
* [Configuration](configuration.md) - env vars, auth, model config
* [API](api.md) - REST endpoints, API keys
* [Alternatives](alternatives.md) - AnythingLLM, LibreChat, ChatGPT-Next-Web
* [Snippets](snippets.md) - deploy + common tasks cheat sheet

## Instance facts (from local source)

* **Port:** 3001 (host) → 8080 (container)
* **Backend:** Ollama / OpenAI-compatible (your :4000 proxy)
* **RAG:** built-in document ingestion
* **Web search:** configurable (can use SearXNG)
* **Image:** `ghcr.io/open-webui/open-webui:main` (prebuilt, no bundled Ollama)
* **Status:** documented for reference; compose present at `programs/openwebui/docker-compose.yaml`, **not currently running** (no container up as of 2026-08-12).

## Cross-references

* **SearXNG** — OpenWebUI can use SearXNG for web search — see [SearXNG AI Integration](../../runtime/searxng/ai-integration.md)
* **AnythingLLM** — similar RAG chat app — see [AnythingLLM Overview](../anythingllm/overview.md)
* **Dify** — more workflow-oriented LLM platform — see [Dify Overview](../../agents/dify/overview.md)
* **Graphify** — can ingest OpenWebUI chats — see [Graphify AI Integration](../../memory/graphify/ai-integration.md)
* **Firecrawl** — can extract web content for RAG — see [Firecrawl AI Integration](../../browsers/firecrawl/ai-integration.md)

## Last verified

**2026-08-12** — **v0.11.0** (2026-07-27). Port corrected to 3001→8080; compose at `programs/openwebui/docker-compose.yaml`. Prior verification 2026-07-09 against upstream docs.openwebui.com.
