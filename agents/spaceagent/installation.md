---
type: Playbook
title: Space Agent Installation
description: Run Space Agent as a desktop app, as a self-hosted Node.js server with an admin user, or in development mode.
resource: https://github.com/agent0ai/space-agent
tags: [space-agent, installation, node]
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

# Space Agent — Installation

**Desktop:** download the latest build from GitHub Releases; it runs everything as one app.

**Server:**

```bash
git clone https://github.com/agent0ai/space-agent.git && cd space-agent
npm install
node space user create admin --password "change-me-now" --full-name "Admin" --groups _admin
node space serve
```

**Development:** `npm run dev` (auto-reload).

## Related

[Space Agent index](index.md) · [Configuration](configuration.md)
