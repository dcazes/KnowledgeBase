---
type: HowTo
title: Space Agent Configuration
description: Configure Space Agent — admin user/groups, server bind, CUSTOMWARE_PATH, supervised zero-downtime deployment.
resource: https://github.com/agent0ai/space-agent
tags: [space-agent, configuration, server, admin]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: space-agent-github-readme
    resource: "https://github.com/agent0ai/space-agent"
    title: "Space Agent GitHub — README"
    author: "site:github.com"
---

# Space Agent — Configuration

## Users & groups

```bash
node space user create admin --password "..." --full-name "Admin" --groups _admin
```

* `_admin` group = admin role (stable control plane).
* Per-user workspaces with **group sharing** for teams.
* Hierarchical structure: personal assistant → groups of users.

## Production serve

```bash
node space set CUSTOMWARE_PATH=/srv/space/customware   # where custom-built tools live
node space supervise HOST=0.0.0.0 PORT=3000            # zero-downtime auto-update
```

* `supervise` runs with auto-update (restarts on new code) — the production entrypoint.
* `HOST`/`PORT` env for bind.

## Capabilities

* Capabilities are plain-text **`SKILL.md`** files in the workspace the agent writes and extends — the "config" for what the agent can do grows itself.
* Git-backed history enables rollback ("time travel") of workspace changes.

## Status here

Not deployed (empty local dir). Config notes from upstream docs only.
