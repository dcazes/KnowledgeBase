---
type: Reference
title: Hindsight Snippets
description: Hindsight snippets — retain, recall and reflect in Python and Node, temporal recall, embedded server, the two-line LLM wrapper, and the per-bank MCP endpoint.
resource: https://github.com/vectorize-io/hindsight
tags: [hindsight, snippets, python, typescript, mcp, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hindsight-github
    resource: "https://github.com/vectorize-io/hindsight"
    title: "vectorize-io/hindsight on GitHub"
    author: "site:github.com"
---

# Hindsight — Snippets

## Python client

```python
from hindsight_client import Hindsight
c = Hindsight(base_url="http://localhost:8888")

c.retain(bank_id="alice", content="Alice got promoted to senior engineer",
         context="career update", timestamp="2026-06-15T10:00:00Z")
c.recall(bank_id="alice", query="What does Alice do?")
c.recall(bank_id="alice", query="What happened in June?")     # temporal
c.reflect(bank_id="alice", query="What should I know before Alice's review?")
```

## Node.js

```javascript
const { HindsightClient } = require('@vectorize-io/hindsight-client');
const client = new HindsightClient({ baseUrl: 'http://localhost:8888' });
await client.retain('alice', 'Alice loves hiking in Yosemite');
console.log(await client.recall('alice', 'What does Alice like?'));
```

## LLM wrapper (automatic memory)

```python
from openai import OpenAI
from hindsight_litellm import wrap_openai      # pip install hindsight-litellm

client = wrap_openai(OpenAI(), bank_id="user-123", hindsight_api_url="http://localhost:8888")
client.chat.completions.create(model="gpt-5-mini",
                               messages=[{"role": "user", "content": "What do you know about me?"}])
```

`wrap_anthropic()` does the same for the Anthropic SDK. [LiteLLM](../../runtime/litellm/index.md) sits underneath.

## MCP

Each bank has an [MCP](../../concepts/mcp.md) endpoint, on by default: `http://localhost:8888/mcp/{bank_id}/` exposing retain, recall and reflect as tools.

## Related

[Hindsight index](index.md) · [AI Integration](ai-integration.md)
