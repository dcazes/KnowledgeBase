---
type: Reference
title: Open WebUI Snippets
description: Open WebUI snippets — Docker Compose with Ollama, API chat requests, RAG over an uploaded file, and admin housekeeping.
resource: https://docs.openwebui.com
tags: [open-webui, snippets, docker, curl, cheat-sheet]
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

# Open WebUI — Snippets

## Compose with Ollama

```yaml
services:
  ollama:
    image: ollama/ollama
    volumes: [ollama:/root/.ollama]
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    ports: ["127.0.0.1:3000:8080"]
    environment:
      OLLAMA_BASE_URL: http://ollama:11434
      WEBUI_SECRET_KEY: change-me
    volumes: [open-webui:/app/backend/data]
volumes: { ollama: {}, open-webui: {} }
```

## API

```bash
curl http://localhost:3000/api/chat/completions -H "Authorization: Bearer $OWUI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen3:8b", "messages": [{"role": "user", "content": "Hello"}]}'

# RAG over an uploaded file
FILE_ID=$(curl -s -X POST http://localhost:3000/api/v1/files/ -H "Authorization: Bearer $OWUI_KEY" \
  -F "file=@handbook.pdf" | jq -r .id)
curl http://localhost:3000/api/chat/completions -H "Authorization: Bearer $OWUI_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\": \"qwen3:8b\", \"messages\": [{\"role\": \"user\", \"content\": \"What is the leave policy?\"}], \"files\": [{\"type\": \"file\", \"id\": \"$FILE_ID\"}]}"
```

## Related

[Open WebUI index](index.md) · [API](api.md)
