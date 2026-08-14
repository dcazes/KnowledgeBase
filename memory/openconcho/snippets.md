---
type: CheatSheet
title: OpenConcho Snippets
description: OpenConcho cheat sheet — npx run, docker compose, add instance, fleet view, chat probe (v0.16.0).
resource: https://github.com/offendingcommit/openconcho
tags: [openconcho, snippets, cheat-sheet]
timestamp: 2026-08-13T00:00:00Z
---

# Snippets

## Run

```bash
npx openconcho                     # latest (0.16.1)
cd programs/openconcho && npm run dev   # checkout (0.16.0)
docker compose up -d               # from checkout
```

## Connect to Honcho

```text
1. Open the UI
2. Instances → Add → http://localhost:8000 (+ keys if set)
3. Dashboard shows workspace count / queue status (10 s auto-refresh)
```

## Browse

```text
Fleet dashboard → all instances side-by-side
Workspaces → pick a workspace → peers / sessions / memories
Peers → representations, context, peer cards
```

## Chat

```text
Open chat → converse against the instance with full memory context
```

## Verify connectivity

```bash
curl -s http://localhost:8000/health      # Honcho itself (if deployed)
# UI dashboard rendering counts = connection OK
```

# Citations

[1] [OpenConcho GitHub](https://github.com/offendingcommit/openconcho)
