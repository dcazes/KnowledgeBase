---
type: Comparison
title: Databases Alternatives
description: Comparison of vector and graph databases for AI — Qdrant, pgvector, Neo4j and FalkorDB — plus other common choices, with guidance on when to use a vector store, a graph store, or both.
resource: https://github.com/topics/vector-database
tags: [databases, comparison, vector-database, graph-database]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: qdrant
    resource: "https://github.com/qdrant/qdrant"
    title: "Qdrant"
    author: "site:github.com"
  - id: pgvector
    resource: "https://github.com/pgvector/pgvector"
    title: "pgvector"
    author: "site:github.com"
  - id: neo4j
    resource: "https://neo4j.com"
    title: "Neo4j"
    author: "site:neo4j.com"
  - id: falkordb
    resource: "https://github.com/FalkorDB/FalkorDB"
    title: "FalkorDB"
    author: "site:github.com"
---

# Databases Alternatives

| | [Qdrant](qdrant/index.md) | [pgvector](pgvector/index.md) | [Neo4j](neo4j/index.md) | [FalkorDB](falkordb/index.md) |
|---|---|---|---|---|
| Kind | Vector DB | Vector extension for Postgres | Graph DB (+ vectors) | Graph DB (+ vectors) |
| Query | REST/gRPC, Query API | SQL | Cypher / GQL | openCypher (Redis protocol) |
| Licence | Apache-2.0 | PostgreSQL | GPL-3.0 CE / commercial | SSPLv1 |
| Strength | Filtered + hybrid + multivector search at scale | One database for app data and vectors | Mature graph tooling, GDS algorithms | Very low latency, multi-graph |
| Typical AI use | RAG, memory vectors | RAG in existing Postgres apps | GraphRAG, temporal memory | Graph memory, Graphiti MCP |

Other vector stores: Milvus, Weaviate, Chroma, LanceDB (embedded), Pinecone, Elasticsearch/OpenSearch, Turbopuffer. Other graph stores: Memgraph, Kuzu (archived), Amazon Neptune, ArangoDB.

## Vector, graph or both?

* **Vector only** — semantic similarity over chunks or facts is enough ([RAG](../concepts/rag.md), [Mem0](../memory/mem0/index.md)).
* **Graph only** — relationships and multi-hop questions matter more than fuzzy matching.
* **Both** — most [GraphRAG](../concepts/graphrag.md) systems: vectors to find entry points, graph to expand context. Neo4j and FalkorDB can hold both; or pair Qdrant/pgvector with a graph store.

## Related

[Vector databases](../concepts/vector-databases.md) · [Knowledge graphs](../concepts/knowledge-graphs.md) · [Memory alternatives](../memory/alternatives.md)
