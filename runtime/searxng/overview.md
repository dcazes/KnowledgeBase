---
type: Software
title: SearXNG — Overview
description: Self-hosted, privacy-respecting metasearch engine that fans a query out to many search engines, deduplicates, and returns unified results.
resource: https://docs.searxng.org/
tags: [searxng, metasearch, privacy, self-hosted, search, search-api]
generated: { by: "human:daniel", at: "2026-07-08T23:10:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-08T23:10:00Z" } ]
status: stable
stale_after: 2027-01-04
sources:
  - id: searxng-overview-docs
    resource: "https://docs.searxng.org/"
    title: "SearXNG overview / docs"
    author: "site:docs.searxng.org"
  - id: searxng-github
    resource: "https://github.com/searxng/searxng"
    title: "SearXNG GitHub"
    author: "site:github.com"
  - id: configured-engines-categories
    resource: "https://docs.searxng.org/user/configured_engines.html"
    title: "Configured engines & categories"
    author: "site:docs.searxng.org"
  - id: local-config-programs-firecrawl-firecrawl-searxng-config
    resource: "/../../programs/firecrawl/firecrawl/searxng-config/"
    title: "Local config - programs/firecrawl/firecrawl/searxng-config/"
---

# What SearXNG is

SearXNG is a free, open-source **metasearch engine**. Instead of crawling the web itself, it forwards your query to many upstream search engines (Google, Bing, DuckDuckGo, Brave, GitHub, arXiv, Wikipedia, YouTube, …), merges and de-duplicates the results, and returns them through one interface — in HTML for humans or JSON/CSV/RSS for programs.

Key properties:

* **License:** AGPLv3.
* **Origin:** A fork of SearX, actively maintained since 2021.
* **Privacy:** No tracking, no user profiling, no stored search history. Upstream engines see *SearXNG's* egress IP, not yours.
* **Self-hosted:** Runs as a Docker container on this machine (see [Installation](installation.md)).
* **API-friendly:** JSON/CSV/RSS output for the AI stack (see [API](api.md)).

# Why it matters here

On this machine SearXNG is the **web-search substrate** for the agent stack:

* **Firecrawl** is pointed at it via `SEARXNG_URL=http://searxng:8080` (see [AI Integration](ai-integration.md)).
* **AnythingLLM / Hermes / OpenCode** can call its `/search?format=json` endpoint directly for grounded web lookups.
* **Graphify** can ingest result URLs into the knowledge graph.

# Architecture

```
Query (browser / Firecrawl / AnythingLLM / script)
        │
        ▼
SearXNG  (metasearch orchestrator, host :8088)
        │  fan-out
        ├────────────┬────────────┬────────────┐
        ▼            ▼            ▼            ▼
    Google       Bing       DuckDuckGo     GitHub / arXiv / …
   (scrape)     (scrape)     (scrape)       (API/scrape)
        │            │            │            │
        └────────────┴─────┬──────┴────────────┘
                           ▼
              Deduplicate + rank + format
                           │
                           ▼
              Unified results (HTML / JSON / CSV / RSS)
```

# Query categories

SearXNG groups engines into categories. Your instance can query (defaults apply unless overridden):

| Category | Example engines |
|----------|-----------------|
| `general` | Google, Bing, DuckDuckGo, Brave, Qwant, Startpage |
| `images` | Google Images, Bing Images, Flickr, Unsplash |
| `videos` | YouTube, Vimeo, Dailymotion, PeerTube |
| `news` | Google News, Bing News, Reddit, Hacker News |
| `code` | GitHub, GitLab, Stack Overflow |
| `academic` | Google Scholar, arXiv, PubMed, Semantic Scholar |
| `maps` | OpenStreetMap, Google Maps, Bing Maps |
| `music` | SoundCloud, Bandcamp |
| `files` | GitHub, GitLab, general file search |

Engines are enabled/disabled per category in `settings.yml` (see [Configuration](configuration.md)).

# Privacy model

What SearXNG does **not** do:

* No cookies (unless you enable them for preferences persistence).
* No IP logging of users.
* No stored search history.
* No user profiling.

What upstream engines see:

* The query from **SearXNG's egress IP** (this machine), not your browser's IP.
* No persistent identifier tied to you.

A localhost instance means queries originate from your own machine — maximum practical privacy for a single-user setup.

# Performance characteristics

| Metric | Typical |
|--------|---------|
| Query latency | 1–3 s (depends on engine count) |
| Results per query | 50–200 aggregated |
| Memory usage | ~200–500 MB (container) |
| CPU | Low idle, I/O-bound spikes on query |
