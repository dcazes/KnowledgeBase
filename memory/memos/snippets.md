---
type: Playbook
title: MemOS — Snippets & Cheat Sheet
description: Copy-paste commands for MemOS — install (pip install MemoryOS), serve (uvicorn :8000), Docker stack, REST API calls, and Python MOS usage.
resource: https://memos-docs.openmem.net/home/overview/
tags: [memos, snippets, cheat-sheet, api, deploy, python]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: memos-repo
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemOS repo"
    author: "site:github.com"
  - id: pypi-memoryos
    resource: "https://pypi.org/project/MemoryOS/"
    title: "PyPI — MemoryOS"
    author: "site:pypi.org"
---

# Install / serve

> As of 2026-08-12 there is **no local checkout** at `programs/memos` — install from PyPI (`MemoryOS`, import `memos`). With a repo clone present, `make install`/`make serve` work identically from the checkout root.

```bash
pip install MemoryOS        # distribution name; import name is memos
uvicorn memos.api.server_api:app --host 0.0.0.0 --port 8000 --workers 1
```

# Docker stack (API + Neo4j + Qdrant)

```bash
# requires a clone of the MemOS repo (not present locally as of 2026-08-12):
git clone https://github.com/MemTensor/MemOS.git programs/memos
cd programs/memos
docker compose -f docker/docker-compose.yml up -d
docker compose -f docker/docker-compose.yml ps
docker compose -f docker/docker-compose.yml down
```

# Verify it is up

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8000/health
```

# REST API (port 8000)

```bash
# base path is /product
curl -X POST http://localhost:8000/product/add \
  -H 'Content-Type: application/json' \
  -d '{"user_id":"u1","messages":[{"role":"user","content":"I prefer concise answers."}]}'

curl -X POST http://localhost:8000/product/search \
  -H 'Content-Type: application/json' \
  -d '{"user_id":"u1","query":"what are my preferences?"}'
```

# Python — MOS

```python
from memos import MOS, GeneralMemCube, MOSConfig

mos = MOS.simple()                       # auto-configure from env
cube = GeneralMemCube(...)              # build a memory cube
mos.register_mem_cube(cube)
mos.add(user_id="u1", messages=[{"role":"user","content":"..."}])
results = mos.search(user_id="u1", query="...")
print(results)
```

# MCP server (for Hermes / OpenCode / Cursor)

```text
# Register the MemOS MCP server in your client's mcpServers config.
# Entry: memos.api MCP server (src/memos/api/). Transport: stdio/SSE per client.
```

# Other commands

```bash
make openapi            # regenerate docs/openapi.json
make test               # full test suite
make format             # ruff lint + format
poetry run pytest tests/<module>/ -q   # single module
```
