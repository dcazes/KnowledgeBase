---
type: Reference
title: Camofox — Anti-Detection
description: How Camoufox spoofs browser fingerprints to resist bot detection, and the limits (CAPTCHAs still need human/VNC help).
resource: https://github.com/daijro/camoufox
tags: [camofox, anti-detection, fingerprint, captcha, stealth, privacy]
generated: { by: "human:daniel", at: "2026-07-09T01:03:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T01:03:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: camoufox-anti-detection-github
    resource: "https://github.com/daijro/camoufox"
    title: "Camoufox anti-detection (GitHub)"
    author: "site:github.com"
  - id: local-launcher-programs-camofox-launcher-desktop
    resource: "/../../programs/Camofox%20Launcher.desktop"
    title: "Local launcher - programs/Camofox Launcher.desktop"
---

# Camofox — The problem Camoufox solves

Automated browsers leak "bot-ness" through dozens of signals: a consistent UA string, missing/forged `navigator` properties, WebGL/Canvas fingerprints that never vary, automation flags (`navigator.webdriver`), and impossible timing. Sites (and their CAPTCHA providers) fingerprint these and block or challenge the client.

# How Camoufox helps

Camoufox is a **Firefox fork** with anti-detection patches:

* **Fingerprint spoofing** — randomized but internally-consistent fingerprints (screen, timezone, fonts, WebGL/Canvas, etc.) so the browser looks like a real user's.
* **No automation flags** — removes/cleans the tells Playwright/ Selenium normally set (e.g. `navigator.webdriver`).
* **Firefox base** — a different fingerprint surface than Chromium, widening coverage.
* **Consistency** — within a session, the spoofed values stay coherent (no contradiction that betrays a bot).

# What it does NOT solve

* **Hard CAPTCHAs** — when a site still challenges, a human steps in via **noVNC (:6080)** to solve it (see [Usage](usage.md)).
* **Behavioral analysis** — super-fast/robotic interaction timing can still trip heuristics; pace actions.
* **IP reputation** — Camofox spoofs the client, not your IP. Pair with a proxy if IP blocking is the issue (separate concern).

# Best practices

* Keep one session per "identity" — don't reuse a spoofed fingerprint across unrelated tasks.
* Use the VNC view for any login that needs a human.
* Don't crank speed; mimic human pacing.
* Treat it as stealth, not invisibility.
