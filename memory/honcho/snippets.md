---
type: CheatSheet
title: Honcho Snippets
description: Honcho cheat sheet — install SDK, peers/sessions/messages, query context via peer.chat, conclusions, TS SDK (@honcho-ai/sdk), server startup.
resource: https://docs.honcho.dev
tags: [honcho, snippets, cheat-sheet]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: honcho-docs-quickstart
    resource: "https://docs.honcho.dev"
    title: "Honcho docs — quickstart"
    author: "site:docs.honcho.dev"
  - id: honcho-github
    resource: "https://github.com/plastic-labs/honcho"
    title: "Honcho GitHub"
    author: "site:github.com"
---

# Honcho — Snippets

## Install + server

```bash
pip install honcho-ai                    # SDK 2.3.0
cd programs/honcho && docker compose up -d          # server (API + workers) on :8000
# or run the FastAPI app directly:
cd programs/honcho && fastapi run --host 0.0.0.0 --port 8000 src/main.py
```

## Peer/session lifecycle (v3 SDK API)

```python
from honcho import Honcho

client = Honcho(api_key="your-api-key")

alice = client.peer("alice")
bob = client.peer("bob")

session = client.session("conversation-1")
session.add_peers([alice, bob])

session.add_messages([
    alice.message("Hello, Bob!"),
    bob.message("Hi Alice, how are you?"),
])

# query Honcho's memory of this peer within the session
response = alice.chat("What did Bob say to me?", session=session)
print(response.message)
```

## Async

```python
peer = await client.aio.peer("user-123")
resp = await peer.aio.chat("query", session=session)
async for p in client.aio.peers():
    print(p.id)
```

## Conclusions

```bash
honcho conclusion list                  # derived conclusions (filter --observer/--observed)
honcho conclusion search "query"        # semantic search
honcho workspace queue-status           # deriver queue
```

## TypeScript

```ts
import { Honcho } from "@honcho-ai/sdk";
const client = new Honcho({ apiKey: "..." });
const alice = client.peer("alice");
const session = client.session("conversation-1");
session.addPeers([alice]);
session.addMessages([alice.message("Hello!")]);
const resp = await alice.chat("What did they say?", { session });
```
