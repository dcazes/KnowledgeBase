---
type: Reference
title: SearXNG
description: Privacy-focused, self-hosted metasearch engine — the web-search backbone for the AI stack on this machine.
resource: https://docs.searxng.org
tags: [searxng, search, metasearch, privacy, firecrawl]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: searxng-documentation
    resource: "https://docs.searxng.org/"
    title: "SearXNG documentation"
    author: "site:docs.searxng.org"
  - id: local-config-programs-firecrawl-firecrawl-searxng-config
    resource: "/../../programs/firecrawl/firecrawl/searxng-config/"
    title: "Local config - programs/firecrawl/firecrawl/searxng-config/"
  - id: local-compose-searxng-embedded-in-firecrawl
    resource: "/../../programs/firecrawl/firecrawl/docker-compose.yaml"
    title: "Local compose (searxng embedded in firecrawl)"
---

# SearXNG

Privacy-focused, self-hosted **metasearch engine** that aggregates results from many search services (Google, Bing, DuckDuckGo, GitHub, arXiv, …) without tracking users. It is the web-search backbone for the AI stack on this machine (Firecrawl queries it, AnythingLLM/Hermes/OpenCode can too).

## Contents

* [Overview](overview.md) - what SearXNG is, architecture, privacy model, license, query categories
* [Installation](installation.md) - Docker deployment from the local compose, settings mount, start & verify
* [Configuration](configuration.md) - `settings.yml` anatomy, engines, rate limiting, caching, image proxy, preferences UI
* [API](api.md) - JSON/CSV/RSS `/search` API: parameters, response schema, code examples
* [Syntax](syntax.md) - `!engine` / `!category` / `!language` shortcuts, boolean operators, `site:`/`filetype:`, time filters
* [AI Integration](ai-integration.md) - Firecrawl, AnythingLLM, Hermes/OpenCode/Graphify, custom scripts
* [Alternatives](alternatives.md) - LibreX, SearX (upstream), Brave Search API, SerpAPI + pros/cons
* [Snippets](snippets.md) - deploy / query / config / troubleshoot cheat sheet

## Instance facts (from config, not live state)

* **Configured URL:** container listens on `8080`. In the Firecrawl compose it publishes host `8088:8080` (localhost:8088, verified 2026-08-12 via `docker ps`). SearXNG runs as the embedded `searxng` service inside `programs/firecrawl/firecrawl/docker-compose.yaml` (service name `agent_searxng`, on the `backend` network). Verify the actual mount with `docker inspect agent_searxng --format '{{json .Mounts}}'`.
* **Formats enabled (your `settings.yml`):** `html`, `json`, `csv` (no `rss`).
* **Settings mode:** `use_default_settings: true` — almost everything is default; your file only overrides `server` + `search.formats`.
* **Verify it is up (run locally):**
  ```bash
  curl -s "http://127.0.0.1:8088/search?q=test&format=json" | head -c 200
  ```

## Cross-references

* **Firecrawl** uses SearXNG as its search backend via `SEARXNG_ENDPOINT` — see [Firecrawl AI Integration](../../browsers/firecrawl/ai-integration.md)
* **AnythingLLM** web-search skill calls SearXNG directly — see [AnythingLLM AI Integration](../../apps/anythingllm/ai-integration.md)
* **Hermes** & **OpenCode** can query SearXNG for grounded web lookups — see [Hermes AI Integration](../../agents/hermes/ai-integration.md) & [OpenCode AI Integration](../../agents/opencode/ai-integration.md)
* **Graphify** can ingest SearXNG result URLs — see [Graphify AI Integration](../../memory/graphify/ai-integration.md)
* **SurfSense** bundles its own SearXNG as the metasearch backend (container-internal :8080) — see [SurfSense](../../browsers/surfsense/index.md)

## Last verified

**2026-08-12** — Rolling release (2026.8.10 build); host port corrected to `8088` (verified against running `agent_searxng` container). Prior verification 2026-07-09 against local `programs/firecrawl/firecrawl/searxng-config/settings.yml` and upstream docs.searxng.org; re-pointed 2026-07-15 after SearXNG was merged into the Firecrawl compose.
