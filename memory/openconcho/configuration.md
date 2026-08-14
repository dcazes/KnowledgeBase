---
type: HowTo
title: OpenConcho Configuration
description: Configure OpenConcho — Honcho instance URLs/keys, multiple-instance switching, browser-only storage, default port.
resource: https://github.com/offendingcommit/openconcho
tags: [openconcho, configuration, honcho]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: openconcho-github-readme
    resource: "https://github.com/offendingcommit/openconcho"
    title: "OpenConcho GitHub — README"
    author: "site:github.com"
---

# Configuration

## Honcho connections

* **Instances** — add one or more Honcho URLs; each stores its connection details **in the browser** (localStorage), per the privacy model.
* **Switching** — toggle between instances from the UI; the fleet dashboard shows all at once with per-instance badges.

## What you provide per instance

```text
- Honcho server URL (e.g. http://localhost:8000)
- Auth/keys if your Honcho deployment requires them
```

## No server-side config

OpenConcho is a static UI — no backend database of its own; all state is the Honcho server's state plus browser-side connection info.

## Ports

Web/dev server port follows the npm/dev config (checkout default per package scripts); Docker compose maps per the compose file.

> Not deployed on this machine (2026-08-13) — no running instance to point at Honcho.
