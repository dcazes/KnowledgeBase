---
type: Playbook
title: Neo4j Installation
description: Run Neo4j with Docker (with APOC and GDS plugins), Neo4j Desktop, or the managed AuraDB, and connect with the Browser and drivers.
resource: https://neo4j.com/docs/operations-manual/current/docker/
tags: [neo4j, installation, docker]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: neo4j-docs
    resource: "https://neo4j.com/docs/"
    title: "Neo4j documentation"
    author: "site:neo4j.com"
---

# Neo4j — Installation

```bash
docker run -d --name neo4j -p 127.0.0.1:7474:7474 -p 127.0.0.1:7687:7687 \
  -v neo4j_data:/data -e NEO4J_AUTH=neo4j/change-me-please \
  -e NEO4J_PLUGINS='["apoc", "graph-data-science"]' \
  neo4j:latest
pip install neo4j
```

Open the Browser at `http://localhost:7474`. Neo4j Desktop bundles local DBMSs and plugins; AuraDB Free is a hosted option. [Graphiti](../../memory/graphiti/backends.md) documents its minimum supported version.

## Related

[Neo4j index](index.md) · [Snippets](snippets.md)
