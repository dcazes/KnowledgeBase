---
type: HowTo
title: Honcho Installation
description: Install Honcho — pip install honcho-ai (v2.3.0 SDK) or local checkout v3.0.11; run the server (Docker / fastapi run src/main.py); verify with a peer/session call.
resource: https://docs.honcho.dev
tags: [honcho, installation, pip, server]
timestamp: 2026-08-13T00:00:00Z
---

# Installation

## 1. SDK (Python)

```bash
pip install honcho-ai           # SDK 2.3.0 as of 2026-08-13
# or from the checkout:
cd programs/honcho && pip install -e .    # checkout SDK pyproject shows 2.2.0
```

## 2. Server

The Honcho server requires an LLM provider key (OpenAI/Anthropic/Gemini, set in `config.toml`) and is run separately from the SDK. Typical paths:

```bash
# Docker (from the repo): runs API + workers
cd programs/honcho && docker compose up -d

# or run the FastAPI app directly (repo layout: src/main.py)
cd programs/honcho && fastapi run --host 0.0.0.0 --port 8000 src/main.py
```

The server listens on `:8000` (compose maps `127.0.0.1:8000:8000`).

## Verify

```python
from honcho import Honcho

client = Honcho(base_url="http://localhost:8000")
alice = client.peer("alice")
session = client.session("verify")
session.add_peers([alice])
print(session)                  # session echoed back
```

## Status on this machine

* `programs/honcho` checkout present (v3.0.11) — **not deployed**, no containers (recon 2026-08-12).

# Citations

[1] [Honcho docs — quickstart](https://docs.honcho.dev)
[2] [honcho-ai on PyPI](https://pypi.org/project/honcho-ai/)
