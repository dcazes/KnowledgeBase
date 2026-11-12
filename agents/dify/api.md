---
type: Reference
title: Dify API
description: Dify's backend-as-a-service APIs — per-app keys, chat-messages, completion-messages and workflows/run endpoints with blocking or streaming responses, file uploads, conversations, and the knowledge (datasets) API.
resource: https://docs.dify.ai
tags: [dify, api, rest, sse]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: dify-docs
    resource: "https://docs.dify.ai"
    title: "Dify documentation"
    author: "site:docs.dify.ai"
---

# Dify — API

Every app has its own API key (*App → API Access*). Base URL: `http://<host>/v1` (self-hosted) or `https://api.dify.ai/v1`.

| Endpoint | App type |
|---|---|
| `POST /chat-messages` | Chatbot, agent, chatflow — `conversation_id` keeps context |
| `POST /completion-messages` | Text generator |
| `POST /workflows/run` | Workflow |
| `POST /files/upload` | Attach files to requests |
| `GET /conversations`, `GET /messages` | History |
| `/datasets/...` | Knowledge API — create datasets, upload documents, retrieve (dataset-scoped keys available) |

`response_mode`: `blocking` or `streaming` (server-sent events). An OpenAPI description and the `difyctl` CLI (1.18+) cover app management.

## Related

[Dify index](index.md) · [Snippets](snippets.md)
