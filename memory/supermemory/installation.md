---
type: HowTo
title: Supermemory Installation
description: Install Supermemory — desktop app from supermemory.ai; what the local .supermemory/ layout tells us; no source checkout on this machine.
resource: https://supermemory.ai
tags: [supermemory, installation, desktop]
timestamp: 2026-08-13T00:00:00Z
---

# Installation

## Desktop app

Download the app for your OS from [supermemory.ai](https://supermemory.ai) (Windows/macOS/Linux builds) and run the installer. First launch provisions the local data directory.

## What the local `.supermemory/` shows

`programs/supermemory/.supermemory/` (permissions `drwx------`, created 2026-07-19, data written 2026-07-20):

| Entry | Meaning |
|---|---|
| `api-key`, `auth-secret` | local auth credentials (0600) |
| `instance-id` | unique install id |
| `env.enc` | encrypted environment blob |
| `models/Xenova/` | bundled local embedding model (Xenova/transformers.js) |
| `runtime/pglite/` | embedded Postgres (PGlite) data dir |
| `runtime/ort-web`, `ort-native/` | ONNX Runtime (web + native) — local inference engine |
| `data` | ~4.3 MB memory store blob |
| `retry-params/` | retry state from a prior run |

## Status on this machine

* Installed + run 2026-07-19/20; **no source checkout** (unlike the git-checkout programs), **not currently running** (no process/container observed in recon 2026-08-12).

# Citations

[1] [Supermemory](https://supermemory.ai)
[2] [Supermemory GitHub](https://github.com/supermemoryai/supermemory)
