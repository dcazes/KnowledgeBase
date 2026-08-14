---
type: Software
title: Camofox — Overview
description: A local browser server built on Camoufox (anti-detection Firefox fork) that gives AI agents a headed, stealthy browser with a watchable UI and VNC.
resource: https://github.com/daijro/camoufox
tags: [camofox, camoufox, browser, anti-detection, automation, hermes]
generated: { by: "human:daniel", at: "2026-07-09T01:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T01:00:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: camoufox-github
    resource: "https://github.com/daijro/camoufox"
    title: "Camoufox GitHub"
    author: "site:github.com"
  - id: local-launcher
    resource: "/../../programs/Camofox%20Launcher.desktop"
    title: "Local launcher"
  - id: local-launcher-programs-camofox-launcher-desktop
    resource: "/../../programs/Camofox%20Launcher.desktop"
    title: "Local launcher - programs/Camofox Launcher.desktop"
---

# What Camofox is

Camofox is a **local browser server** that wraps [Camoufox](https://github.com/daijro/camoufox) — a Firefox fork modified for **anti-detection fingerprint spoofing**. Where a normal automated browser announces "I'm a bot" through consistent, forged-looking fingerprints, Camoufox randomizes/spoofs them to look like a real user's browser.

It is the browser layer for agents: instead of a headless scrape that gets CAPTCHAd, the agent drives a real (Firefox-based) browser that resists fingerprinting — and you can watch it through a live window or a VNC viewer.

# Why it exists here

* **Anti-bot resilience** — spoofs fingerprints so sites (incl. Google CAPTCHA flows) are less likely to block it.
* **Watchable** — a headed browser you (and Hermes) can see; **VNC is opt-in** (`ENABLE_VNC=1`) and lets you do visual logins (e.g. OAuth screens Firecrawl can't solve).
* **Local & private** — runs on your machine via Docker; no third-party browser farm.

# How it relates to Camoufox vs Firefox

```
Firefox  ──(fork, anti-detection patches)──►  Camoufox  ──(server wrapper + API + VNC)──►  Camofox
```

Camoufox is the engine (Firefox fork, anti-detection patches at the C++ level); Camofox is the packaged, agent-facing server (Docker image `camofox-browser`). Engine dev has moved to CloverLabsAI (daijro/camoufox is the master copy); the server wrapper is jo-inc/camofox-browser v1.6.0 (active community fork redf0x1 v2.4.6).

# Where it fits in your stack

* **Hermes** uses Camofox as its **headed/anti-bot browser backend** (see [AI Integration](ai-integration.md)).
* Complements **Firecrawl** (which uses Playwright for rendering) — Camofox is the stealthy, human-watchable option for flows that need it.
* Distinct from **CloakBrowser** (separate stealth browser server — see its own KB page).
