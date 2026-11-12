---
type: Reference
title: Space Agent Configuration
description: Space Agent server configuration — users and the _admin group, customware path, host and port, and zero-downtime supervised production mode.
resource: https://github.com/agent0ai/space-agent
tags: [space-agent, configuration, production]
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

# Space Agent — Configuration

```bash
node space set CUSTOMWARE_PATH=/srv/space/customware     # where user/group customisations live
node space supervise HOST=0.0.0.0 PORT=3000              # production: zero-downtime auto-update
node space help                                          # full command surface (commands/params.yaml)
```

* Admins belong to the `_admin` group; use admin mode to recover when a user or group change breaks the workspace.
* Put the server behind TLS and authentication, or on a private network such as [Tailscale](../../runtime/tailscale/index.md), since agents can change the running app.

## Related

[Space Agent index](index.md) · [Snippets](snippets.md)
