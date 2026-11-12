---
type: Reference
title: MemOS Snippets
description: MemOS REST snippets — add and search memories on MemOS Cloud, and create a memory cube, add and search on a self-hosted server.
resource: https://github.com/MemTensor/MemOS
tags: [memos, snippets, rest, python, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: memos-github
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemTensor/MemOS on GitHub"
    author: "site:github.com"
---

# MemOS — Snippets

## Cloud API

```python
import requests
base = "https://memos.memtensor.cn/api/openmem/v1"
headers = {"Authorization": "Token mpg-...", "Content-Type": "application/json"}

requests.post(f"{base}/add/message", headers=headers, json={
    "user_id": "alice", "conversation_id": "conv_001",
    "messages": [{"role": "user", "content": "I like strawberry"}],
})
print(requests.post(f"{base}/search/memory", headers=headers,
                    json={"query": "What do I like?", "user_id": "alice"}).json())
```

## Self-hosted: cubes

```python
import requests, json
base = "http://localhost:8000/product"
h = {"Content-Type": "application/json"}

requests.post(f"{base}/create_cube", headers=h, data=json.dumps(
    {"cube_name": "Alice's memory", "owner_id": "alice", "cube_id": "alice_cube"}))
requests.post(f"{base}/add", headers=h, data=json.dumps(
    {"user_id": "alice", "writable_cube_ids": ["alice_cube"],
     "messages": [{"role": "user", "content": "I like strawberry"}]}))
```

Search the cube through the corresponding search endpoint (see the API docs served by your instance).

## Related

[MemOS index](index.md) · [Installation](installation.md)
