---
type: Reference
title: n8n Snippets
description: n8n snippets — a webhook-triggered AI agent pattern, calling a workflow, Code node examples in JavaScript and Python, and the public REST API.
resource: https://docs.n8n.io
tags: [n8n, snippets, webhook, code-node, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: n8n-docs
    resource: "https://docs.n8n.io"
    title: "n8n documentation"
    author: "site:docs.n8n.io"
---

# n8n — Snippets

## Pattern: support-triage agent

```
Webhook (POST /triage)
  → AI Agent (chat model: Ollama qwen3:14b, memory: Postgres chat memory)
       tools: Search knowledge (Qdrant vector store tool)
              Create ticket (Jira node as tool)
              Notify (Slack node as tool)
  → Respond to Webhook
```

```bash
curl -X POST https://n8n.example.com/webhook/triage -H "Content-Type: application/json" \
  -d '{"email": "alice@example.com", "message": "I was charged twice this month"}'
```

## Code node

```javascript
// JavaScript: enrich each item
return $input.all().map(item => ({ json: { ...item.json, priority: item.json.message.includes("charged") ? "high" : "normal" } }));
```

```python
# Python
for item in _input.all():
    item.json["length"] = len(item.json["message"])
return _input.all()
```

## Public API

```bash
curl https://n8n.example.com/api/v1/workflows -H "X-N8N-API-KEY: $N8N_KEY"
```

## Related

[n8n index](index.md) · [Overview](overview.md)
