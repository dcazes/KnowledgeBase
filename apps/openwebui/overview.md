---
type: Software
title: OpenWebUI — Overview
description: Self-hosted AI chat platform supporting Ollama and OpenAI-compatible APIs, with built-in RAG, agents, plugins, and web search for RAG.
resource: https://github.com/open-webui/open-webui
tags: [openwebui, llm, chat, rag, self-hosted, ollama, openai-compatible]
generated: { by: "human:daniel", at: "2026-07-09T02:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T02:00:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: openwebui-github
    resource: "https://github.com/open-webui/open-webui"
    title: "OpenWebUI GitHub"
    author: "site:github.com"
  - id: key-features-readme
    resource: "https://github.com/open-webui/open-webui#key-features-of-open-webui-"
    title: "Key features (README)"
    author: "site:github.com"
  - id: docs
    resource: "https://docs.openwebui.com"
    title: "Docs"
    author: "site:docs.openwebui.com"
---

# What OpenWebUI is

OpenWebUI is an **extensible, feature-rich, self-hosted AI platform** designed to run entirely offline if needed. It provides a chat UI over any LLM — local runners like **Ollama** or **any OpenAI-compatible API** — plus a built-in inference engine for RAG, agents, and a plugin system.

# Key features (from upstream README)

* **Effortless setup** — pip, uv, Docker, or Kubernetes (kubectl/kustomize/helm). Tagged images `:ollama` and `:cuda`.
* **Broad model & API integration** — connect any OpenAI-compatible API alongside local Ollama. Point the API URL at LMStudio, GroqCloud, Mistral, **OpenRouter**, vLLM, and more.
* **Plugin support** — extend with Filters, Actions, Pipes, Tools, and Skills. Connect external services via MCP, MCPO, and OpenAPI tool servers.
* **Models & agents** — wrap any base model with custom instructions, tools, and knowledge to build specialized agents. Dynamic variables, per-user/group access control, community preset imports.
* **Persistent artifact storage** — built-in key-value storage API for artifacts (journals, trackers, collaborative tools).
* **Local RAG** — retrieval augmented generation backed by **9 vector databases** and multiple content-extraction engines (Tika, Docling, Document Intelligence, Mistral OCR, PaddleOCR-vl, external loaders). Hybrid search (BM25 + vector) with reranking and full-context mode.
* **Web Search for RAG** — search via dozens of providers including **SearXNG**, Brave, Kagi, Tavily, Perplexity, **Firecrawl**, DuckDuckGo, SerpApi, Bing, Jina, Exa, and more, injecting results into the conversation.

# Architecture (high level)

```
Browser ──HTTP──► OpenWebUI (Svelte/Python backend, :8080 in container)
                      │
                      ├─ Model connections: Ollama (:11434) | OpenAI-compatible (:4000 proxy here)
                      ├─ RAG: vector DB (e.g. chroma) + document loaders
                      ├─ Web Search providers: SearXNG, Firecrawl, ...
                      └─ Plugins/Tools/Skills (MCP, OpenAPI)
```

# Where it fits in your stack

OpenWebUI is the **chat front-end** layer. It complements:
* **AnythingLLM** — also a RAG chat tool (turnkey).
* **Dify** — the app/workflow builder.
* **SearXNG / Firecrawl** — used here as OpenWebUI's *web search for RAG* providers.
* **:4000 proxy** — the inference endpoint (since no Ollama runs locally).

# License note

Open WebUI uses a custom **Open WebUI License** (branding must be preserved) with some prior contributions under their original licenses. Check `LICENSE`/`LICENSE_HISTORY` upstream before redistribution.
