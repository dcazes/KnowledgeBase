---
type: Reference
title: OpenWebUI — RAG & Web Search
description: Built-in local RAG (9 vector DBs, hybrid search, reranking) and wiring SearXNG + Firecrawl as web-search-for-RAG providers.
resource: https://docs.openwebui.com/features/rag/
tags: [openwebui, rag, web-search, searxng, firecrawl, vector-db, retrieval]
timestamp: 2026-07-09T02:03:00Z
---

# Built-in RAG

OpenWebUI has a built-in RAG engine:
* **9 vector databases** supported (chroma is common default).
* **Content extraction** via Tika, Docling, Document Intelligence, Mistral OCR, PaddleOCR-vl, external loaders.
* **Hybrid search** — BM25 (keyword) + vector, with **reranking** and a **full-context mode**.
* Documents load into chat or a library (reference them with the `#` command).

# Web Search for RAG

OpenWebUI can **search the web and inject results into the conversation**. This stack wires two self-hosted providers (set their endpoints as below):
* **SearXNG** — metasearch; set the endpoint to `http://searxng:8080` (or `http://localhost:8088`).
* **Firecrawl** — web context API; set the endpoint to `http://localhost:3002` with your Firecrawl API key.

Other providers (Brave, Tavily, Perplexity, DuckDuckGo, SerpApi, Bing, Jina, Exa, …) are available if you have keys.

# Wiring SearXNG

In **Admin Settings → Web Search**:
```
Enable:        on
Provider:      SearXNG
SearXNG URL:   http://searxng:8080      # or http://localhost:8088 from host
```
Then SearXNG results are pulled into RAG/chat. This is the same SearXNG instance built earlier in this KB.

# Wiring Firecrawl

```
Provider:   Firecrawl
Base URL:   http://localhost:3002
API Key:    <FIRECRAWL_API_KEY>
```
Firecrawl returns clean Markdown/JSON for the agent to ingest.

# Local vs web RAG

* **Local RAG** — your uploaded documents (vector store), private.
* **Web RAG** — live web via SearXNG/Firecrawl, for current info.

Both feed the same retrieval pipeline (hybrid + rerank).

# Citations

[1] [RAG features (docs)](https://docs.openwebui.com/features/rag/)
[2] [Web search providers (README)](https://github.com/open-webui/open-webui#-web-search-for-rag)
[3] [SearXNG endpoint](/../../searxng/index.md)
[4] [Firecrawl endpoint](/../../firecrawl/index.md)
