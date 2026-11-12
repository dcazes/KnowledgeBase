---
type: Playbook
title: SurfSense Installation
description: Install SurfSense with the desktop installers for Windows, macOS and Linux, or self-host the Docker server with the official install script.
resource: https://github.com/MODSetter/SurfSense
tags: [surfsense, installation, desktop, docker]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: surfsense-github
    resource: "https://github.com/MODSetter/SurfSense"
    title: "MODSetter/SurfSense on GitHub"
    author: "site:github.com"
  - id: surfsense-site
    resource: "https://www.surfsense.com"
    title: "SurfSense website"
    author: "site:surfsense.com"
---

# SurfSense — Installation

## Desktop

Download from surfsense.com: `SurfSense-Setup.exe` (Windows x64), `SurfSense-arm64.dmg` (macOS Apple Silicon), AppImage or `.deb` (Linux x64). Complete onboarding, choose a model, then add files or folders as sources.

## Docker (server on your network)

```bash
curl -fsSL https://raw.githubusercontent.com/MODSetter/SurfSense/main/docker/scripts/install.sh | bash   # Linux, macOS
irm https://raw.githubusercontent.com/MODSetter/SurfSense/main/docker/scripts/install.ps1 | iex          # Windows
```

Run the same command again to update. Read install scripts before piping them to a shell, and keep the server on a private network such as [Tailscale](../../runtime/tailscale/index.md).

## Related

[SurfSense index](index.md) · [Docker](../../runtime/docker/index.md)
