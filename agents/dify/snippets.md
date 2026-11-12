---
type: Reference
title: Dify Snippets
description: Dify curl snippets — chat with an app, stream responses, run a workflow with inputs, and retrieve from a knowledge base.
resource: https://docs.dify.ai
tags: [dify, snippets, curl, cheat-sheet]
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

# Dify — Snippets

```bash
# chat (blocking)
curl -X POST http://localhost/v1/chat-messages -H "Authorization: Bearer $DIFY_APP_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"inputs": {}, "query": "What is our refund policy?", "response_mode": "blocking", "user": "alice"}'

# streaming (SSE)
curl -N -X POST http://localhost/v1/chat-messages -H "Authorization: Bearer $DIFY_APP_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"inputs": {}, "query": "Summarise the onboarding doc", "response_mode": "streaming", "user": "alice"}'

# run a workflow
curl -X POST http://localhost/v1/workflows/run -H "Authorization: Bearer $DIFY_WORKFLOW_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"inputs": {"url": "https://example.com"}, "response_mode": "blocking", "user": "alice"}'

# knowledge retrieval
curl -X POST http://localhost/v1/datasets/$DATASET_ID/retrieve -H "Authorization: Bearer $DIFY_DATASET_KEY" \
  -H 'Content-Type: application/json' -d '{"query": "refund window"}'
```

## Related

[Dify index](index.md) · [API](api.md)
