---
type: Reference
title: promptfoo Snippets
description: promptfoo configuration snippets — comparing a hosted and a local model with assertions, testing an HTTP RAG endpoint, a red-team config, and CI commands.
resource: https://www.promptfoo.dev/docs/configuration/guide/
tags: [promptfoo, snippets, yaml, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: promptfoo-docs
    resource: "https://www.promptfoo.dev/docs/"
    title: "promptfoo documentation"
    author: "site:promptfoo.dev"
---

# promptfoo — Snippets

## `promptfooconfig.yaml`

```yaml
prompts:
  - "Answer briefly using only the context.\nContext: {{context}}\nQuestion: {{question}}"
providers:
  - openai:gpt-5-mini
  - ollama:chat:qwen3:8b
  - id: https
    label: my-rag-api
    config:
      url: http://localhost:8000/ask
      method: POST
      body: { question: "{{question}}" }
      transformResponse: json.answer
tests:
  - vars: { question: "What is the refund window?", context: "Refunds within 30 days." }
    assert:
      - type: contains
        value: "30"
      - type: llm-rubric
        value: "Does not invent policies not in the context"
      - type: latency
        threshold: 3000
```

## Red team

```yaml
redteam:
  purpose: "Customer-support bot for an online shop"
  plugins: [pii, prompt-injection, excessive-agency, harmful]
  strategies: [jailbreak, base64]
```

```bash
promptfoo redteam run
promptfoo eval -o results.json --no-cache     # CI
```

## Related

[promptfoo index](index.md) · [Overview](overview.md)
