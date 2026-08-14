---
type: Reference
title: Camofox — Usage
description: Driving the Camofox browser server via its API on :9377 and watching it via noVNC on :6080.
resource: https://github.com/daijro/camoufox
tags: [camofox, usage, api, novnc, browser-automation]
generated: { by: "human:daniel", at: "2026-07-09T01:02:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T01:02:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: camoufox-playwright-compatible
    resource: "https://github.com/daijro/camoufox"
    title: "Camoufox (Playwright-compatible)"
    author: "site:github.com"
  - id: installation-ports
    resource: "installation.md"
    title: "Installation / ports"
---

# Two faces of Camofox

| Surface | Port | Use |
|---------|------|-----|
| **API** | `9377` | Agents drive the browser programmatically (navigate, click, read DOM). |
| **noVNC** | `6080` | A human watches/controls the live browser in a web VNC client. **Opt-in** (`ENABLE_VNC=1`). |

# API (port 9377)

The server exposes a browser-control API (Camoufox/Camofox server contract). Typical operations an agent performs:

* **New session / page** — open a headed Firefox instance.
* **Navigate** — go to a URL.
* **Interact** — click, type, scroll, wait.
* **Read** — extract DOM/text/screenshot.

Exact endpoints depend on the Camofox server build; the key fact is the agent talks to `http://localhost:9377/`. From Hermes or a script:

```python
# conceptual shape (confirm against the running server's API)
import requests
BASE = "http://localhost:9377"
r = requests.post(f"{BASE}/session", json={"url": "https://example.com"})
print(r.json())
```

> For precise endpoints, inspect the running server or the Camoufox docs; the API surface follows Playwright/CDP-style primitives since Camoufox is Playwright-compatible.

# Watching via noVNC (port 6080)

Open in a browser:
```
http://localhost:6080/
```
You'll see the live Firefox desktop. Useful for:
* **Visual logins** — OAuth/Google screens that need a human (or a watched click).
* **Debugging** — see exactly what the agent sees.
* **CAPTCHA solving** — a human can step in when anti-detection isn't enough.

# Typical flow

1. `make up` (server + VNC start).
2. Agent opens a session via `:9377`, navigates, interacts.
3. If a login/CAPTCHA appears, you open `:6080` and complete it.
4. Agent continues and reads results.
