---
type: Software
title: Frigate — Overview
description: Open-source NVR with real-time AI object detection for IP cameras — go2rtc ingest, ONNX detector, GPU-accelerated.
resource: https://frigate.video/
tags: [frigate, nvr, surveillance, object-detection, camera, ai, onnx]
generated: { by: "human:daniel", at: "2026-07-09T04:15:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:15:00Z" } ]
status: stable
stale_after: 2027-01-05
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

# What Frigate is

Frigate is an open-source **NVR (Network Video Recorder)** designed for **real-time AI object detection** on IP cameras. It ingests camera streams (often via `go2rtc`), detects objects (people, vehicles, etc.) on-device, records, and serves a web UI — all self-hosted.

# How it works

```
Camera (RTSP/HTTP-FLV)
   │  go2rtc (restream/stabilize)
   ▼
Frigate ── detector (ONNX) ── objects
   ├─ record (continuous/events)
       ├─ snapshots
       └─ Web UI (:8971 authenticated, TLS via reverse proxy) + RTSP restream (:8554) + WebRTC (:8555)
```

# Why it matters

* **Local & private** — your footage never leaves your hardware.
* **AI detection** — runs inference on CPU/GPU (here: NVIDIA + ONNX).* **go2rtc** — stabilizes flaky camera streams (Reolink over HTTP-FLV).
* **Rich UI** — live view, events, recordings, masks/zones.

# How it fits your stack

Frigate is the **surveillance** layer — separate from the LLM/agent tools, but part of `programs/`. It's not an LLM; it's computer-vision object detection. (You could later feed detections into agents, but that's not wired here.)

# Notes

* Camera credentials live in `config.yml` **in plaintext** — never copy them into this KB.
* GPU helps detection/decoding throughput.
