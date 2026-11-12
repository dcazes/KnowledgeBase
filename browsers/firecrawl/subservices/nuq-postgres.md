---
type: Reference
title: Firecrawl NuQ PostgreSQL
description: NuQ, Firecrawl's PostgreSQL-backed job queue — the default durable queue for scrape and crawl jobs, persistence and backups.
resource: https://github.com/firecrawl/firecrawl
tags: [firecrawl, postgres, queue, subservice]
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

# Firecrawl — NuQ PostgreSQL

**NuQ** is Firecrawl's job queue implemented on PostgreSQL. API calls enqueue scrape and crawl jobs; workers claim and complete them. Because the queue is durable, jobs survive worker restarts. Put its data on a named volume and back it up if crawl history matters. For very high volumes the queue can switch to [FoundationDB](foundationdb.md) (`NUQ_BACKEND=fdb`).

## Related

[Subservices](index.md) · [pgvector](../../../databases/pgvector/index.md) (Postgres for vectors, a different use)
