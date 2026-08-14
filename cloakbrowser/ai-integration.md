---
type: Reference
title: CloakBrowser — AI Integration
description: CloakBrowser as a Chromium-based agent browser backend, and how it relates to Camofox and Firecrawl.
resource: https://github.com/cloakhq/cloakbrowser
tags: [cloakbrowser, integration, agents, cdp, camofox, firecrawl]
timestamp: 2026-07-09T01:13:00Z
---

# Agent browser backend (Chromium side)

CloakBrowser gives agents a **Brave/Chromium** browser they drive over CDP. When a task needs a Chromium engine (site compatibility, CDP tooling, persistent profiles), CloakBrowser is the pick — complementing **Camofox** (Firefox/Camoufox) and **Firecrawl** (Playwright-based bulk extraction).

```
Agent  ──CDP (:9222)──►  CloakBrowser (Brave)
                            │
                            ├─ headed window (watchable)
                            └─ persistent profiles (Docker manager)
```

# Relationship to the other browsers

| Need | Tool |
|------|------|
| Chromium automation, CDP, persistent profiles | **CloakBrowser** |
| Firefox anti-detection, watchable + VNC | **Camofox** |
| Bulk scrape/extract (Playwright render) | **Firecrawl** |

They're not redundant — each covers a different browser engine / stealth strategy.

# In the stack

The SearXNG compose listed `cloakbrowser-manager` as a service, signaling CloakBrowser is intended as a shared browser service other components can call (e.g. Firecrawl could use it for renders, though Firecrawl's own `playwright-service` is the default).

# Usage pattern

1. Launch `npx cloakbrowser --remote-debugging-port=9222 --headless=false`.
2. Agent connects via Playwright/Puppeteer on :9222.
3. For logins, use the visible window or the Docker manager's `cloak_profiles`.

# Citations

[1] [Overview](overview.md)
[2] [Usage (CDP)](usage.md)
[3] [Camofox (contrast)](/../../camofox/index.md)
[4] [Firecrawl (contrast)](/../../firecrawl/index.md)
