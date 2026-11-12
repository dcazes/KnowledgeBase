---
type: Software
title: Frigate
description: Open-source network video recorder with real-time local AI object detection for IP cameras — hardware-accelerated detectors (Coral, OpenVINO, TensorRT, ROCm, Hailo, RKNN), review and semantic search, multi-provider generative AI descriptions and chat, face and plate recognition, and Home Assistant integration.
resource: https://frigate.video
tags: [frigate, nvr, computer-vision, object-detection, home-assistant, genai]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: frigate-github
    resource: "https://github.com/blakeblackshear/frigate"
    title: "blakeblackshear/frigate on GitHub"
    author: "site:github.com"
  - id: frigate-docs
    resource: "https://docs.frigate.video"
    title: "Frigate documentation"
    author: "site:docs.frigate.video"
  - id: frigate-018
    resource: "https://github.com/blakeblackshear/frigate/releases/tag/v0.18.0"
    title: "Frigate 0.18.0 release notes"
    author: "site:github.com"
---

# Frigate

**Frigate** turns a small server into a private, AI-powered security camera system. It records your cameras and runs object detection **locally** on each frame region where motion occurs, so you get alerts for people, cars or animals without sending video to the cloud. In 2025–2026 it gained vision-language features: generated descriptions of events, semantic search over footage, and (in 0.18) chat over your camera history.

| | |
|---|---|
| Category | Computer vision · [Local inference](../../concepts/local-inference.md) · [Self-hosting](../../concepts/self-hosting.md) |
| License | MIT |
| Language | Python, TypeScript UI |
| Latest release | v0.18.2 (2026-10-15) |
| Images | `ghcr.io/blakeblackshear/frigate` — standard, `-tensorrt`, `-rocm`, `-rk`, `-tensorrt-jp6`, `-synaptics`, arm64 |

## Contents

* [Overview](overview.md) — pipeline, detectors, review, GenAI
* [Installation](installation.md) — Docker Compose, hardware
* [Configuration](configuration.md) — config.yml essentials, 0.18 changes
* [Cameras](cameras.md) — streams, go2rtc, zones and masks
* [Snippets](snippets.md) — config fragments and API calls
* [AI Integration](ai-integration.md) — GenAI providers, Ollama, Home Assistant, MQTT

## Related

* Concepts: [Local inference](../../concepts/local-inference.md) · [Embeddings](../../concepts/embeddings.md) · [Self-hosting](../../concepts/self-hosting.md)
* Runs on: [Docker](../../runtime/docker/index.md) (GPU: [Docker GPU & AI](../../runtime/docker/gpu-ai.md)); GenAI via [Ollama](../../runtime/ollama/index.md)
* Comparison: [Tools alternatives](../alternatives.md)
