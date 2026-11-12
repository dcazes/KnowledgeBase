---
type: Reference
title: LightRAG Snippets
description: LightRAG snippets — Python library insert and query with QueryParam modes, and server REST calls for document upload and querying.
resource: https://github.com/HKUDS/LightRAG
tags: [lightrag, snippets, python, api, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: lightrag-github
    resource: "https://github.com/HKUDS/LightRAG"
    title: "HKUDS/LightRAG on GitHub"
    author: "site:github.com"
---

# LightRAG — Snippets

## Python library

```python
import asyncio
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed

async def main():
    rag = LightRAG(working_dir="./rag_storage",
                   llm_model_func=gpt_4o_mini_complete,
                   embedding_func=openai_embed)
    await rag.initialize_storages()

    await rag.ainsert(open("book.txt").read())
    for mode in ["local", "global", "hybrid", "mix"]:
        print(mode, await rag.aquery("What are the main themes?", param=QueryParam(mode=mode)))

    await rag.finalize_storages()

asyncio.run(main())
```

Swap the model functions for the Ollama or generic OpenAI-compatible helpers in `lightrag.llm` to run locally.

## Server API

```bash
curl -X POST http://localhost:9621/documents/upload -F "file=@report.pdf"
curl -X POST http://localhost:9621/query -H "Content-Type: application/json" \
     -d '{"query": "Summarise the key risks", "mode": "mix"}'
```

Add `-H "X-API-Key: $LIGHTRAG_API_KEY"` when an API key is configured. Full schema at `http://localhost:9621/docs`.

## Related

[LightRAG index](index.md) · [Configuration](configuration.md)
