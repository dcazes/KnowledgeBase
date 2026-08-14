---
type: Concept
title: Honcho AI Integration
description: Wire Honcho into agents — peers/sessions/messages, query context via peer.chat, conclusions, Python/TS SDKs, vs Mem0/MemOS/Graphiti for user memory.
resource: https://docs.honcho.dev
tags: [honcho, integration, sdk, peers, agents]
timestamp: 2026-08-13T00:00:00Z
---

# AI Integration

## Python SDK flow (v3 API)

```python
from honcho import Honcho

client = Honcho(base_url="http://localhost:8000")

# per conversation
alice = client.peer("alice")
bot = client.peer("support-bot")
session = client.session("support-ticket-42")
session.add_peers([alice, bot])

# stream turns through Honcho
session.add_messages([
    alice.message("I'm shopping for a laptop under $800"),
    bot.message("Great — gaming or everyday use?"),
])

# query the model's memory of this peer
response = alice.chat("What did the bot ask me?", session=session)
print(response.message)
```

## TypeScript SDK

```ts
import { Honcho } from "@honcho-ai/sdk";
const client = new Honcho({ baseURL: "http://localhost:8000" });
const alice = client.peer("alice");
const session = client.session("support-ticket-42");
session.addPeers([alice]);
session.addMessages([alice.message("…")]);
const resp = await alice.chat("What did they ask?", { session });
```

## Agent pattern

1. Create/reuse peers per user; reuse the session per conversation.
2. After each exchange, batch both turns via `session.add_messages(...)`.
3. Before responding, query `peer.chat("…", session=session)` to ground the reply in Honcho's derived context (conclusions).
4. Inspect derived state via `honcho conclusion list` / `queue-status` (CLI).

## In this stack

* Not deployed here (2026-08-13); fits alongside [Mem0](../mem0/index.md) (facts) and [MemOS](../memos/index.md) (memory OS) — Honcho adds **user modeling** (peers + derived conclusions) none of the others provide.
* [Graphiti](../graphiti/index.md) covers temporal fact provenance; Honcho covers *who the user is*.
* UI companion: [OpenConcho](../openconcho/index.md) (Honcho UI).

# Citations

[1] [Honcho docs — quickstart](https://docs.honcho.dev)
[2] [Honcho GitHub](https://github.com/plastic-labs/honcho)
