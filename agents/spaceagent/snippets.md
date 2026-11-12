---
type: Reference
title: Space Agent Snippets
description: Space Agent CLI cheat sheet — creating users, serving, development mode, configuration and supervised production runs.
resource: https://github.com/agent0ai/space-agent
tags: [space-agent, snippets, cli, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: space-agent-github
    resource: "https://github.com/agent0ai/space-agent"
    title: "agent0ai/space-agent on GitHub"
    author: "site:github.com"
---

# Space Agent — Snippets

```bash
node space user create alice --password "..." --full-name "Alice" --groups team
node space serve
npm run dev
node space set CUSTOMWARE_PATH=/srv/space/customware
node space supervise HOST=0.0.0.0 PORT=3000
node space help
```

Example requests to the agent: "Build me a page that tracks my reading list", "Add a widget that shows today's calendar", "Turn this checklist into a reusable workflow for the team".

## Related

[Space Agent index](index.md) · [Installation](installation.md)
