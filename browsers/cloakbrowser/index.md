---
type: Reference
title: CloakBrowser
description: A Chromium-based Playwright/Puppeteer drop-in wrapper (Python + JS) for agent browser automation — not a standalone CDP server.
resource: https://github.com/cloakhq/cloakbrowser
tags: [cloakbrowser, browser, automation, chromium, playwright, puppeteer, stealth, anti-detection]
timestamp: 2026-08-12T00:00:00Z
---

# CloakBrowser

A **stealth / automation browser tool** built on **Chromium** (not Brave). It is a **Playwright/Puppeteer drop-in wrapper (Python + JS)** — not a standalone CDP server on `:9222`. Two forms on this machine: a Node CLI (`npx cloakbrowser`) and a Docker "manager" service (`cloakhq/cloakbrowser-manager`, :8080). It's the Chromium-based counterpart to Camofox for agent browsing/automation.

## Contents

* [Overview](overview.md) - what CloakBrowser is, Chromium base, Playwright/Puppeteer wrapper, how it differs from Camofox
* [Installation](installation.md) - the desktop launcher / `npx` CLI, the Docker manager, ports
* [Usage](usage.md) - driving via Playwright/Puppeteer, profiles, agent automation
* [AI Integration](ai-integration.md) - agent browser backend, relation to Camofox & Firecrawl
* [Alternatives](alternatives.md) - Camofox, Playwright, Puppeteer, Undetected-Chromedriver
* [Snippets](snippets.md) - copy-paste cheat sheet

## Instance facts (from local launcher + compose)

* **Version:** v0.5.7 (2026-08-11), Chromium 150. Free tier ships an older Chromium v146 build; the latest build requires a free GitHub-sign-in key (1 session) or paid Pro.
* **CLI launcher:** `npx cloakbrowser --remote-debugging-port=9222 --headless=false`
* **Docker service:** `cloakhq/cloakbrowser-manager:latest`, port `8080`, volume `cloak_profiles`
* **Base:** Chromium (not Firefox — distinct from Camofox)

## Cross-references

* **Camofox** — Firefox-based alternative with anti-detection — see [Camofox Overview](../camofox/overview.md)
* **Firecrawl** — Firecrawl's playwright-service provides similar rendering — see [Firecrawl Subservices](../firecrawl/subservices/playwright-service.md)
* **Hermes** — can use CloakBrowser via CDP — see [Hermes Browser](../../agents/hermes/browser.md)
* **Graphify** — can ingest CloakBrowser-crawled pages — see [Graphify AI Integration](../../memory/graphify/ai-integration.md)
* **SearXNG** — SearXNG compose includes cloakbrowser-manager — see [SearXNG Installation](../../runtime/searxng/installation.md)

## Last verified

**2026-08-12** — CLI command, Docker service, ports, and Chromium base verified against local launcher. v0.5.7 (Chromium 150); Playwright/Puppeteer drop-in wrapper (not a standalone CDP server).

# Citations

[1] [Local launcher - programs/CloakBrowser.desktop](/../../programs/CloakBrowser.desktop)
[2] [CloakBrowser manager service (historical — former combined SearXNG compose, now defunct)](/../../programs/searxng/docker-compose.yml)