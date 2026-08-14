---
type: HowTo
title: Supermemory Configuration
description: Configure Supermemory — local credentials (api-key/auth-secret/instance-id), encrypted env, local embedding model, pglite persistence.
resource: https://supermemory.ai
tags: [supermemory, configuration, local-first]
timestamp: 2026-08-13T00:00:00Z
---

# Configuration

Supermemory is **local-first by design** — configuration lives under `.supermemory/` and is largely opaque (encrypted/env-managed). What the layout tells us:

## Credentials

* `api-key` + `auth-secret` — local authentication material (mode 0600); generated at first launch.
* `instance-id` — unique per-install identifier (36 chars).
* `env.enc` — encrypted environment (210 bytes); contains API/service config the app needs (e.g. any cloud sync keys), encrypted at rest.

## Local inference

* `models/Xenova/` — local embedding model via **transformers.js (Xenova)**; embeddings are computed locally (no cloud embedding round-trip).
* `runtime/ort-web` + `ort-native` — **ONNX Runtime** variants: native binary for local execution, web build for embedded/in-browser fallback. These power the local model inference.

## Persistence

* `runtime/pglite/` — **PGlite**: Postgres compiled to WASM, run in-process; the app's relational store (pages, snippets, vectors, metadata) lives here.
* `data` — the memory store payload (~4.3 MB).

## Behavior notes

* Because env is encrypted and credentials are app-generated, there is **no hand-editable config file** — settings are managed in-app.
* `retry-params/` indicates the app persists failed-sync/queue state across restarts.

# Citations

[1] [Supermemory](https://supermemory.ai)
[2] [Supermemory GitHub](https://github.com/supermemoryai/supermemory)
