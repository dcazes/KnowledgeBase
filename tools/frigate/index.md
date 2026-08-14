---
type: Reference
title: Frigate
description: Open-source NVR with real-time AI object detection for IP cameras — go2rtc ingest, ONNX detector, GPU-accelerated.
resource: https://frigate.video/
tags: [frigate, nvr, surveillance, object-detection, camera, ai, onnx]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: frigate
    resource: "https://frigate.video/"
    title: "Frigate"
    author: "site:frigate.video"
  - id: docs-architecture
    resource: "https://docs.frigate.video/"
    title: "Docs — Architecture"
    author: "site:docs.frigate.video"
  - id: local-config
    resource: "/../../programs/frigate/config.yml"
    title: "Local config"
---

# Frigate

An open-source **NVR (Network Video Recorder)** designed for **real-time AI object detection** on IP cameras. It ingests camera streams (often via `go2rtc`), detects objects (people, vehicles, etc.) on-device, records, and serves a web UI — all self-hosted.

## Contents

* [Overview](overview.md) - what Frigate is, AI NVR model
* [Installation](installation.md) - Docker compose, ports, GPU, storage
* [Configuration](configuration.md) - `config.yml` anatomy, go2rtc, detectors, redacted secrets
* [Cameras](cameras.md) - Reolink camera, detect/record roles
* [AI Integration](ai-integration.md) - object detection, how it differs from the LLM stack
* [Alternatives](../alternatives.md) - ZoneMinder, Shinobi, Blue Iris, MotionEye
* [Snippets](snippets.md) - compose/ports/verify cheat sheet

## Instance facts (this machine, from `programs/frigate/`)

* **Version:** stable **0.17.2** (0.18.0 in beta — full UI config, FFmpeg 8, WebP-only snapshots)
* **Image:** `ghcr.io/blakeblackshear/frigate:stable`
* **Ports:** `8971` (Authenticated UI & API — TLS via reverse proxy), `5000` (Internal unauthenticated), `8554` (RTSP), `8555` (WebRTC tcp/udp)
* **GPU:** NVIDIA device reserved; `ffmpeg hwaccel_args: preset-nvidia`; detector `onnx` (TensorRT detector removed in 0.16.0; NVIDIA GPUs use the ONNX detector with CUDA Graphs since 0.17)
* **Camera:** Reolink (`reolink_camera`), fed via `go2rtc` HTTP-FLV from `192.168.68.61`
* **Storage:** `/media/daniel/New Volume/frigate` → `/media/frigate`
* **⚠️ Secrets:** camera + RTSP passwords are in `config.yml` **in plaintext** — keep them out of this KB (redacted).

## Cross-references

* **Docker** — Frigate runs via Docker Compose with GPU device reservation — see [Docker GPU & AI](../../runtime/docker/gpu-ai.md)
* **Graphify** — Frigate detection events could be ingested into a knowledge graph via MQTT/API (not yet wired) — see [Graphify AI Integration](../../memory/graphify/ai-integration.md)
* **Hermes** — could subscribe to Frigate MQTT or poll REST API for detection alerts — see [Hermes AI Integration](../../agents/hermes/ai-integration.md)

## Last verified

**2026-08-12** — All compose ports, GPU config, go2rtc wiring, and camera config verified against local `programs/frigate/config.yml` and `docker-compose.yml`. Stable 0.17.2; ONNX detector (TensorRT removed in 0.16.0).
