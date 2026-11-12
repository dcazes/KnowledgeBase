---
type: Reference
title: Open WebUI API
description: Using Open WebUI programmatically — per-user API keys, the OpenAI-compatible chat completions endpoint across all connected models, file upload and knowledge endpoints, and the Ollama passthrough.
resource: https://docs.openwebui.com/getting-started/api-endpoints
tags: [open-webui, api, openai-compatible]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openwebui-docs
    resource: "https://docs.openwebui.com"
    title: "Open WebUI documentation"
    author: "site:docs.openwebui.com"
---

# Open WebUI — API

Create an API key under *Settings → Account* (admins can restrict this).

| Endpoint | Purpose |
|---|---|
| `GET /api/models` | List all models from every connection |
| `POST /api/chat/completions` | OpenAI-compatible chat across any connected model, with optional `files` / knowledge collections for RAG |
| `POST /api/v1/files/` | Upload a file |
| `POST /api/v1/knowledge/{id}/file/add` | Add a file to a knowledge base |
| `/ollama/...` | Proxied Ollama API |

This makes Open WebUI a lightweight gateway with users and RAG in front of your models — though [LiteLLM](../../runtime/litellm/index.md) is the better fit for pure API routing.

## Related

[Open WebUI index](index.md) · [Snippets](snippets.md)
