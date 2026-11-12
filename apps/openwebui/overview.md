---
type: Concept
title: Open WebUI Overview
description: What Open WebUI is — a provider-agnostic chat front end and backend with users, groups and permissions, knowledge and tools, built on FastAPI and Svelte with SQLite or PostgreSQL storage.
resource: https://docs.openwebui.com
tags: [open-webui, overview, architecture]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openwebui-docs
    resource: "https://docs.openwebui.com"
    title: "Open WebUI documentation"
    author: "site:docs.openwebui.com"
---

# Open WebUI — Overview

* **Provider-agnostic.** Native Ollama connection plus any number of [OpenAI-compatible](../../concepts/openai-compatible-api.md) connections; models from all of them appear in one picker.
* **Multi-user.** Admin, users, groups and role-based access to models, knowledge and tools; SSO via OAuth/OIDC, LDAP or trusted headers.
* **Batteries included.** RAG, web search, code execution, image generation, speech in and out — each can use local or external services.
* **Extensible.** Tools and Functions (Python plugins), Pipelines (a separate server for heavier middleware), and external tool servers over [MCP](../../concepts/mcp.md) or OpenAPI.

## Architecture

FastAPI backend with SQLite by default (PostgreSQL for production), a built-in vector store (ChromaDB by default; Qdrant, pgvector, Milvus, OpenSearch and others selectable), optional Redis for multi-instance deployments, and a Svelte single-page app. The `:slim` image delegates embeddings, extraction and voice to external services.

## Related

[Open WebUI index](index.md) · [Features](features.md) · [Configuration](configuration.md)
