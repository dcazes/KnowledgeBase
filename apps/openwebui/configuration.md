---
type: Reference
title: Open WebUI Configuration
description: Key Open WebUI settings — Ollama and OpenAI-compatible connections, secret key and auth, signup and default roles, OAuth/OIDC, database and Redis for scaling, vector store and web search, and the persistent-config behaviour of the admin UI.
resource: https://docs.openwebui.com/getting-started/env-configuration
tags: [open-webui, configuration, env, oauth]
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

# Open WebUI — Configuration

| Variable | Purpose |
|---|---|
| `OLLAMA_BASE_URL` | Ollama endpoint(s) |
| `OPENAI_API_BASE_URL(S)`, `OPENAI_API_KEY(S)` | OpenAI-compatible connections ([LiteLLM](../../runtime/litellm/index.md), [vLLM](../../runtime/vllm/index.md), hosted APIs) |
| `WEBUI_SECRET_KEY` | Session signing — set a fixed value |
| `ENABLE_SIGNUP`, `DEFAULT_USER_ROLE` | Control who can join and with what role |
| `ENABLE_OAUTH_SIGNUP`, `OPENID_PROVIDER_URL`, … | SSO (e.g. Tailscale's tsidp, Authentik, Keycloak) |
| `DATABASE_URL` | PostgreSQL instead of SQLite |
| `REDIS_URL`, `WEBSOCKET_MANAGER` | Multi-instance deployments |
| `VECTOR_DB` | `chroma` (default), `qdrant`, `pgvector`, `milvus`, `opensearch`, … |
| `RAG_EMBEDDING_ENGINE`, `RAG_EMBEDDING_MODEL` | Embedding model ([Embeddings](../../concepts/embeddings.md)) |
| `ENABLE_WEB_SEARCH`, `WEB_SEARCH_ENGINE`, `SEARXNG_QUERY_URL` | Web search |

Many settings are stored in the database after first start and then edited in *Admin → Settings*; environment variables marked "persistent config" only apply on first launch unless you reset them.

## Related

[Open WebUI index](index.md) · [RAG](rag.md)
