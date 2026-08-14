---
type: Playbook
title: Hermes — Snippets Cheat Sheet
description: Copy-paste commands for launching Hermes, editing config, connecting the browser, listing cron jobs, locating skills, and managing toolsets.
resource: https://hermes-agent.nousresearch.com
tags: [hermes, snippets, cheat-sheet, cli, config, browser, cron, skills, toolsets]
timestamp: 2026-07-09T03:27:00Z
---

# Launch

```bash
hermes            # launch TUI/CLI
# or open the desktop GUI application
```

# Edit config

```bash
${EDITOR:-vim} ~/.hermes/config.yaml     # behavioral settings
${EDITOR:-vim} ~/.hermes/.env            # secrets only
```

Config anatomy: [Configuration](configuration.md).

# Connect the browser

```bash
# 1. Start Chromium with remote debugging
chromium --remote-debugging-port=9222 --user-data-dir=$HOME/.hermes/chrome-debug

# 2. In the Hermes CLI
/browser connect      # auto-connects http://127.0.0.1:9222
/browser status
/browser disconnect
```

Full workflow: [Browser](browser.md).

# List cron jobs

```bash
# From inside Hermes (cronjob tool):
cronjob action='list'
```

# Locate skills / plugins / memory

```bash
ls ~/.hermes/skills/      # procedural memory (SKILL.md)
ls ~/.hermes/plugins/     # extensions
ls ~/.hermes/cron/        # scheduled jobs
ls ~/.hermes/memories/    # MEMORY.md + USER.md
```

# Manage toolsets

```bash
hermes setup tools        # enable/disable CLI toolsets
```

Enabled here: `browser, clarify, code_execution, computer_use, context_engine, cronjob, delegation, file, image_gen, memory, session_search, skills, terminal, todo, web`.

# Verify a connection

```bash
curl -s http://127.0.0.1:9222/json/version   # Chromium debugger up
```

# Citations

[1] [Hermes — setup note (vault)](/../../vault/03%20-%20Reference/Hermes%20Setup.md)
[2] [Hermes (Nous Research)](https://hermes-agent.nousresearch.com)
[3] [Configuration](configuration.md)
[4] [Browser](browser.md)
[5] [Skills & Plugins](skills-plugins.md)
