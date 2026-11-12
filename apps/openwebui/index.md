---
type: Software
title: Open WebUI
description: Self-hosted, extensible AI chat platform for Ollama and any OpenAI-compatible API — multi-user with RBAC, built-in RAG and web search, tools, functions and pipelines, MCP and OpenAPI tool servers, voice, image generation and an API.
resource: https://github.com/open-webui/open-webui
tags: [open-webui, chat-ui, self-hosting, rag, ollama, multi-user]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openwebui-github
    resource: "https://github.com/open-webui/open-webui"
    title: "open-webui/open-webui on GitHub"
    author: "site:github.com"
  - id: openwebui-docs
    resource: "https://docs.openwebui.com"
    title: "Open WebUI documentation"
    author: "site:docs.openwebui.com"
---

# Open WebUI

**Open WebUI** is the most popular self-hosted ChatGPT-style interface. Point it at [Ollama](../../runtime/ollama/index.md), [vLLM](../../runtime/vllm/index.md), a [LiteLLM](../../runtime/litellm/index.md) gateway or hosted APIs, and give a household or team a private chat app with document Q&A, web search, tools and per-user permissions.

| | |
|---|---|
| Category | Chat UI · [RAG](../../concepts/rag.md) · [Self-hosting](../../concepts/self-hosting.md) |
| License | Open WebUI License (BSD-3-Clause based, with a branding-preservation clause) |
| Language | Python backend (FastAPI), Svelte front end |
| Latest release | v0.13.3 (2026-11-08) |
| Delivery | Docker (`:main`, `:slim`, `:cuda`, `:ollama`), pip/uvx, Kubernetes |

## Contents

* [Overview](overview.md) — what it is and how it is built
* [Features](features.md) — chat, RAG, search, tools, voice, images, admin
* [Installation](installation.md) — Docker images, Python, updates
* [Configuration](configuration.md) — connections, environment variables, auth
* [RAG](rag.md) — knowledge bases, document extraction, vector stores, web search
* [API](api.md) — OpenAI-compatible endpoints and API keys
* [Snippets](snippets.md) — run commands and API calls
* [AI Integration](ai-integration.md) — tools, MCP, pipelines, the wider stack

## Related

* Concepts: [RAG](../../concepts/rag.md) · [Local inference](../../concepts/local-inference.md) · [MCP](../../concepts/mcp.md)
* Peers: [AnythingLLM](../anythingllm/index.md), [SurfSense](../../browsers/surfsense/index.md), [LM Studio](../../runtime/lmstudio/index.md) (desktop)
* Comparison: [Apps alternatives](../alternatives.md)
