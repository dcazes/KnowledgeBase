---
type: Reference
title: Firecrawl FoundationDB
description: Optional FoundationDB queue backend for Firecrawl — when to use it instead of NuQ PostgreSQL and the operational cost.
resource: https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md
tags: [firecrawl, foundationdb, queue, subservice]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: firecrawl-selfhost
    resource: "https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md"
    title: "Self-hosting Firecrawl"
    author: "site:github.com"
  - id: fdb
    resource: "https://www.foundationdb.org"
    title: "FoundationDB"
    author: "site:foundationdb.org"
---

# Firecrawl — FoundationDB

FoundationDB is an optional, distributed, transactional key-value store that Firecrawl can use as its queue backend (`NUQ_BACKEND=fdb`) for large deployments. The self-hosting guide recommends staying on [NuQ PostgreSQL](nuq-postgres.md) unless you are prepared to operate FoundationDB — it is powerful but adds real operational complexity.

## Related

[Subservices](index.md) · [Self-hosting](../self-hosting.md)
