---
type: Reference
title: AnythingLLM Snippets
description: AnythingLLM developer API snippets — API keys, chatting with a workspace, uploading and embedding documents, and the OpenAI-compatible endpoint.
resource: https://docs.anythingllm.com
tags: [anythingllm, snippets, api, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: anythingllm-docs
    resource: "https://docs.anythingllm.com"
    title: "AnythingLLM documentation"
    author: "site:docs.anythingllm.com"
---

# AnythingLLM — Snippets

Create an API key in *Settings → Developer API*; Swagger docs are served at `/api/docs`.

```bash
# chat with a workspace
curl -X POST http://localhost:3001/api/v1/workspace/my-workspace/chat \
  -H "Authorization: Bearer $ALLM_KEY" -H "Content-Type: application/json" \
  -d '{"message": "What does the contract say about renewal?", "mode": "query"}'

# upload a document
curl -X POST http://localhost:3001/api/v1/document/upload \
  -H "Authorization: Bearer $ALLM_KEY" -F "file=@contract.pdf"

# OpenAI-compatible: each workspace appears as a model
curl http://localhost:3001/api/v1/openai/chat/completions -H "Authorization: Bearer $ALLM_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "my-workspace", "messages": [{"role": "user", "content": "Summarise"}]}'
```

## Related

[AnythingLLM index](index.md) · [AI Integration](ai-integration.md)
