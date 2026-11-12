---
type: Playbook
title: OpenConcho Installation
description: Install OpenConcho from release binaries, run the web app with pnpm, build the Tauri desktop app, or deploy the web image with Docker Compose or Helm.
resource: https://github.com/offendingcommit/openconcho
tags: [openconcho, installation, docker, helm, tauri]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openconcho-github
    resource: "https://github.com/offendingcommit/openconcho"
    title: "offendingcommit/openconcho on GitHub"
    author: "site:github.com"
---

# OpenConcho — Installation

## Binaries

Each GitHub release ships `.dmg` (Apple Silicon and Intel), `.deb` / `.AppImage` / `.rpm` and Windows `.exe` / `.msi`.

## Web app from source

Needs Node.js 22+ and pnpm 10 (`corepack enable`).

```bash
git clone https://github.com/offendingcommit/openconcho.git && cd openconcho
pnpm install
pnpm dev                                   # http://localhost:5173
pnpm --filter @openconcho/desktop dev      # desktop (needs Rust + Tauri prerequisites)
```

## Docker

The container serves the SPA and reverse-proxies the Honcho API under its own origin, so there is no CORS to configure.

```bash
OPENCONCHO_DEFAULT_HONCHO_URL=https://honcho.example.net make prod    # pull the published image
OPENCONCHO_DEFAULT_HONCHO_URL=https://honcho.example.net make up      # build locally
make down                                                             # → http://localhost:8080
```

## Helm

```bash
helm install openconcho oci://ghcr.io/offendingcommit/charts/openconcho \
  --create-namespace --namespace openconcho \
  --set honcho.defaultUrl=https://honcho.example.com
```

Add `ingress.*` values for an Ingress with TLS.

## Related

[OpenConcho index](index.md) · [Configuration](configuration.md) · [Honcho installation](../honcho/installation.md)
