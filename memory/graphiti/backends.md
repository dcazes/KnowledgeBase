---
type: Reference
title: Graphiti — Backends
description: Graphiti's pluggable graph backends — Neo4j, FalkorDB, Amazon Neptune, and deprecated Kuzu — and their install extras.
resource: https://github.com/getzep/graphiti#installation
tags: [graphiti, backend, neo4j, falkordb, neptune, kuzu, driver]
generated: { by: "human:daniel", at: "2026-07-09T05:03:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T05:03:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: installation-backends-readme
    resource: "https://github.com/getzep/graphiti#installation"
    title: "Installation / backends (README)"
    author: "site:github.com"
  - id: neo4j
    resource: "https://neo4j.com/"
    title: "Neo4j"
    author: "site:neo4j.com"
  - id: falkordb
    resource: "https://falkordb.com/"
    title: "FalkorDB"
    author: "site:falkordb.com"
---

# Supported backends

Graphiti uses a pluggable driver layer. Requirements (from README):

| Backend | Version | Notes |
|---------|---------|-------|
| **Neo4j** | 5.26 | Default; Docker or Neo4j Desktop |
| **FalkorDB** | 1.1.2 | `pip install graphiti-core[falkordb]`; embedded `falkordblite` (Py 3.12+) |
| **Amazon Neptune** | Database Cluster or Neptune Analytics + OpenSearch | `pip install graphiti-core[neptune]` |
| **Kuzu** | 0.11.2 | **Deprecated** — upstream unmaintained; emits DeprecationWarning |

# Neo4j (recommended)

```bash
docker run -d --name neo4j -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/<STRONG_PASSWORD> neo4j:5.26
```
Database name defaults to `neo4j` (hardcoded in `Neo4jDriver`); as of v0.17.0 you can pass a custom driver:
```python
from graphiti_core.driver.neo4j_driver import Neo4jDriver
driver = Neo4jDriver(user="neo4j", password="...", db="my_db", uri="bolt://localhost:7687")
```

# FalkorDB

```bash
pip install graphiti-core[falkordb]
docker run -p 6379:6379 -p 3000:3000 -it --rm falkordb/falkordb:latest
```

# Kuzu (avoid for new projects)

Deprecated; use Neo4j/FalkorDB instead.

# Tips

* Neo4j is the most battle-tested for Graphiti.
* Neptune only makes sense if you're already on AWS.
* Match the install extra to your backend or the driver won't load.
