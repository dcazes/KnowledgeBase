---
type: Playbook
title: Frigate AI Integration
description: Frigate's generative-AI and automation integrations — local vision-language models via Ollama or OpenAI-compatible servers, Gemini and OpenAI providers, semantic search, Home Assistant and MQTT automations, and n8n workflows.
resource: https://docs.frigate.video/configuration/genai
tags: [frigate, integration, genai, ollama, home-assistant]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: frigate-docs
    resource: "https://docs.frigate.video"
    title: "Frigate documentation"
    author: "site:docs.frigate.video"
---

# Frigate — AI Integration

* **GenAI providers:** [Ollama](../../runtime/ollama/index.md) (fully local, e.g. a Qwen-VL or Gemma vision model), Gemini, OpenAI, Azure, or any [OpenAI-compatible](../../concepts/openai-compatible-api.md) server such as [vLLM](../../runtime/vllm/index.md). Assign roles per provider — a small local model for descriptions, a stronger one for chat.
* **Semantic search** uses local embedding models (or remote embeddings in 0.18) — see [Embeddings](../../concepts/embeddings.md).
* **Home Assistant:** the Frigate integration exposes cameras, sensors and events for automations and notifications.
* **MQTT / webhooks → [n8n](../../apps/n8n/index.md):** trigger workflows that summarise a day's events with an LLM or open tickets.
* **Privacy:** keep inference local and the UI on a private network ([Tailscale](../../runtime/tailscale/index.md)); cloud providers receive frames you send them.

## Related

[Frigate index](index.md) · [Local inference](../../concepts/local-inference.md)
