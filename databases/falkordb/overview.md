---
type: Concept
title: FalkorDB Overview
description: How FalkorDB works — sparse adjacency matrices with GraphBLAS, openCypher support, many isolated graphs per instance for multi-tenancy, vector and full-text indexes, and the trade-offs of SSPL licensing.
resource: https://docs.falkordb.com
tags: [falkordb, overview, graphblas, multi-tenant]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: falkordb-docs
    resource: "https://docs.falkordb.com"
    title: "FalkorDB documentation"
    author: "site:docs.falkordb.com"
---

# FalkorDB — Overview

* **Linear-algebra engine:** relationships are stored as sparse matrices; traversals become matrix multiplications, which GraphBLAS executes efficiently.
* **openCypher** queries, property graph model.
* **Many graphs per instance:** each tenant or user can have its own graph key — convenient for per-user [agent memory](../../concepts/agent-memory.md).
* **Vector and full-text indexes** for hybrid graph + semantic retrieval.
* **Redis protocol:** use Redis tooling, persistence (RDB/AOF) and replication.
* **Licence:** SSPLv1 restricts offering FalkorDB itself as a managed service; fine for internal use.

## Related

[FalkorDB index](index.md) · [Neo4j overview](../neo4j/overview.md)
