---
type: Concept
title: CloakBrowser Overview
description: How CloakBrowser works — source-level Chromium fingerprint patches, humanized input, proxy signal removal, WebRTC IP spoofing, GeoIP matching, and the licence-key model introduced in 2026.
resource: https://github.com/CloakHQ/CloakBrowser
tags: [cloakbrowser, overview, fingerprinting, humanize]
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

# CloakBrowser — Overview

## What is patched

Canvas, WebGL, audio, fonts, GPU and screen parameters, WebRTC, network timing, automation signals and CDP input behaviour — inside Chromium's C++ source, so detection scripts see a consistent, ordinary browser. On Windows, real GPU values are passed through rather than spoofed.

## Behaviour

`humanize=True` adds human-like mouse curves, typing rhythm and scrolling, and waits for elements to be visible and stable before acting. Per-call `human_config` overrides tune it.

## Network

* HTTP (with inline credentials) and native SOCKS5 proxies, including QUIC over SOCKS5.
* Proxy tell-tales removed (timing, cache headers, `Proxy-Connection`).
* `geoip=True` matches timezone and locale to the proxy's exit IP and spoofs WebRTC ICE candidates accordingly.

## Licensing

Since 2026 every launch needs a licence key: a free key by email, or a paid Pro key for the newest builds and higher scale. The first interactive launch prompts for one; set it via `license_key` / the environment for automation. Factor this into self-hosted, offline or CI use.

> Use anti-detection browsers only where you are allowed to automate: your own sites, sites whose terms permit it, or authorised testing. Bypassing access controls can breach terms of service or law.

## Related

[CloakBrowser index](index.md) · [Usage](usage.md) · [Camofox anti-detection](../camofox/anti-detection.md)
