---
type: Software
title: CloakBrowser — Overview
description: A Brave/Chromium-based stealth and automation browser driven via CDP (port 9222), available as a Node CLI and a Docker manager service.
resource: https://github.com/cloakhq/cloakbrowser
tags: [cloakbrowser, browser, automation, cdp, brave, stealth, anti-detection]
timestamp: 2026-07-09T01:10:00Z
---

# What CloakBrowser is

CloakBrowser is a **browser automation / stealth tool** built on **Brave** (a Chromium fork). It exposes the **Chrome DevTools Protocol (CDP)** so agents and scripts can drive a real browser — navigate, click, read the DOM, take screenshots — while benefiting from Brave's privacy/anti-tracking defaults.

Two forms exist on this machine:

1. **Node CLI** — `npx cloakbrowser --remote-debugging-port=9222 --headless=false` (runs a local Brave instance with CDP on :9222).
2. **Docker manager** — `cloakhq/cloakbrowser-manager:latest` (a server form on :8080, with a `cloak_profiles` volume for persistent profiles).

# How it differs from Camofox

| | CloakBrowser | Camofox |
|--|--------------|---------|
| Browser base | **Brave / Chromium** | **Firefox / Camoufox** |
| Protocol | CDP (Chrome DevTools) | Playwright-compatible |
| Stealth approach | Brave anti-tracking + CDP control | Camoufox fingerprint spoofing |
| Watchable | headed (`--headless=false`) | headed + noVNC |

They're complementary: CloakBrowser for Chromium-based automation, Camofox for Firefox-based anti-detection.

# Where it fits

* Agent **browser backend** for Chromium-flavored automation.
* In the SearXNG compose it appeared as `cloakbrowser-manager` — a managed browser service other stack pieces can call.
* Good for tasks where a Chromium engine is required (site compatibility, CDP tooling).

# Citations

[1] [CloakBrowser (cloakhq)](https://github.com/cloakhq/cloakbrowser)
[2] [Local launcher](/../../programs/CloakBrowser.desktop)
[3] [CloakBrowser manager service (historical — former combined SearXNG compose, now defunct)](/../../programs/searxng/docker-compose.yml)
