---
type: HowTo
title: Space Agent Installation
description: Install Space Agent — desktop app from GitHub Releases (no terminal), or server (clone, npm install, create user, node space serve); empty local dir on this machine.
resource: https://github.com/agent0ai/space-agent
tags: [space-agent, installation, server, desktop]
timestamp: 2026-08-13T00:00:00Z
---

# Installation

## Option A — Desktop app (no terminal)

Download the latest build from **GitHub Releases** (`agent0ai/space-agent`) and run it — everything runs as one app.

## Option B — Server (teams)

```bash
git clone https://github.com/agent0ai/space-agent.git
cd space-agent
npm install
node space user create admin --password "change-me-now" --full-name "Admin" --groups _admin
node space serve
```

## Option C — Dev

```bash
npm run dev
```

## Status on this machine

* `programs/spaceagent/` — **EMPTY dir**, no checkout, not deployed (verified 2026-08-12).
* No upstream version tag to pin (no semver reported as of 2026-08-13).

# Citations

[1] [Space Agent GitHub — README](https://github.com/agent0ai/space-agent)
