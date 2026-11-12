---
type: Concept
title: Neo4j Overview
description: Neo4j concepts — labelled property graph model, Cypher pattern matching, GQL, constraints and indexes including vector and full-text, Graph Data Science algorithms (community detection, centrality, similarity), and editions.
resource: https://neo4j.com/docs/
tags: [neo4j, overview, cypher, gds]
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

# Neo4j — Overview

* **Property graph:** nodes with labels (`:Person`), relationships with types (`-[:WORKS_AT]->`), both with properties.
* **Cypher:** declarative pattern matching — `MATCH (p:Person)-[:WORKS_AT]->(c:Company {name: 'Acme'}) RETURN p`. Neo4j also implements the ISO **GQL** standard.
* **Indexes:** range, text, full-text (Lucene) and **vector** indexes (HNSW) for semantic search on node or relationship embeddings.
* **Graph Data Science:** Leiden/Louvain communities, PageRank, node similarity, embeddings (FastRP, node2vec) — the same community detection [Microsoft GraphRAG](../../memory/graphrag/overview.md) relies on.
* **Editions:** Community (single instance), Enterprise (clustering, RBAC), AuraDB (managed).

## Related

[Neo4j index](index.md) · [Snippets](snippets.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md)
