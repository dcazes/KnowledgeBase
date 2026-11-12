---
type: Playbook
title: CloakBrowser Installation
description: Install CloakBrowser for Python, Node (with playwright-core or puppeteer-core) or .NET, the GeoIP extra, first-run binary download and licence key, and the Docker self-test.
resource: https://github.com/CloakHQ/CloakBrowser
tags: [cloakbrowser, installation, pip, npm, docker]
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

# CloakBrowser — Installation

```bash
pip install cloakbrowser
pip install 'cloakbrowser[geoip]'                 # timezone/locale from proxy IP
npm install cloakbrowser playwright-core          # Playwright flavour
npm install cloakbrowser puppeteer-core           # Puppeteer flavour
dotnet add package CloakBrowser                   # community .NET client
```

On first launch the stealth Chromium (~200 MB) downloads and caches automatically, and you are asked for a licence key (free with an email address).

## Self-test in Docker

```bash
docker run --rm -it cloakhq/cloakbrowser cloaktest
```

## Related

[CloakBrowser index](index.md) · [Usage](usage.md)
