---
type: Reference
title: Hermes — Browser
description: Local agent-browser mode, the /browser connect workflow (desktop Chromium at :9222), Camofox anti-detect backend, and computer_use.
resource: https://hermes-agent.nousresearch.com
tags: [hermes, browser, agent-browser, chromium, remote-debugging, camofox, computer-use]
timestamp: 2026-07-09T03:24:00Z
---

# Local agent-browser mode

Hermes runs the browser in **local** mode (`browser.cloud_provider: local` in `config.yaml`). All `browser_*` tools then operate inside a real desktop browser window you control.

# /browser connect workflow

1. **Start Chromium with remote debugging:**

```bash
chromium --remote-debugging-port=9222 \
         --user-data-dir=$HOME/.hermes/chrome-debug
```

2. **Connect from the Hermes CLI:**

```bash
/browser connect      # auto-connects to http://127.0.0.1:9222
/browser status       # confirm connection
/browser disconnect    # release the window
```

After `connect`, every `browser_*` tool (navigate, snapshot, click, type, …) drives that Chromium window.

# Browser environment flags

These live in `~/.hermes/.env` (secrets/flags only, never in `config.yaml`):

| Env var | Purpose |
|---------|---------|
| `BROWSERBASE_PROXIES` | Proxy configuration |
| `BROWSERBASE_ADVANCED_STEALTH` | Stealth/anti-detection flags |
| `BROWSER_SESSION_TIMEOUT` | Session timeout (e.g. `300`) |
| `BROWSER_INACTIVITY_TIMEOUT` | Inactivity timeout (e.g. `120`) |
| `CHROME_DESKTOP` | Desktop entry name (e.g. `Hermes.desktop`) |

# Camofox backend (anti-detect)

Hermes can use **Camofox** as an anti-detect browser backend instead of plain Chromium. Camofox is documented in its own KB section:

* [Camofox](/../../camofox/index.md)

# computer_use (background desktop control)

Beyond the browser, Hermes's **computer_use** toolset drives the whole Linux desktop in the background — clicking, typing, scrolling — without stealing the user's cursor or focus. It complements `/browser connect` for full-OS automation.

# Verify

```bash
curl -s http://127.0.0.1:9222/json/version   # Chromium debugger reachable
/browser status                               # from inside Hermes CLI
```

# Citations

[1] [Hermes browser — setup note (vault)](/../../vault/03%20-%20Reference/Hermes%20Setup.md)
[2] [Hermes (Nous Research)](https://hermes-agent.nousresearch.com)
[3] [Camofox](/../../camofox/index.md)
[4] [Configuration](configuration.md)
