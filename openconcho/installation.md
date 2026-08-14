---
type: HowTo
title: OpenConcho Installation
description: Install OpenConcho — GitHub release binaries (v0.16.1) or build from source (pnpm), docker-compose/Helm from checkout; verify against a Honcho URL.
resource: https://github.com/offendingcommit/openconcho
tags: [openconcho, installation, releases, docker, helm]
timestamp: 2026-08-13T00:00:00Z
---

# Installation

There is **no npm package** (`openconcho` 404s on the npm registry — verified 2026-08-13). Distribution is via GitHub Releases (desktop binaries), building from source, or Docker/Helm.

## 1. Desktop (release binaries)

Grab the latest release (**v0.16.1** as of 2026-08-13) from GitHub Releases — macOS / Linux / Windows binaries per the README "Latest release" badge.

## 2. From source (pnpm)

```bash
cd programs/openconcho        # v0.16.0 checkout
pnpm install && pnpm dev      # web UI in dev mode
```

## 3. Docker / Helm

The checkout ships `docker-compose.yml` (+ `charts/` for Helm, published at `ghcr.io/offendingcommit/charts`):

```bash
cd programs/openconcho
docker compose up -d          # serves the web UI
```

## Verify

1. Launch the app.
2. Add your Honcho connection (URL + keys) under *Instances*.
3. Dashboard shows workspace count + queue status (auto-refresh 10 s) — success means it reached Honcho.

## Status on this machine

* `programs/openconcho` checkout present (v0.16.0) — **not deployed** (recon 2026-08-12); [Honcho](../honcho/index.md) is also not running, so there's nothing to connect to yet.

# Citations

[1] [OpenConcho GitHub — README](https://github.com/offendingcommit/openconcho)
[2] [OpenConcho GitHub Releases](https://github.com/offendingcommit/openconcho/releases)
