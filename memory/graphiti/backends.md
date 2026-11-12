---
type: Reference
title: Graphiti Backends
description: Graph databases supported by Graphiti — Neo4j, FalkorDB (including embedded FalkorDBLite), Amazon Neptune with OpenSearch, and the deprecated Kuzu driver.
resource: https://github.com/getzep/graphiti
tags: [graphiti, neo4j, falkordb, neptune, kuzu, graph-database]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphiti-github
    resource: "https://github.com/getzep/graphiti"
    title: "getzep/graphiti on GitHub"
    author: "site:github.com"
  - id: neo4j-docs
    resource: "https://neo4j.com/docs/"
    title: "Neo4j documentation"
    author: "site:neo4j.com"
  - id: falkordb-docs
    resource: "https://docs.falkordb.com"
    title: "FalkorDB documentation"
    author: "site:docs.falkordb.com"
---

# Graphiti — Backends

| Backend | Install extra | Notes |
|---|---|---|
| [Neo4j](../../databases/neo4j/index.md) 5.26+ | (default) | Most mature driver; Neo4j Desktop or the `neo4j` Docker image |
| [FalkorDB](../../databases/falkordb/index.md) | `graphiti-core[falkordb]` | Redis-protocol graph DB; default backend of the MCP server |
| FalkorDBLite | `graphiti-core[falkordblite]` | Embedded FalkorDB, Python 3.12+, no server needed |
| Amazon Neptune | `graphiti-core[neptune]` | Neptune Database or Neptune Analytics plus OpenSearch Serverless for full-text search |
| Kuzu | `graphiti-core[kuzu]` | **Deprecated**: upstream Kuzu is unmaintained; emits a `DeprecationWarning` |

## Choosing

* **Neo4j** — best tooling (Browser, Bloom, Cypher ecosystem) and the most tested path.
* **FalkorDB** — lightweight, fast, one container; a good default for local development and the MCP server.
* **Neptune** — when you are already on AWS and want a managed service.
* Avoid **Kuzu** for new projects.

## Quick start containers

```bash
docker run -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password neo4j:5.26
docker run -p 6379:6379 -p 3000:3000 -it --rm falkordb/falkordb:latest
```

The repo's own `docker compose up` starts Neo4j; `docker compose --profile falkordb up` starts FalkorDB.

## Related

[Graphiti index](index.md) · [Installation](installation.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md) · [Neo4j](../../databases/neo4j/index.md) · [FalkorDB](../../databases/falkordb/index.md)
