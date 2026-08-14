---
type: HowTo
title: PydanticAI Installation
description: Install PydanticAI — uv add pydantic-ai / pip install; version v2.29.0, Python 3.10+, pin pydantic>=2.12; verify with a minimal agent.
resource: https://pydantic.dev/docs/ai/overview/install/
tags: [pydantic, ai, installation, pip, uv]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: pydanticai-install-guide
    resource: "https://pydantic.dev/docs/ai/overview/install/"
    title: "PydanticAI install guide"
    author: "site:pydantic.dev"
  - id: pydanticai-on-pypi
    resource: "https://pypi.org/project/pydantic-ai/"
    title: "PydanticAI on PyPI"
    author: "site:pypi.org"
  - id: pydanticai-github
    resource: "https://github.com/pydantic/pydantic-ai"
    title: "PydanticAI GitHub"
    author: "site:github.com"
---

# Installation

## Install

```bash
uv add pydantic-ai        # uv projects
# or
pip install "pydantic-ai>=2.29.0"
```

Python **3.10+** required. Model extras are optional per provider (e.g. `pydantic-ai[openai]`, `pydantic-ai[anthropic]`).

## Version & security pin

* **Current: v2.29.0** (released 2026-08-13; requires Python 3.10+).
* **Security (2026-08-13 verified):** v2.28.0 patches **GHSA-h4xc-3qfq-jf93** (High — web chat UI CSRF/origin validation; no CVE assigned) for both `pydantic-ai` and `pydantic-ai-slim`; other High advisories (SSRF GHSA-2jrp-274c-jhv3, stored XSS GHSA-wjp5-868j-wqv7) are patched in earlier 2.x — keep `pydantic-ai` current.
* Requires `pydantic>=2.12`. If your system pydantic is older (this machine: **2.9.0** system python), install/upgrade in a venv first — see [Pydantic installation](../../tools/pydantic/installation.md).

## Verify

```bash
uv run python -c "import pydantic_ai; print(pydantic_ai.__version__)"
```

```python
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o-mini", instructions="Say hello.")
print(agent.run_sync("hi").output)
```

## Status here

No dedicated checkout in `programs/` — PydanticAI is a library used from the `pydantic` program context (`programs/pydantic/.venv`, pydantic 2.13.4). Not a running service.
