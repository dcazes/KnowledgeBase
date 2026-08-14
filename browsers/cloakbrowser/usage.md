---
type: Reference
title: CloakBrowser — Usage
description: Driving CloakBrowser over CDP (port 9222), connecting Playwright/agent clients, and using persistent profiles.
resource: https://github.com/cloakhq/cloakbrowser
tags: [cloakbrowser, usage, cdp, playwright, automation, agent]
timestamp: 2026-07-09T01:12:00Z
---

# CDP endpoint (port 9222)

With the CLI running (`--remote-debugging-port=9222`), the browser is controllable via the **Chrome DevTools Protocol**:

```
http://localhost:9222/json/version     # browser version + webSocketDebuggerUrl
http://localhost:9222/json             # list open targets (tabs)
http://localhost:9222/json/new?...    # open a new tab
```

# Driving it from code

Because CDP is standard, any CDP client works — including **Playwright** (which speaks CDP under the hood) and **Puppeteer**.

```python
# Playwright can connect to an existing CDP browser:
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp("http://localhost:9222")
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
```

```javascript
// Puppeteer connecting over CDP:
const puppeteer = require('puppeteer-core');
const browser = await puppeteer.connect({ browserURL: 'http://localhost:9222' });
const page = await browser.newPage();
await page.goto('https://example.com');
console.log(await page.title());
```

# Persistent profiles (Docker manager)

The Docker `cloakbrowser-manager` stores profiles in the `cloak_profiles` volume, so logins/sessions survive restarts — useful for sites that need a stable identity.

# Headless vs headed

* `--headless=false` (launcher default) → visible Brave window you can watch.
* Omit/flip for headless automation (no UI).

# Typical agent flow

1. Launch `npx cloakbrowser --remote-debugging-port=9222 --headless=false`.
2. Agent connects via CDP (Playwright/Puppeteer) on :9222.
3. Navigate, interact, extract.
4. For logins, watch the visible window or use the Docker manager's persistent profile.

# Citations

[1] [Installation / ports](installation.md)
[2] [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)
