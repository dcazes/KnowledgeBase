---
type: Reference
title: LM Studio Snippets
description: LM Studio snippets — lms CLI commands, OpenAI-compatible requests to the local server, and the Python and TypeScript SDKs.
resource: https://lmstudio.ai/docs
tags: [lmstudio, snippets, cli, python, typescript, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: lms-github
    resource: "https://github.com/lmstudio-ai/lms"
    title: "lmstudio-ai/lms (CLI)"
    author: "site:github.com"
  - id: lmstudio-docs
    resource: "https://lmstudio.ai/docs"
    title: "LM Studio documentation"
    author: "site:lmstudio.ai"
---

# LM Studio — Snippets

## CLI

```bash
lms status
lms ls                       # downloaded models (--json for scripts)
lms ps                       # loaded models
lms load <model> -y          # load with maximum GPU offload
lms unload --all
lms server start | stop
lms log stream
```

## OpenAI-compatible server

```python
from openai import OpenAI
c = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
print(c.chat.completions.create(model="qwen3-8b",
      messages=[{"role": "user", "content": "Hello"}]).choices[0].message.content)
```

## Python SDK

```python
import lmstudio as lms
model = lms.llm("qwen3-8b")
print(model.respond("What is the capital of France?"))
```

## TypeScript SDK

```typescript
import { LMStudioClient } from "@lmstudio/sdk";
const client = new LMStudioClient();
const model = await client.llm.model("qwen3-8b");
console.log((await model.respond("Hello")).content);
```

## Related

[LM Studio index](index.md) · [AI Integration](ai-integration.md)
