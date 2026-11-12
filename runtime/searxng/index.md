---
type: Software
title: SearXNG
description: Free, self-hosted metasearch engine that aggregates results from 200+ search services without tracking users — the most common private web-search backend for AI agents, chat UIs and scrapers via its JSON API.
resource: https://docs.searxng.org
tags: [searxng, metasearch, web-search, privacy, self-hosting, python]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: searxng-docs
    resource: "https://docs.searxng.org"
    title: "SearXNG documentation"
    author: "site:docs.searxng.org"
  - id: searxng-github
    resource: "https://github.com/searxng/searxng"
    title: "searxng/searxng on GitHub"
    author: "site:github.com"
---

# SearXNG

**SearXNG** queries many search engines (Google, Bing, DuckDuckGo, Brave, Wikipedia, GitHub, arXiv and hundreds more) on your behalf, merges the results and returns them without profiling you. For AI stacks its key feature is a **JSON API**: chat UIs, agents and crawlers use it as a free, private web-search tool instead of paid search APIs.

| | |
|---|---|
| Category | [Web scraping & search](../../concepts/web-scraping.md) · [Self-hosting](../../concepts/self-hosting.md) |
| License | AGPL-3.0 |
| Language | Python |
| Releases | Rolling — container images rebuilt from `master` continuously (no versioned releases) |
| Default port | 8080 in the container |

## Contents

* [Overview](overview.md) — how metasearch works, engines and categories, privacy model
* [Installation](installation.md) — container compose template, Docker, reverse proxy
* [Configuration](configuration.md) — `settings.yml`, enabling JSON, limiter, engines
* [Search syntax](syntax.md) — bangs, language and category modifiers
* [API](api.md) — `/search` parameters and JSON response
* [Snippets](snippets.md) — curl and Python examples
* [AI Integration](ai-integration.md) — Open WebUI, Firecrawl, agents, MCP

## Related

* Concepts: [Web scraping & search](../../concepts/web-scraping.md) · [RAG](../../concepts/rag.md) · [Tool calling](../../concepts/tool-calling.md)
* Used by: [Open WebUI](../../apps/openwebui/index.md), [Firecrawl](../../browsers/firecrawl/index.md), [SurfSense](../../browsers/surfsense/index.md), [AnythingLLM](../../apps/anythingllm/index.md), [Hermes](../../agents/hermes/index.md), [Dify](../../agents/dify/index.md), [n8n](../../apps/n8n/index.md)
* Runs on: [Docker](../docker/index.md)
* Comparison: [Runtime alternatives](../alternatives.md)
