---
type: Playbook
title: OpenClaw — Installation
description: Setting up OpenClaw via the openclaw onboard CLI and the Windows Hub companion app.
resource: https://docs.openclaw.ai/
tags: [openclaw, install, onboard, windows-hub, gateway, setup]
generated: { by: "human:daniel", at: "2026-07-09T03:11:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T03:11:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: install-onboard-docs
    resource: "https://docs.openclaw.ai/"
    title: "Install / onboard docs"
    author: "site:docs.openclaw.ai"
  - id: github
    resource: "https://github.com/openclaw/openclaw"
    title: "GitHub"
    author: "site:github.com"
---

# Preferred setup — `openclaw onboard`

The recommended path is the interactive CLI setup, which walks through gateway, workspace, channels, and skills:

```bash
# install (method depends on platform/release; see docs)
# then:
openclaw onboard
```

`onboard` guides you step by step through:
1. **Gateway** — the core server.
2. **Workspace** — your assistant's working directory.
3. **Channels** — which chat apps to connect (Discord, Telegram, …).
4. **Skills** — initial skills to enable.

Works on macOS, Linux, and Windows.

# Windows Hub (Windows only)

Native companion app for:
* Setup and tray status
* Chat
* **Node mode** (run OpenClaw as a node)
* **Local MCP mode** (serve MCP tools locally)

# Verify

```bash
openclaw status          # if available
# or check the gateway process / logs from onboard
```

# Notes

* No launcher found in `programs/` on this machine — OpenClaw is documented from upstream; install when you want it.
* Channel plugins each need their own credentials (bot tokens, etc.) configured during onboard.

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `openclaw: command not found` | not installed | install per docs; check PATH |
| Channel won't connect | missing token | re-run onboard step for that channel |
| Gateway not starting | port/dep issue | check onboard logs; free the port |
