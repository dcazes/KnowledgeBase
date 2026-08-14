---
type: Reference
title: OpenWebUI — API
description: OpenWebUI's OpenAI-compatible API plus admin endpoints, with examples against the :3001 service.
resource: https://docs.openwebui.com/openapi/
tags: [openwebui, api, openai-compatible, chat, admin, integration]
generated: { by: "human:daniel", at: "2026-07-09T02:05:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T02:05:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: openwebui-openapi-docs
    resource: "https://docs.openwebui.com/openapi/"
    title: "OpenWebUI OpenAPI/docs"
    author: "site:docs.openwebui.com"
  - id: configuration-model-connection
    resource: "configuration.md"
    title: "Configuration (model connection)"
---

# OpenWebUI — OpenAI-compatible API

OpenWebUI exposes an **OpenAI-compatible** REST API (under `/api` and `/ollama` for Ollama-style calls), so existing OpenAI SDKs work by pointing the base URL at it.

Base URL: `http://localhost:3001` (or `http://localhost:8088` in host-network mode).

# Authentication

Generate a key in **Admin Settings → Tokens / API Keys**, then:
```
Authorization: Bearer <OPENWEBUI_TOKEN>
```

# Chat completion (OpenAI-compatible)

```bash
curl -X POST http://localhost:3001/v1/chat/completions \
  -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' \
  -d '{
    "model": "<model-id>",
    "messages": [{"role":"user","content":"Hello"}],
    "stream": false
  }'
```

# Ollama-style endpoint

For Ollama-compatible clients:
```
POST /ollama/api/chat
POST /ollama/api/generate
```
(Not used here since no Ollama is configured, but the routes exist.)

# Admin / management

OpenWebUI also has its own admin API (users, models, documents) under `/api/v1/...` — documented in the OpenAPI spec at `/docs` (FastAPI Swagger UI) when running.

```bash
curl -s http://localhost:3001/docs       # Swagger UI
curl -s http://localhost:3001/openapi.json | head
```

# SDK usage

```python
from openai import OpenAI
c = OpenAI(base_url="http://localhost:3001/v1", api_key="<TOKEN>")
r = c.chat.completions.create(model="<model-id>",
    messages=[{"role":"user","content":"Hi"}])
print(r.choices[0].message.content)
```
