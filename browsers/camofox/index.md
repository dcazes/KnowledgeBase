---
type: Reference
title: Camofox
description: A local browser server built on Camoufox (anti-detection Firefox fork) that gives AI agents a headed, stealthy browser with a watchable UI and opt-in VNC.
resource: https://github.com/daijro/camoufox
tags: [camofox, camoufox, browser, anti-detection, automation, hermes]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: camoufox-upstream
    resource: "https://github.com/daijro/camoufox"
    title: "Camoufox (upstream)"
    author: "site:github.com"
  - id: local-launcher-programs-camofox-launcher-desktop
    resource: "/../../programs/Camofox%20Launcher.desktop"
    title: "Local launcher - programs/Camofox Launcher.desktop"
---

# Camofox

A **local browser server** powered by [Camoufox](https://github.com/daijro/camoufox) — a Firefox fork with anti-detection fingerprint spoofing. Gives AI agents a headed, anti-bot browser they can drive and you can watch (live window + VNC). On this machine it's Hermes's browser backend.

## Contents

* [Overview](overview.md) - what Camofox/Camoufox is and why
* [Installation](installation.md) - build/launch via make, the Docker image, ports
* [Usage](usage.md) - API on :9377, noVNC on :6080, driving the browser
* [Anti-Detection](anti-detection.md) - fingerprint spoofing, captcha handling
* [AI Integration](ai-integration.md) - Hermes browser backend, agent automation
* [Alternatives](alternatives.md) - Playwright, Puppeteer, Camoufox raw, Undetected-Chromedriver
* [Snippets](snippets.md) - copy-paste cheat sheet

## Instance facts (from local launcher + vault notes)

* **Upstream:** jo-inc/camofox-browser **v1.6.0** (server wrapper, MIT); active community fork **redf0x1 v2.4.6**; Camoufox engine dev moved to CloverLabsAI (daijro/camoufox is the master copy).
* **Launch:** `sudo make -C /home/daniel/Documents/camofox-browser up`
* **Repo:** `/home/daniel/Documents/camofox-browser` (also `/home/daniel/Documents/Camox`)
* **Image:** `camofox-browser:135.0.1-x86_64`
* **Ports:** `9377` (API/control), `6080` (noVNC viewer — **opt-in**, only when `ENABLE_VNC=1`)
* **Deployment:** standalone `docker run` (no compose)
* **Status:** currently **exited (crash, exit 255)** — see local launcher
* **Role:** Hermes's headed/anti-bot browser backend (live window + VNC for visual logins)

## Cross-references

* **Hermes** — primary consumer; Hermes uses Camofox as its browser backend — see [Hermes Browser](../../agents/hermes/browser.md)
* **CloakBrowser** — alternative stealth browser (Chromium-based, CDP) — see [CloakBrowser Overview](../cloakbrowser/overview.md)
* **Firecrawl** — Firecrawl's playwright-service provides similar rendering — see [Firecrawl Subservices](../firecrawl/subservices/playwright-service.md)
* **Graphify** — can ingest Camofox-crawled pages — see [Graphify AI Integration](../../memory/graphify/ai-integration.md)

## Last verified

**2026-08-12** — Launch command, image tag, ports, and Hermes integration verified against local launcher and upstream Camoufox docs. jo-inc v1.6.0; VNC opt-in via ENABLE_VNC=1; currently exited (crash).
