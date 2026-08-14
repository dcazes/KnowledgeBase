---
type: Reference
title: Frigate — AI Integration
description: Frigate's role as a computer-vision object detector vs the LLM/agent stack; optional pathways to feed detections into agents.
resource: https://docs.frigate.video/
tags: [frigate, ai, object-detection, computer-vision, integration, mqtt]
generated: { by: "human:daniel", at: "2026-07-09T04:19:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:19:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: frigate
    resource: "https://frigate.video/"
    title: "Frigate"
    author: "site:frigate.video"
  - id: api-docs
    resource: "https://docs.frigate.video/"
    title: "API/docs"
    author: "site:docs.frigate.video"
  - id: overview
    resource: "overview.md"
    title: "Overview"
---

# What "AI" means here

Frigate's AI is **computer-vision object detection** (people, cars, pets…) — not an LLM. It runs an ONNX model on your GPU (the TensorRT detector was removed in 0.16.0; NVIDIA GPUs use the ONNX detector with CUDA Graphs since 0.17). This is a different AI family than the LLM/agent tools in the rest of the stack.

# Outputs

* **Events** — detection clips/snapshots.
* **MQTT** — can publish detection state (disabled in this config: `mqtt.enabled: false`).
* **API/UI** — live view, recordings, REST API.

# Connecting to the agent stack (optional, not wired)

| Path | How |
|------|-----|
| MQTT → agent | enable `mqtt`, subscribe from an agent (Hermes/OpenCode) |
| API → agent | poll Frigate REST API from a skill |
| Detections → RAG | store events as notes in the Obsidian vault / Graphify |

None of these are configured here yet — Frigate runs standalone as surveillance.

# Distinction

| Tool | AI type |
|------|---------|
| **Frigate** | CV object detection (GPU) |
| OpenWebUI / Dify / Hermes | LLM reasoning/agents |
| Graphify | knowledge graph |
