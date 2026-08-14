---
type: Playbook
title: CloakBrowser — Snippets & Cheat Sheet
description: Copy-paste commands to launch CloakBrowser, connect over CDP, and run the Docker manager.
resource: https://github.com/cloakhq/cloakbrowser
tags: [cloakbrowser, snippets, cheat-sheet, cdp, cli, docker]
timestamp: 2026-07-09T01:15:00Z
---

# Launch (CLI)

```bash
npx cloakbrowser --remote-debugging-port=9222 --headless=false
```

# Verify CDP

```bash
curl -s http://localhost:9222/json/version
```

# Drive via Playwright (Python)

```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://localhost:9222")
    pg = b.new_page(); pg.goto("https://example.com")
    print(pg.title()); b.close()
```

# Drive via Puppeteer (Node)

```javascript
const p = require('puppeteer-core');
const b = await p.connect({ browserURL: 'http://localhost:9222' });
const pg = await b.newPage(); await pg.goto('https://example.com');
console.log(await pg.title());
```

# Docker manager

```bash
cd programs/cloakbrowser
docker compose up -d cloakbrowser-manager     # :8080, volume cloak_profiles
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080/
docker volume ls | grep cloak_profiles
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| :9222 refused | not launched | run the `npx` command |
| `npx` not found | Node missing | install Node |
| Docker :8080 down | not started | `docker compose up -d cloakbrowser-manager` |
| Profiles lost | volume missing | check `cloak_profiles` |

# Citations

[1] [Installation](installation.md)
[2] [Usage (CDP)](usage.md)
