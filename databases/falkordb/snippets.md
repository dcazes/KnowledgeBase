---
type: Reference
title: FalkorDB Snippets
description: FalkorDB snippets — connect with the Python client, create and query a graph with Cypher, and work with multiple graphs.
resource: https://github.com/FalkorDB/FalkorDB
tags: [falkordb, snippets, python, cypher, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: falkordb-github
    resource: "https://github.com/FalkorDB/FalkorDB"
    title: "FalkorDB/FalkorDB on GitHub"
    author: "site:github.com"
---

# FalkorDB — Snippets

```python
from falkordb import FalkorDB

db = FalkorDB(host="localhost", port=6379)
g = db.select_graph("alice_memory")               # one graph per user
g.query("""
  MERGE (a:Person {name: 'Alice'})-[:LIKES]->(:Topic {name: 'GraphRAG'})
""")
res = g.query("MATCH (p:Person)-[:LIKES]->(t:Topic) RETURN p.name, t.name")
for row in res.result_set:
    print(row)
print(db.list_graphs())
```

## Related

[FalkorDB index](index.md) · [AI Integration](ai-integration.md)
