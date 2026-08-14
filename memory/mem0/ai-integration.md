---
type: Concept
title: Mem0 AI Integration
description: Use Mem0 as agent memory — Python/JS SDKs, OpenMemory REST API, wiring into Hermes/OpenCode, and how it compares to MemOS for this stack.
resource: https://docs.mem0.ai
tags: [mem0, integration, sdk, api, agents, hermes]
timestamp: 2026-08-13T00:00:00Z
---

# AI Integration

## Python SDK (primary)

```python
from mem0 import Memory

m = Memory.from_config()          # reads config.json
m.add("I like dark-roast coffee", user_id="alice")
results = m.search("What coffee does alice like?", user_id="alice")
m.get_all(user_id="alice")
m.update(memory_id="...", data="I like light-roast coffee", user_id="alice")
m.delete(memory_id="...", user_id="alice")
```

## JS SDK

```js
import { Memory } from "@mem0/node";
const memory = new Memory({});    // reads config.json
await memory.add("I like dark-roast coffee", { user_id: "alice" });
const res = await memory.search("coffee preference", { user_id: "alice" });
```

## OpenMemory REST API

```bash
# OpenMemory app on :3000 (docker compose up from the OpenMemory repo)
curl -X POST http://localhost:3000/api/memories \
  -H "Authorization: Bearer <key>" -H "Content-Type: application/json" \
  -d '{"text": "I like dark-roast coffee", "user_id": "alice"}'
curl "http://localhost:3000/api/memories/search?query=coffee&user_id=alice" \
  -H "Authorization: Bearer <key>"
```

## In this stack

* No active Mem0 deployment on this machine (local checkout only, 2026-08-13).
* If wired up, the natural pattern is Ollama LLM + embedded Qdrant + scoped `user_id` per agent — no cloud keys.
* Competes with [MemOS](../memos/index.md) (the deployed-via-pip option) and [Graphiti](../graphiti/index.md) (temporal graph MCP). Mem0 = pragmatic per-user memory; MemOS = full memory-OS with scheduling; Graphiti = temporal facts with provenance. See the [memory comparison](../../meta/architecture/memory/memory-comparison.md).

# Citations

[1] [Mem0 docs — quickstart](https://docs.mem0.ai/quickstart)
[2] [Mem0 GitHub](https://github.com/mem0ai/mem0)
