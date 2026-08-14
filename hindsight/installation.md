---
type: HowTo
title: Hindsight Installation
description: Install Hindsight — Rust CLI (hindsight), Python API (uv), npm @vectorize-io/hindsight-all, or control-plane deploy (Docker/Helm) from the v0.8.4 checkout; verify with version/status.
resource: https://hindsight.vectorize.io
tags: [hindsight, installation, cli, docker, helm]
timestamp: 2026-08-13T00:00:00Z
---

# Installation

## 1. CLI (Rust)

```bash
# Build the CLI from the checkout (hindsight-cli/ Cargo.toml, bin name `hindsight`)
cd programs/hindsight/hindsight-cli
cargo build --release          # -> target/release/hindsight

# npm-available builds: @vectorize-io/hindsight-all (hindsight-all-npm/)
```

## 2. API + control plane (server deploy)

The repo ships `docker/` and `helm/` manifests; the control plane is a Next.js app (`@vectorize-io/hindsight-control-plane`, `hindsight-control-plane/`):

```bash
cd programs/hindsight/docker
# build/run per README — API + control-plane services
# or Helm chart for Kubernetes (helm/ dir)
```

## Verify

```bash
hindsight --version          # 0.8.4 (if CLI installed)
# or API probe once deployed:
curl -s http://localhost:PORT/health   # per service docs
```

## Status on this machine

* `programs/hindsight` checkout present (v0.8.4) — **not deployed**, no running services (recon 2026-08-12).

# Citations

[1] [Hindsight docs — installation](https://hindsight.vectorize.io)
[2] [Hindsight GitHub](https://github.com/vectorize-io/hindsight)
