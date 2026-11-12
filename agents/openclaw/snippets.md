---
type: Reference
title: OpenClaw Snippets
description: OpenClaw CLI cheat sheet — onboarding, gateway control, dashboard, pairing approvals, skills and plugins.
resource: https://docs.openclaw.ai/cli
tags: [openclaw, snippets, cli, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openclaw-docs
    resource: "https://docs.openclaw.ai"
    title: "OpenClaw documentation"
    author: "site:docs.openclaw.ai"
---

# OpenClaw — Snippets

```bash
openclaw onboard --install-daemon
openclaw gateway status
openclaw gateway --force                    # restart after config/plugin changes
openclaw dashboard                          # open the Control UI
openclaw pairing approve telegram 123456    # approve a new DM sender
openclaw skills install <clawhub-slug>
openclaw plugins install @honcho-ai/openclaw-honcho
openclaw plugins install @askjo/camofox-browser
```

## Related

[OpenClaw index](index.md) · [AI Integration](ai-integration.md)
