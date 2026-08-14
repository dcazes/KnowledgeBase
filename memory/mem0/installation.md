---
type: HowTo
title: Mem0 Installation
description: Install Mem0 — pip install mem0ai (v2.0.18) or local checkout v2.0.12; optional OpenMemory app via Docker on :3000; verify with a first add/search.
resource: https://docs.mem0.ai
tags: [mem0, installation, pip, openmemory, docker]
timestamp: 2026-08-13T00:00:00Z
---

# Installation

Two deployment modes: the **Python library** (typical) and the **OpenMemory app** (FastAPI + web UI).

## 1. Python library

```bash
pip install mem0ai          # latest (2.0.18 as of 2026-08-13)
# or use the local checkout:
cd programs/mem0 && pip install -e .
```

Verify:

```bash
python -c "import mem0; print(mem0.__version__)"   # 2.0.12 on local checkout
```

## 2. OpenMemory app (optional, self-hosted UI)

OpenMemory is a separate repo (`mem0ai/OpenMemory`). The local `programs/mem0` checkout does **not** include it. Run from the repo:

```bash
cd OpenMemory
docker compose up -d        # web UI on :3000, API + embedded Qdrant
```

## Status on this machine

* `programs/mem0` checkout present (v2.0.12) — **not deployed**, no containers, no venv (recon 2026-08-12).
* No `mem0` MCP/server config in the agent stack (unlike [Graphiti MCP](../graphiti/index.md)).

# Citations

[1] [Mem0 docs — quickstart](https://docs.mem0.ai/quickstart)
[2] [Mem0 on PyPI](https://pypi.org/project/mem0ai/)
[3] [OpenMemory repo](https://github.com/mem0ai/OpenMemory)
