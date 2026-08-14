---
type: Reference
title: Firecrawl
description: Open-source web context API to search, scrape, crawl, and extract the web into clean Markdown/JSON for AI agents — self-hosted on this machine.
resource: https://github.com/firecrawl/firecrawl
tags: [firecrawl, web-scraping, crawling, self-hosted, search]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: firecrawl-github
    resource: "https://github.com/firecrawl/firecrawl"
    title: "Firecrawl GitHub"
    author: "site:github.com"
  - id: self-hosting-docs-self-host-md
    resource: "https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md"
    title: "Self-hosting docs (SELF_HOST.md)"
    author: "site:github.com"
  - id: local-stack-programs-firecrawl-firecrawl-docker-compose-yaml
    resource: "/../../programs/firecrawl/firecrawl/docker-compose.yaml"
    title: "Local stack - programs/firecrawl/firecrawl/docker-compose.yaml"
---

# Firecrawl

Open-source **web context API** to search, scrape, crawl, and extract the web into clean Markdown / structured JSON / screenshots for AI agents. On this machine it runs as a **self-hosted Docker stack** (6 services + SearXNG) and is the scraping/extraction engine behind the agent stack.

## Contents

* [Overview](overview.md) - what Firecrawl is, architecture, v2 endpoint map
* [Subservices](subservices/index.md) - one topic per container: api, playwright-service, redis, rabbitmq, nuq-postgres, foundationdb
  * [API](subservices/api.md) · [Playwright Service](subservices/playwright-service.md) · [Redis](subservices/redis.md) · [RabbitMQ](subservices/rabbitmq.md) · [NUQ Postgres](subservices/nuq-postgres.md) · [FoundationDB](subservices/foundationdb.md)
* [API Reference](api-reference.md) - v2 endpoints with request/response examples
* [CLI](cli.md) - firecrawl-cli + firecrawl-skills
* [Self-Hosting](self-hosting.md) - compose, env vars, SearXNG wiring, limitations
* [AI Integration](ai-integration.md) - SearXNG search backend, agents/MCP
* [Alternatives](../alternatives.md) - ScraperAPI, Crawl4AI, Playwright, Apify, Jina AI
* [Snippets](snippets.md) - copy-paste cheat sheet

## Instance facts (from local compose + SELF_HOST.md)

* **Stack:** `programs/firecrawl/firecrawl/docker-compose.yaml` — services `api`, `playwright-service`, `redis`, `rabbitmq`, `nuq-postgres`, `foundationdb`, plus our added `searxng`.
* **API port:** `3002` (host), `INTERNAL_PORT=3002`. Exposed by the `firecrawl-api` service in the compose.
* **Search backend:** `SEARXNG_ENDPOINT` defaults to `http://searxng:8080` (our SearXNG instance, host port 8088) — see [AI Integration](ai-integration.md).
* **Self-host caveats:** no Fire-engine (advanced anti-bot); Google search by default unless SearXNG configured; proxies/extra engines need manual `.env`.

## Cross-references

* **SearXNG** provides the `/search` backend for Firecrawl — see [SearXNG AI Integration](../../runtime/searxng/ai-integration.md)
* **AnythingLLM** can use Firecrawl via its web-search skill — see [AnythingLLM AI Integration](../../apps/anythingllm/ai-integration.md)
* **Hermes** & **OpenCode** can call Firecrawl's `/v2/scrape` and `/v2/crawl` endpoints — see [Hermes AI Integration](../../agents/hermes/ai-integration.md) & [OpenCode AI Integration](../../agents/opencode/ai-integration.md)
* **Graphify** can ingest Firecrawl-extracted URLs — see [Graphify AI Integration](../../memory/graphify/ai-integration.md)
* **Dify** RAG pipelines can pull web content via Firecrawl — see [Dify AI Integration](../../agents/dify/ai-integration.md)

## Last verified

**2026-08-12** — **v2.11.192** (2026-08-07); stack and env verified against local `programs/firecrawl/firecrawl/docker-compose.yaml` and running containers (api :3002, agent_searxng :8088).
