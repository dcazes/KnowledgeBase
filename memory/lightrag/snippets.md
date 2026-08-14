---
type: CheatSheet
title: LightRAG Snippets
description: LightRAG cheat sheet — install, library insert/query, hybrid/local/global modes, REST calls, incremental updates, storage env.
resource: https://lightrag.readthedocs.io/en/latest/
tags: [lightrag, snippets, cheat-sheet, rag]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: lightrag-docs-examples
    resource: "https://lightrag.readthedocs.io/en/latest/"
    title: "LightRAG docs — examples"
    author: "site:lightrag.readthedocs.io"
  - id: lightrag-github
    resource: "https://github.com/HKUDS/LightRAG"
    title: "LightRAG GitHub"
    author: "site:github.com"
---

# LightRAG — Snippets

## Install

```bash
pip install lightrag-hku        # 1.5.6 latest; local checkout 1.5.5
```

## Library: insert + query

```python
import asyncio
from lightrag import LightRAG, QueryParam

async def main():
    rag = LightRAG(working_dir="./rag_storage")     # needs LLM binding configured
    await rag.ainsert(open("docs.md").read())
    r = await rag.aquery("Summary of key themes?", param=QueryParam(mode="hybrid"))
    print(r)

asyncio.run(main())
```

## Query modes

```python
QueryParam(mode="naive")    # keyword/vector only
QueryParam(mode="local")    # low-level (graph traversal, precise facts)
QueryParam(mode="global")   # high-level (themes via graph)
QueryParam(mode="hybrid")   # both (default)
```

## Incremental insert (no rebuild)

```python
await rag.ainsert("New document text…")
await rag.ainsert(["Doc A…", "Doc B…"], split_by_character=True)
```

## Server (Docker)

```bash
docker compose up -d            # API :9621
curl -X POST http://localhost:9621/documents/text -H "Content-Type: application/json" \
  -d '{"text":"content here"}'
curl -X POST http://localhost:9621/query -H "Content-Type: application/json" \
  -d '{"query":"question","mode":"hybrid"}'
curl http://localhost:9621/documents  # list indexed docs
```

## Ollama-local env

```bash
export LLM_BINDING=ollama LLM_MODEL=llama3.1 OLLAMA_HOST=http://localhost:11434
export EMBEDDING_BINDING=ollama EMBEDDING_MODEL=nomic-embed-text
```
