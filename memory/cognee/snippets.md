---
type: CheatSheet
title: Cognee Snippets
description: Cognee cheat sheet — install, add data, cognify, semantic vs graph-completion search, prune/reset, docker.
resource: https://docs.cognee.ai
tags: [cognee, snippets, cheat-sheet]
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

# Cognee — Snippets

## Install

```bash
pip install cognee            # 1.4.2 latest; local checkout 1.4.0
```

## Ingest → cognify → search

```python
import asyncio, cognee
from cognee.infrastructure.databases.vector.embeddings import SEARCH_TYPE

async def main():
    await cognee.add("report.pdf", dataset_name="research")     # files, URLs, code, dirs
    await cognee.cognify(dataset_name="research")               # ECL pipeline

    sem = await cognee.search("key findings", dataset_name="research",
                              query_type=SEARCH_TYPE.SEMANTIC)
    graph = await cognee.search("how findings connect", dataset_name="research",
                                query_type=SEARCH_TYPE.GRAPH_COMPLETION)
    print(sem, graph)

asyncio.run(main())
```

## Add from URL / code / directory

```python
await cognee.add("https://example.com/page", dataset_name="web")
await cognee.add("~/projects/myrepo", dataset_name="code")
await cognee.add(["a.txt", "b.txt"], dataset_name="docs")
```

## Manage

```python
await cognee.prune()                    # wipe graph + data
await cognee.reset()                    # full reset (delete data dir)
# list datasets
await cognee.data_points.list_datasets()
```

## Docker

```bash
cd programs/cognee && docker compose up -d   # API + Postgres + vector store
```
