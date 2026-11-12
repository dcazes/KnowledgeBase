---
type: Reference
title: Firecrawl Redis
description: Redis in a self-hosted Firecrawl stack — rate limiting, caching and coordination between API and workers.
resource: https://github.com/firecrawl/firecrawl
tags: [firecrawl, redis, subservice]
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

# Firecrawl — Redis

Redis holds short-lived shared state: rate-limit counters, caches, locks and coordination data used by the API and workers. Data is mostly ephemeral; losing it interrupts in-flight jobs but not durable results. Keep it on the internal Compose network with no published port.

## Related

[Subservices](index.md) · [Docker volumes & networks](../../../runtime/docker/volumes-networks.md)
