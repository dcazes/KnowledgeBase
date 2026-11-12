---
type: Reference
title: CloakBrowser Snippets
description: CloakBrowser code snippets — Python and JavaScript Playwright launch, Puppeteer import, and a protected-site configuration.
resource: https://github.com/CloakHQ/CloakBrowser
tags: [cloakbrowser, snippets, python, javascript, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: cloakbrowser-github
    resource: "https://github.com/CloakHQ/CloakBrowser"
    title: "CloakHQ/CloakBrowser on GitHub"
    author: "site:github.com"
---

# CloakBrowser — Snippets

```python
from cloakbrowser import launch
browser = launch()
page = browser.new_page()
page.goto("https://example.com")
print(page.title())
browser.close()
```

```javascript
import { launch } from "cloakbrowser";                 // Playwright API
// import { launch } from "cloakbrowser/puppeteer";    // Puppeteer API
const browser = await launch({ geoip: true, humanize: true });
const page = await browser.newPage();
await page.goto("https://example.com");
await browser.close();
```

```python
browser = launch(proxy="http://user:pass@residential-proxy:port",
                 geoip=True, headless=False, humanize=True)
```

## Related

[CloakBrowser index](index.md) · [Usage](usage.md)
