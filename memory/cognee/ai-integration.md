---
type: Concept
title: Cognee AI Integration
description: Use Cognee as AI memory — Python API (add/cognify/search), REST API + frontend, agent wiring, semantic vs graph-completion search, vs LightRAG/Graphiti.
resource: https://docs.cognee.ai
tags: [cognee, integration, api, agents, memory]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: cognee-docs-quickstart
    resource: "https://docs.cognee.ai"
    title: "Cognee docs — quickstart"
    author: "site:docs.cognee.ai"
  - id: cognee-github
    resource: "https://github.com/topoteretes/cognee"
    title: "Cognee GitHub"
    author: "site:github.com"
---

# AI Integration

## Python API

```python
import asyncio
import cognee
from cognee.shared.data_models import KnowledgeGraph
from cognee.infrastructure.databases.vector.embeddings import SEARCH_TYPE

async def main():
    await cognee.add("notes.md", dataset_name="kb")
    await cognee.cognify(dataset_name="kb")                    # run ECL pipeline

    # semantic (embedding) search
    r1 = await cognee.search("What themes are in the notes?", dataset_name="kb",
                             query_type=SEARCH_TYPE.SEMANTIC)
    # graph-completion search (traverses relations)
    r2 = await cognee.search("How do concepts relate?", dataset_name="kb",
                             query_type=SEARCH_TYPE.GRAPH_COMPLETION)
    print(r1, r2)

asyncio.run(main())
```

## REST API + frontend

The Docker deployment exposes a cognee API; the bundled `cognee-frontend` provides a web UI to upload data, run the pipeline, and search the graph.

## Agent wiring

* Use Cognee as a **grounded memory tool** for Hermes/OpenCode: an agent calls `add` + `cognify` on ingested documents, then `search` with graph completion for fact-aware answers.
* Division of labor: Cognee = corpus knowledge engineering; [Graphiti](../graphiti/index.md) = temporal agent memory; [Mem0](../mem0/index.md)/[MemOS](../memos/index.md) = per-user memory. LightRAG = lighter-weight graph RAG alternative.
