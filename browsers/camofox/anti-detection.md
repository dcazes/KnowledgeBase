---
type: Concept
title: Camofox Anti-Detection
description: How Camoufox resists bot detection — spoofing navigator, WebGL, AudioContext, screen and WebRTC values inside Firefox's C++ code rather than with JavaScript stealth patches — plus limits and responsible use.
resource: https://camoufox.com
tags: [camofox, camoufox, anti-detection, fingerprinting]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: camoufox-github
    resource: "https://github.com/daijro/camoufox"
    title: "daijro/camoufox on GitHub"
    author: "site:github.com"
  - id: camoufox-site
    resource: "https://camoufox.com"
    title: "Camoufox documentation"
    author: "site:camoufox.com"
---

# Camofox — Anti-Detection

## Why stealth plugins fail

Classic stealth plugins patch browser APIs from JavaScript after the page loads. Detection scripts can notice the patches themselves — "stealth plugins become the fingerprint".

## Camoufox's approach

Camoufox modifies Firefox **at the C++ implementation level**, so spoofed values (`navigator.hardwareConcurrency`, WebGL renderer strings, AudioContext output, screen geometry, fonts, WebRTC addresses) are what the engine genuinely reports before any page JavaScript runs. Fingerprints are generated to be internally consistent and match real-world device distributions.

## Practical limits

* IP reputation still matters: datacentre IPs are flagged regardless of fingerprint; residential proxies with matching GeoIP help.
* Behaviour matters: superhuman click speed and navigation patterns are detectable.
* Firefox has a smaller market share than Chrome, which some systems weigh — [CloakBrowser](../cloakbrowser/index.md) applies the same idea to Chromium.

> Use anti-detection browsers only where you are allowed to automate: your own sites, sites whose terms permit it, or authorised testing. Bypassing access controls can breach terms of service or law.

## Related

[Camofox index](index.md) · [CloakBrowser](../cloakbrowser/index.md) · [Agent security](../../concepts/agent-security.md)
