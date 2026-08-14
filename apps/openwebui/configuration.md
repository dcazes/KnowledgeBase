---
type: Reference
title: OpenWebUI — Configuration (Models & Proxy)
description: Connecting OpenWebUI to an OpenAI-compatible endpoint — here, the local :4000 proxy — since no Ollama runs on this host.
resource: https://docs.openwebui.com/getting-started/openai-api/
tags: [openwebui, configuration, models, openai-compatible, proxy, openrouter]
generated: { by: "human:daniel", at: "2026-07-09T02:02:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T02:02:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: openai-api-connection-docs
    resource: "https://docs.openwebui.com/getting-started/openai-api/"
    title: "OpenAI API connection (docs)"
    author: "site:docs.openwebui.com"
  - id: installation-proxy-fit
    resource: "installation.md"
    title: "Installation / proxy fit"
---

# The situation on this machine

OpenWebUI's `:ollama` image *expects* an Ollama server. **There is no Ollama on this host.** Inference is provided by the local **`:4000` OpenAI-compatible proxy** (OpenRouter/NIM failover). So you connect OpenWebUI as an **OpenAI-compatible** provider, not Ollama.

# Add an OpenAI-compatible connection

In the UI: **Settings → Connections → Manage OpenAI API Connections** (or Admin Settings → Models):
```
Type:            OpenAI-compatible
Base URL:        http://localhost:4000/v1
API Key:         <value the :4000 proxy accepts>
Model:           <model exposed by the proxy, e.g. a free model>
```
Save, then the model appears in the model picker.

> The `/v1` suffix matters — OpenWebUI appends `/chat/completions`, `/models`, etc. to the Base URL.

# Why not Ollama here

* No `ollama` is configured in this stack (only `open-webui`, Firecrawl, SearXNG are part of the design); the GTX 1060 6GB can't run large local models well, so cloud models via the proxy are the practical path.
* The GTX 1060 6GB can't run large local models well; cloud models via the proxy are the practical path.
* If you later add Ollama, point OpenWebUI at `http://host.docker.internal:11434` (or `--network=host` → `http://localhost:11434`).

# Multi-provider mixing

OpenWebUI can hold several connections at once (OpenRouter via proxy, plus an optional Ollama). Switch per-chat in the model dropdown.

# Tips

* Use a proxy API key that the `:4000` service accepts (it may accept any non-empty string).
* Set a default model in Admin Settings so new chats work immediately.
* For embeddings/RAG, configure an embedding model endpoint too (if your proxy exposes one).
