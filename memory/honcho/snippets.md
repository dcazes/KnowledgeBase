---
type: Reference
title: Honcho Snippets
description: Honcho SDK snippets — create peers and sessions, add messages, ask the chat endpoint about a peer, and fetch token-budgeted session context in OpenAI message format (Python and TypeScript).
resource: https://github.com/plastic-labs/honcho
tags: [honcho, snippets, python, typescript, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: honcho-github
    resource: "https://github.com/plastic-labs/honcho"
    title: "plastic-labs/honcho on GitHub"
    author: "site:github.com"
---

# Honcho — Snippets

## Python

```python
import os
from honcho import Honcho
from openai import OpenAI

honcho = Honcho(workspace_id="tutoring", api_key=os.environ["HONCHO_API_KEY"])
alice, tutor = honcho.peer("alice"), honcho.peer("tutor")
session = honcho.session("session-1")

session.add_messages([
    alice.message("Can you help me with my math homework?"),
    tutor.message("Absolutely. Send me your first problem!"),
])

print(alice.chat("What learning styles does the user respond to best?"))   # natural-language answer

context = session.context(summary=True, tokens=10_000)
reply = OpenAI().chat.completions.create(model="gpt-5-mini",
                                         messages=context.to_openai(assistant=tutor))
```

## TypeScript

```typescript
import { Honcho } from "@honcho-ai/sdk";

const honcho = new Honcho({ workspaceId: "tutoring", apiKey: process.env.HONCHO_API_KEY });
const alice = await honcho.peer("alice");
const tutor = await honcho.peer("tutor");
const session = await honcho.session("session-1");

await session.addMessages([alice.message("Explain fractions please"), tutor.message("Sure!")]);
const answer = await alice.chat("How confident is the user with fractions?");
const context = await session.context({ summary: true, tokens: 10_000 });
const messages = context.toOpenAI({ assistant: tutor });
```

## Related

[Honcho index](index.md) · [AI Integration](ai-integration.md)
