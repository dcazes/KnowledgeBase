---
type: Reference
title: Firecrawl RabbitMQ
description: RabbitMQ in a self-hosted Firecrawl stack — message broker for job events between components.
resource: https://github.com/firecrawl/firecrawl
tags: [firecrawl, rabbitmq, subservice]
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

# Firecrawl — RabbitMQ

RabbitMQ carries messages between Firecrawl components (job events and notifications) so the API and workers stay decoupled. It needs no tuning for small deployments; monitor queue depth if jobs back up. Keep its management UI private.

## Related

[Subservices](index.md) · [NuQ PostgreSQL](nuq-postgres.md)
