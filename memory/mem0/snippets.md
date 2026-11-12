---
type: Reference
title: Mem0 Snippets
description: Copy-paste Mem0 snippets for the 2026 API — add conversations, filtered search, list and delete memories, async usage, Node SDK, and the CLI.
resource: https://docs.mem0.ai
tags: [mem0, snippets, cheat-sheet, python, typescript]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: mem0-readme
    resource: "https://github.com/mem0ai/mem0"
    title: "Mem0 README — Basic Usage"
    author: "site:github.com"
  - id: mem0-migration-v3
    resource: "https://docs.mem0.ai/migration/oss-v2-to-v3"
    title: "Open Source: Migrating to the New Memory Algorithm"
    author: "site:docs.mem0.ai"
---

# Mem0 — Snippets

## Add and search (Python)

```python
from mem0 import Memory
m = Memory()

messages = [
    {"role": "user", "content": "I'm vegetarian and allergic to peanuts."},
    {"role": "assistant", "content": "Noted, I'll avoid those in recipes."},
]
m.add(messages, user_id="alice")                       # entity ids: top-level on add()

hits = m.search("dietary restrictions", filters={"user_id": "alice"}, top_k=5)
for h in hits["results"]:
    print(h["memory"], h.get("score"))
```

## Scope to an agent and a session

```python
m.add("Deploys go through the staging branch first.", agent_id="release-bot", run_id="2026-11-12")
m.search("deploy process", filters={"agent_id": "release-bot"})
```

## List and delete

```python
all_mem = m.get_all(filters={"user_id": "alice"})
m.delete(memory_id=all_mem["results"][0]["id"])
m.delete_all(user_id="alice")
```

## Async and context manager

```python
from mem0 import AsyncMemory

async with AsyncMemory() as m:
    await m.add("Uses Neovim", user_id="bob")
    print(await m.search("editor", filters={"user_id": "bob"}))
```

## Node.js

```ts
import { Memory } from "mem0ai/oss";

const memory = new Memory();
await memory.add("Prefers TypeScript over JavaScript", { userId: "alice" });
const res = await memory.search("language preference", { filters: { userId: "alice" }, topK: 5 });
```

## CLI

```bash
mem0 add "Works in UTC+1" --user-id alice
mem0 search "timezone" --user-id alice
```

## Related

[Mem0 index](index.md) · [Configuration](configuration.md) · [AI Integration](ai-integration.md)
