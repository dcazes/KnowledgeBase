---
type: Reference
title: Neo4j Snippets
description: Neo4j snippets — Cypher to create and query a small knowledge graph, a vector index with similarity search, a combined vector-plus-graph query, and the Python driver.
resource: https://neo4j.com/docs/cypher-manual/current/
tags: [neo4j, snippets, cypher, python, cheat-sheet]
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

# Neo4j — Snippets

```cypher
MERGE (a:Person {name: 'Alice'})
MERGE (c:Company {name: 'Acme'})
MERGE (a)-[:WORKS_AT {since: 2024}]->(c);

MATCH (p:Person)-[:WORKS_AT]->(c:Company) RETURN p.name, c.name;

CREATE VECTOR INDEX chunk_embeddings IF NOT EXISTS
FOR (ch:Chunk) ON ch.embedding
OPTIONS {indexConfig: {`vector.dimensions`: 768, `vector.similarity_function`: 'cosine'}};

// vector search, then expand through the graph (GraphRAG-style)
CALL db.index.vector.queryNodes('chunk_embeddings', 5, $query_embedding) YIELD node, score
MATCH (node)-[:MENTIONS]->(e:Entity)-[r]-(related)
RETURN node.text, score, e.name, type(r), related.name LIMIT 25;
```

```python
from neo4j import GraphDatabase
with GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "change-me-please")) as d:
    rows, _, _ = d.execute_query("MATCH (p:Person) RETURN p.name AS name")
    print([r["name"] for r in rows])
```

## Related

[Neo4j index](index.md) · [AI Integration](ai-integration.md)
