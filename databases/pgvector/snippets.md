---
type: Reference
title: pgvector Snippets
description: pgvector SQL snippets — table with embeddings, HNSW index, nearest-neighbour and filtered queries, iterative scans, and hybrid search with full-text ranking fused by RRF.
resource: https://github.com/pgvector/pgvector
tags: [pgvector, snippets, sql, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pgvector-github
    resource: "https://github.com/pgvector/pgvector"
    title: "pgvector/pgvector on GitHub"
    author: "site:github.com"
---

# pgvector — Snippets

```sql
CREATE TABLE chunks (
  id bigserial PRIMARY KEY,
  doc_id text, lang text, content text,
  embedding vector(768),
  tsv tsvector GENERATED ALWAYS AS (to_tsvector('english', content)) STORED
);
CREATE INDEX ON chunks USING hnsw (embedding vector_cosine_ops);
CREATE INDEX ON chunks USING gin (tsv);

-- nearest neighbours
SELECT id, content FROM chunks ORDER BY embedding <=> $1 LIMIT 5;

-- filtered, with iterative scans so enough rows come back
SET hnsw.iterative_scan = relaxed_order;
SELECT id FROM chunks WHERE lang = 'en' ORDER BY embedding <=> $1 LIMIT 5;

-- hybrid: reciprocal rank fusion of vector and keyword results
WITH v AS (SELECT id, row_number() OVER (ORDER BY embedding <=> $1) r FROM chunks ORDER BY embedding <=> $1 LIMIT 20),
     k AS (SELECT id, row_number() OVER (ORDER BY ts_rank(tsv, q) DESC) r
           FROM chunks, plainto_tsquery('english', $2) q WHERE tsv @@ q LIMIT 20)
SELECT id, sum(1.0 / (60 + r)) AS score FROM (SELECT * FROM v UNION ALL SELECT * FROM k) s
GROUP BY id ORDER BY score DESC LIMIT 5;
```

## Related

[pgvector index](index.md) · [Overview](overview.md)
