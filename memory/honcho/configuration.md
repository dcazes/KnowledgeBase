---
type: HowTo
title: Honcho Configuration
description: Configure Honcho — config.toml sections (app/db/auth/llm/embedding), API keys, base_url for SDK, workspace/peer/session scoping metadata.
resource: https://docs.honcho.dev
tags: [honcho, configuration, config.toml, workspace]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: honcho-docs-configuration
    resource: "https://docs.honcho.dev"
    title: "Honcho docs — configuration"
    author: "site:docs.honcho.dev"
  - id: honcho-github
    resource: "https://github.com/plastic-labs/honcho"
    title: "Honcho GitHub"
    author: "site:github.com"
---

# Honcho — Configuration

## config.toml (server)

Honcho v3 configures the server via `config.toml` (copy `config.toml.example`, or use env vars which override it). Key sections (verified from the checkout, 2026-08-13):

```toml
[app]
LOG_LEVEL = "INFO"
NAMESPACE = "honcho"

[db]
CONNECTION_URI = "postgresql+psycopg://postgres:postgres@localhost:5432/postgres"

[auth]
USE_AUTH = false
# JWT_SECRET = "..."   # required if USE_AUTH = true

[llm]
OPENAI_API_KEY = "your-api-key-here"     # or ANTHROPIC_API_KEY / GEMINI_API_KEY
DEFAULT_MAX_TOKENS = 2500

[embedding]
VECTOR_DIMENSIONS = 1536
```

* LLM providers supported: **openai, anthropic, gemini** (defaults: text gen `openai/gpt-5.4-mini`, embeddings `openai/text-embedding-3-small`).
* The server uses the LLM to derive conclusions; the SDK is a thin client.

## SDK client

```python
from honcho import Honcho

client = Honcho(
    base_url="http://localhost:8000",
    # api_key if the server requires auth (USE_AUTH=true)
)
```

## Scoping

* **Workspace** — top-level tenant; isolates deployments (multi-tenant by design).
* **Peer** — a user or agent; `client.peer("id")` with optional metadata.
* **Session** — conversation thread; `client.session("id")`; `session.add_peers([...])`; messages carry metadata (`peer.message("text", metadata={...})`) which feeds the model's context.

## Conclusion configuration

Derived conclusions are queryable via `honcho conclusion list` / `search` (CLI) or the SDK; the deriver queue state via `honcho workspace queue-status`.
