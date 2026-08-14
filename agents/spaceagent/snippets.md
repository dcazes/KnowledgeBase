---
type: CheatSheet
title: Space Agent Snippets
description: Space Agent cheat sheet — desktop release, server install, user create, serve, supervise, dev mode.
resource: https://github.com/agent0ai/space-agent
tags: [space-agent, snippets, cheat-sheet]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: space-agent-github
    resource: "https://github.com/agent0ai/space-agent"
    title: "Space Agent GitHub"
    author: "site:github.com"
---

# Snippets

## Desktop

```text
Download latest build from GitHub Releases → run the app (no terminal)
```

## Server

```bash
git clone https://github.com/agent0ai/space-agent.git && cd space-agent
npm install
node space user create admin --password "change-me-now" --full-name "Admin" --groups _admin
node space serve
```

## Production (zero-downtime)

```bash
node space set CUSTOMWARE_PATH=/srv/space/customware
node space supervise HOST=0.0.0.0 PORT=3000
```

## Dev

```bash
npm run dev
```

## Workspace features

```text
- agent builds pages/tools/widgets/workflows live into the workspace
- capabilities = SKILL.md files (plain text) the agent extends itself
- Git-backed history for rollback
- admin mode = stable control plane
```
