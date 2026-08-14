---
type: Playbook
title: Dify — Snippets & Cheat Sheet
description: Copy-paste commands for deploying Dify, configuring the :4000 model proxy, ingesting knowledge, and calling the API.
resource: https://docs.dify.ai
tags: [dify, snippets, cheat-sheet, deploy, api, rag]
generated: { by: "human:daniel", at: "2026-07-09T00:58:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:58:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: installation
    resource: "installation.md"
    title: "Installation"
  - id: api-reference
    resource: "api.md"
    title: "API reference"
  - id: model-providers
    resource: "model-providers.md"
    title: "Model providers"
---

# Deploy

```bash
cd programs/archive/dify/docker
cp .env.example .env
docker compose up -d
```
Dashboard: http://localhost/install  → then http://localhost/

# Status / logs

```bash
docker compose ps
docker compose logs -f api
curl -s -o /dev/null -w "%{http_code}\n" http://localhost/install
```

# Pick a vector store

Edit `docker/.env` → set `VECTOR_STORE=weaviate` (default) / `qdrant` / `pgvector` / `chroma` / `milvus`, then enable that service in the compose and `docker compose up -d`.

# Wire your :4000 model proxy

In UI: **Settings → Model Provider → OpenAI-API-compatible**:
```
Base URL: http://localhost:4000/v1
API Key:  <proxy-accepted value>
```
Do the same for an embedding model if using RAG.

# Ingest a Knowledge Base (API)

```bash
# create dataset
curl -X POST http://localhost/v1/datasets \
  -H 'Authorization: Bearer <API_KEY>' -H 'Content-Type: application/json' \
  -d '{"name":"my-kb"}'
# upload + index a document (multipart)
curl -X POST http://localhost/v1/datasets/<ID>/documents \
  -H 'Authorization: Bearer <API_KEY>' -F 'data=@/path/doc.pdf' -F 'indexing_technique=high_quality'
```

# Chat via API

```bash
curl -X POST http://localhost/v1/chat-messages \
  -H 'Authorization: Bearer <APP_API_KEY>' -H 'Content-Type: application/json' \
  -d '{"inputs":{},"query":"What is RAG?","user":"local","response_mode":"blocking"}'
```

# Run a workflow

```bash
curl -X POST http://localhost/v1/workflows/run \
  -H 'Authorization: Bearer <APP_API_KEY>' -H 'Content-Type: application/json' \
  -d '{"inputs":{"topic":"graphs"},"response_mode":"streaming"}'
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| :80 clash | port in use | change nginx port in compose/.env |
| Jobs stuck | redis/worker down | `docker compose restart redis worker` |
| RAG empty | wrong vector store / embedding | verify VECTOR_STORE + embedding model |
| Model 401 | proxy key | set API key the :4000 proxy accepts |
