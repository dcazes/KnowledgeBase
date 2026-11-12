---
type: Reference
title: Camofox Snippets
description: Camofox REST snippets — create a tab, navigate, snapshot, click by ref, search macros and structured extraction; check /docs on your instance for exact routes.
resource: https://github.com/jo-inc/camofox-browser
tags: [camofox, snippets, rest, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: camofox-github
    resource: "https://github.com/jo-inc/camofox-browser"
    title: "jo-inc/camofox-browser on GitHub"
    author: "site:github.com"
---

# Camofox — Snippets

Routes from the project README; the full list is in the OpenAPI spec at `http://localhost:9377/openapi.json`. Calls carry a `userId` (session owner) and optionally a `sessionKey` (task).

```bash
# open a tab
curl -X POST localhost:9377/tabs -H 'Content-Type: application/json' \
  -d '{"userId": "agent1", "sessionKey": "task1", "url": "https://example.com"}'

# accessibility snapshot with element refs
curl "localhost:9377/tabs/TAB_ID/snapshot?userId=agent1"

# click and type by ref
curl -X POST localhost:9377/tabs/TAB_ID/click -H 'Content-Type: application/json' \
  -d '{"userId": "agent1", "ref": "e1"}'
curl -X POST localhost:9377/tabs/TAB_ID/type -H 'Content-Type: application/json' \
  -d '{"userId": "agent1", "ref": "e2", "text": "graph rag", "pressEnter": true}'

# navigate, extract, end a session
curl -X POST localhost:9377/tabs/TAB_ID/navigate -H 'Content-Type: application/json' \
  -d '{"userId": "agent1", "url": "https://example.org"}'
curl -X POST localhost:9377/tabs/TAB_ID/extract -H 'Content-Type: application/json' \
  -d '{"userId": "agent1", "schema": {"type": "object", "properties": {"title": {"type": "string", "x-ref": "e3"}}}}'
curl -X DELETE localhost:9377/sessions/agent1
```

Cookie import (`POST /sessions/:userId/cookies`) only works when `CAMOFOX_API_KEY` is set; `POST /stop` needs `CAMOFOX_ADMIN_KEY`.

## Related

[Camofox index](index.md) · [Usage](usage.md)
