---
type: CheatSheet
title: Mem0 Snippets
description: Mem0 cheat sheet — pip install, Memory.from_config, add/search/get/update/delete, scoped queries, OpenMemory HTTP calls, Docker.
resource: https://docs.mem0.ai
tags: [mem0, snippets, cheat-sheet, memory, api]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: mem0-docs-quickstart
    resource: "https://docs.mem0.ai/quickstart"
    title: "Mem0 docs — quickstart"
    author: "site:docs.mem0.ai"
  - id: mem0-github
    resource: "https://github.com/mem0ai/mem0"
    title: "Mem0 GitHub"
    author: "site:github.com"
---

# Mem0 — Snippets

## Install

```bash
pip install mem0ai                    # latest (2.0.18)
python -c "import mem0; print(mem0.__version__)"   # 2.0.12 on local checkout
```

## Basic memory loop

```python
from mem0 import Memory
m = Memory.from_config()

m.add("The sky is blue", user_id="alice")
r = m.search("what color is the sky", user_id="alice")
print(r)                              # [{memory: "The sky is blue", ...}]
```

## CRUD

```python
mid = m.get_all(user_id="alice")[0]["id"]
m.update(memory_id=mid, data="The sky is cyan today", user_id="alice")
m.delete(memory_id=mid, user_id="alice")
```

## Scoped search + filters

```python
m.search("project context", user_id="alice", agent_id="planner")
m.search("anything", metadata_filter={"team": "infra"})   # requires stored metadata
```

## Ollama-local config (no cloud)

```python
from mem0 import Memory
m = Memory.from_config({"llm": {"provider": "ollama", "config": {"model": "llama3.1"}},
                        "embedder": {"provider": "ollama", "config": {"model": "nomic-embed-text"}},
                        "vector_store": {"provider": "qdrant", "config": {"on_disk": True}}})
```

## OpenMemory REST

```bash
curl -X POST http://localhost:3000/api/memories -H "Authorization: Bearer $MEM0_API_KEY" \
  -H "Content-Type: application/json" -d '{"text":"remember this","user_id":"alice"}'
curl "http://localhost:3000/api/memories/search?query=this&user_id=alice" -H "Authorization: Bearer $MEM0_API_KEY"
```

## Docker (OpenMemory app)

```bash
git clone https://github.com/mem0ai/OpenMemory && cd OpenMemory
docker compose up -d        # UI :3000
```
