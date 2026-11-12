---
type: Concept
title: Camofox Overview
description: What Camofox provides on top of Camoufox — token-efficient accessibility snapshots, element refs, search macros, sessions, cookie import, uploads and downloads, proxy with GeoIP, VNC login, structured extraction, tracing and low idle memory.
resource: https://github.com/jo-inc/camofox-browser
tags: [camofox, overview, snapshots, element-refs]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: camofox-github
    resource: "https://github.com/jo-inc/camofox-browser"
    title: "jo-inc/camofox-browser on GitHub"
    author: "site:github.com"
---

# Camofox — Overview

## Two layers

* **Camoufox** (by daijro) — a Firefox fork whose fingerprint surfaces are patched in C++ (see [Anti-detection](anti-detection.md)).
* **camofox-browser** (by the Jo team) — a Node server that launches Camoufox through Playwright and exposes an agent-friendly REST API.

## Features

| Feature | Why it helps agents |
|---|---|
| Accessibility snapshots | ~90% smaller than HTML — fewer tokens per page |
| Stable element refs | `click e12` instead of brittle CSS selectors |
| Search macros | `@google_search`, `@youtube_search`, `@amazon_search`, `@reddit_subreddit` and more |
| Session isolation | Separate cookies and storage per user or task |
| Cookie / storage import | Reuse authenticated sessions (Netscape cookie files, storage state) |
| VNC interactive login | Log in by hand via noVNC once, export state for the agent |
| Proxy + GeoIP | Route through proxies with matching locale and timezone |
| Structured extract | JSON Schema whose properties map to snapshot refs (`x-ref`) |
| Uploads, downloads, screenshots, YouTube transcripts | Common agent chores without extra tools |
| Session tracing | Opt-in Playwright traces for debugging |
| Lazy launch, idle shutdown | ~40 MB idle — fits on a Raspberry Pi or small VPS |

Large pages are truncated with offset-based pagination. Note that it sends anonymised crash and hang telemetry by default; review the settings.

## Related

[Camofox index](index.md) · [Usage](usage.md) · [Browser automation](../../concepts/browser-automation.md)
