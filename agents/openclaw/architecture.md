---
type: Concept
title: OpenClaw Architecture
description: OpenClaw's components — the Gateway control plane for sessions, tools, events and channels; the Control UI, CLI and TUI clients; channel adapters; and companion apps and device nodes for voice, Canvas, camera and screen.
resource: https://docs.openclaw.ai/concepts/architecture
tags: [openclaw, architecture, gateway, nodes]
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

# OpenClaw — Architecture

```
WhatsApp / Telegram / Slack / Discord / iMessage / …
                 │  channel adapters
                 ▼
            ┌──────────┐      Control UI · CLI · TUI
            │ Gateway  │◀──── (clients)
            └──────────┘
   sessions · tools · events · skills · plugins · memory
                 │
     model providers / harnesses (Claude, Codex, local)
                 │
     companion apps & nodes (voice, Canvas, camera, screen)
```

* **Gateway** — the local control plane, run as a daemon. Everything connects to it.
* **Clients** — the browser Control UI (`openclaw dashboard`), CLI and terminal UI.
* **Channels** — adapters that bring the assistant to messaging services.
* **Nodes and companion apps** — add device-local actions on supported platforms.

Keep the Gateway bound to localhost or a private network such as [Tailscale](../../runtime/tailscale/index.md); the docs include an exposure runbook.

## Related

[OpenClaw index](index.md) · [Overview](overview.md)
