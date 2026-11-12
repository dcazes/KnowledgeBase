---
type: Playbook
title: Camofox Installation
description: Install Camofox via npx, from source, with the Docker Makefile, or as an OpenClaw plugin; Camoufox binary download and air-gapped options.
resource: https://github.com/jo-inc/camofox-browser
tags: [camofox, installation, docker, npx, openclaw]
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

# Camofox — Installation

```bash
npx @askjo/camofox-browser                      # quickest; listens on :9377

git clone https://github.com/jo-inc/camofox-browser && cd camofox-browser
npm install && npm start                        # downloads Camoufox (~300 MB) on first run
```

## Docker

```bash
make up            # builds for your CPU arch, pre-downloads Camoufox and yt-dlp
make down | make reset | make fetch
make up ARCH=x86_64
```

Windows uses `build.ps1 up|down|build|reset|fetch`. Fly.io and Railway deployments are documented.

## OpenClaw plugin

```bash
openclaw plugins install @askjo/camofox-browser
```

## Custom or offline binaries

Set `CAMOUFOX_EXECUTABLE=/path/to/camoufox-bin` to use an existing Camoufox build, or install with `--ignore-scripts` to skip the automatic download.

## Related

[Camofox index](index.md) · [Usage](usage.md) · [OpenClaw](../../agents/openclaw/index.md)
