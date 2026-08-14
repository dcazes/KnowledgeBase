---
type: Playbook
title: Hermes — Installation & Runtime
description: Running Hermes (desktop GUI / TUI), its home directory, and where config/secrets/skills live.
resource: https://hermes-agent.nousresearch.com
tags: [hermes, install, runtime, desktop, tui, home-dir]
generated: { by: "human:daniel", at: "2026-07-09T03:21:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T03:21:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: setup-note-config-files
    resource: "/../../vault/03%20-%20Reference/Hermes%20Setup.md"
    title: "Setup note — config files"
  - id: overview
    resource: "overview.md"
    title: "Overview"
---

# Runtime

Hermes runs as a **desktop GUI** and/or **TUI**:

```bash
hermes            # launch TUI/CLI
# or open the desktop GUI application
```

# Home directory

Everything lives under `~/.hermes/`:

| Path | Purpose |
|------|---------|
| `~/.hermes/config.yaml` | Main config — model, agent limits, toolsets, browser |
| `~/.hermes/.env` | Secrets only (API keys, tokens, timeouts, flags) |
| `~/.hermes/auth.json` | Authentication state |
| `~/.hermes/skills/` | User-installed skills |
| `~/.hermes/plugins/` | User-installed plugins |
| `~/.hermes/cron/` | Scheduled cron jobs |
| `~/.hermes/memories/` | Profile-scoped memory |

> **Rule:** `.env` is for secrets (API keys, tokens). All behavioral settings belong in `config.yaml`.

# Verify

```bash
ls -la ~/.hermes/
hermes --help          # if available
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `hermes: command not found` | not on PATH | install/relink the binary |
| Model errors | bad key in `.env` | check `~/.hermes/.env` |
| Toolset missing | disabled in config | `hermes setup tools` |
