---
type: Playbook
title: CloakBrowser Usage
description: CloakBrowser launch options — proxy, geoip, headless versus headed, humanize, extensions — migrating from Playwright, and troubleshooting tougher anti-bot systems.
resource: https://github.com/CloakHQ/CloakBrowser
tags: [cloakbrowser, usage, proxy, humanize]
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

# CloakBrowser — Usage

## Migrating from Playwright

```diff
- from playwright.sync_api import sync_playwright
- browser = sync_playwright().start().chromium.launch()
+ from cloakbrowser import launch
+ browser = launch()
```

Everything after `launch()` is ordinary Playwright.

## Options for protected sites

| Option | Purpose |
|---|---|
| `proxy="http://user:pass@host:port"` or `socks5://…` | Residential IPs; datacentre IPs are flagged regardless of fingerprint |
| `geoip=True` | Match timezone, locale and WebRTC IP to the proxy |
| `headless=False` | Some systems still detect headless mode |
| `humanize=True` | Human-like input timing |
| `extension_paths=[...]` | Load Chrome extensions |

The project README has site-specific troubleshooting for Kasada, Akamai and reCAPTCHA.

## Related

[CloakBrowser index](index.md) · [Snippets](snippets.md)
