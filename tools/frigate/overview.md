---
type: Concept
title: Frigate Overview
description: How Frigate works — motion detection gating object detection, tracked objects and events, recording retention, review items and alerts, semantic search with embeddings, generative AI descriptions and chat, face and license-plate recognition, and supported detectors.
resource: https://docs.frigate.video
tags: [frigate, overview, object-detection, semantic-search]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: frigate-docs
    resource: "https://docs.frigate.video"
    title: "Frigate documentation"
    author: "site:docs.frigate.video"
  - id: frigate-018
    resource: "https://github.com/blakeblackshear/frigate/releases/tag/v0.18.0"
    title: "Frigate 0.18.0 release notes"
    author: "site:github.com"
---

# Frigate — Overview

## Pipeline

1. Decode camera streams (FFmpeg, hardware-accelerated).
2. **Motion detection** finds changed regions cheaply.
3. **Object detection** runs only on those regions with a detector model.
4. Objects are **tracked** across frames; events and review items (alerts, detections) are created.
5. Recordings and snapshots are stored per retention rules.

## Detectors

Google Coral (Edge TPU), Intel OpenVINO (CPU/iGPU/NPU), NVIDIA TensorRT, AMD ROCm, Hailo, Rockchip RKNN, Apple Silicon and ONNX models such as YOLO variants. DeGirum was removed in 0.18; DeepStack is deprecated.

## AI features beyond detection

| Feature | What it does |
|---|---|
| Semantic search | Embeds thumbnails and descriptions so you can search "red car in the driveway" — [Embeddings](../../concepts/embeddings.md) |
| GenAI descriptions | A vision-language model describes tracked objects and review items |
| GenAI chat (0.18) | Ask questions about camera activity |
| Remote embeddings (0.18) | Offload embedding models to another server |
| Face recognition, LPR, bird classification | Specialised enrichments |
| Motion search (0.18) | Find periods of motion in a drawn region |

## Related

[Frigate index](index.md) · [Configuration](configuration.md) · [AI Integration](ai-integration.md)
