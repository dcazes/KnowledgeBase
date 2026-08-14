---
type: Reference
title: Dify — API (Backend-as-a-Service)
description: Dify's HTTP API for apps, conversations, completions, knowledge bases, and datasets — with key auth and example calls.
resource: https://docs.dify.ai/api-reference
tags: [dify, api, bas, rest, integration, authentication]
timestamp: 2026-07-09T00:56:00Z
---

# Overview

Every Dify capability is exposed as an API ("Backend-as-a-Service"), so you can embed apps into your own logic. The API base is the `api` service (behind nginx on :80), typically `http://localhost/v1`.

# Authentication

Each app has an **API key** generated in the UI (App → API Access). Send it as:
```
Authorization: Bearer <APP_API_KEY>
```

# Common endpoints (v1)

| Endpoint | Purpose |
|----------|---------|
| `POST /v1/chat-messages` | send a chat message to a Chat app |
| `POST /v1/completion-messages` | send to a Completion app |
| `POST /v1/workflows/run` | run a published Workflow |
| `GET /v1/messages` | fetch conversation history |
| `POST /v1/audio-to-text` | transcription |
| `POST /v1/text-to-audio` | TTS |
| Knowledge Base: `POST /v1/datasets` (create), `POST /v1/datasets/<id>/documents` (upload), `POST /v1/datasets/<id>/documents/<doc>/segments` (index) | RAG ingestion |

# Example: chat message

```bash
curl -X POST http://localhost/v1/chat-messages \
  -H 'Authorization: Bearer <APP_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{
    "inputs": {},
    "query": "What is RAG?",
    "user": "local-user",
    "response_mode": "blocking"
  }'
```

`response_mode` can be `blocking` (full reply) or `streaming` (SSE).

# Example: run a workflow

```bash
curl -X POST http://localhost/v1/workflows/run \
  -H 'Authorization: Bearer <APP_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{"inputs":{"topic":"knowledge graphs"},"response_mode":"streaming"}'
```

# Notes

* The console (UI) and the API share the same backend.
* API keys are per-app; rotate in the UI.
* For server-to-server, point at `http://localhost/v1` (or the api container internally).

# Citations

[1] [API reference (docs)](https://docs.dify.ai/api-reference)
[2] [Architecture — api service](architecture.md)
