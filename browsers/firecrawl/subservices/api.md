---
type: Reference
title: Firecrawl API & Workers
description: The Firecrawl API service and its queue workers — responsibilities, scaling with NUM_WORKERS_PER_QUEUE, authentication and admin routes.
resource: https://github.com/firecrawl/firecrawl/tree/main/apps/api
tags: [firecrawl, api, workers, subservice]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: firecrawl-selfhost
    resource: "https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md"
    title: "Self-hosting Firecrawl"
    author: "site:github.com"
---

# Firecrawl — API & Workers

The `apps/api` service exposes the v2 REST API on port 3002 and runs workers that pull jobs from the queue. Workers fetch pages (directly or via the [Playwright service](playwright-service.md)), convert HTML to Markdown, call an LLM for JSON extraction when requested, and store results.

* Scale throughput with `NUM_WORKERS_PER_QUEUE` and by running more worker replicas.
* `USE_DB_AUTHENTICATION=true` enforces API keys; leave it off only for private local use.
* `BULL_AUTH_KEY` enables `/admin/...` routes, including a queue dashboard; protect it like a password.

## Related

[Subservices](index.md) · [Self-hosting](../self-hosting.md) · [API reference](../api-reference.md)
