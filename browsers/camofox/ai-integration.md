---
type: Reference
title: Camofox — AI Integration
description: Camofox as Hermes's headed/anti-bot browser backend, and how it complements Firecrawl and CloakBrowser.
resource: https://github.com/daijro/camoufox
tags: [camofox, hermes, integration, browser, automation, agent]
generated: { by: "human:daniel", at: "2026-07-09T01:04:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T01:04:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: camofox-overview
    resource: "overview.md"
    title: "Camofox overview"
  - id: usage-api-vnc
    resource: "usage.md"
    title: "Usage (API + VNC)"
  - id: firecrawl-contrast
    resource: "/../../firecrawl/index.md"
    title: "Firecrawl (contrast)"
---

# Camofox — Hermes browser backend

Camofox is wired as **Hermes's headed/anti-bot browser backend**. When Hermes needs to browse a site that blocks headless scrapers, it drives Camofox instead of a plain Playwright browser — gaining fingerprint spoofing and a watchable window.

```
Hermes  ──drives──►  Camofox API (:9377)
                        │
                        ├─ headed Firefox (spoofed fingerprint)
                        └─ noVNC (:6080)  ← you watch / solve CAPTCHAs
```

# Why not just Firecrawl?

* **Firecrawl** uses Playwright for rendering and is great for bulk scrape/extract — but a plain Playwright browser is more detectable and has no live human-view window.
* **Camofox** is the stealthy, watchable option for flows that need to *look human* or require a visual login.

They're complementary: Firecrawl for scale/extract, Camofox for fragile/anti-bot sessions.

# Relationship to CloakBrowser

**CloakBrowser** is a separate stealth browser server in your stack (its own KB page). Camofox and CloakBrowser are distinct tools; both provide browser-stealth capabilities but are independent services. In the earlier SearXNG compose, `cloakbrowser-manager` appeared as a service — that's CloakBrowser, not Camofox.

# Usage pattern

1. `make up` Camofox.
2. Hermes opens a Camofox session via `:9377`, navigates, interacts.
3. On a login/CAPTCHA, you open `:6080` and complete it.
4. Hermes reads the result and continues.
