---
type: Reference
title: AnythingLLM
description: All-in-one local-first RAG chat app with workspaces and agent skills — documented as reference, not deployed on this machine.
resource: https://github.com/Mintplex-Labs/anything-llm
tags: [anythingllm, rag, chat, local-ai]
timestamp: 2026-08-12T00:00:00Z
---

# AnythingLLM

All-in-one local-first RAG chat app with workspaces and agent skills. Documented here as a **reference / available-to-deploy** app — not currently running on this machine (no deployment directory present).

## Contents

* [Overview](overview.md) - what AnythingLLM is, features
* [Installation](installation.md) - Docker deploy, setup
* [Workspaces](workspaces.md) - multi-workspace management
* [RAG & Embeddings](rag-embeddings.md) - document ingestion, vector stores
* [Agent Skills](agent-skills.md) - web-search, code, custom skills
* [AI Integration](ai-integration.md) - SearXNG, Firecrawl, Graphify
* [Alternatives](alternatives.md) - OpenWebUI, Dify, Chatbox
* [Snippets](snippets.md) - cheat sheet

## Instance facts

* **Status:** documented for reference; **not deployed** on this machine (no `programs/anythingllm/` directory, no running container).
* **URL (if deployed):** `http://localhost:3001` (or configured port)
* **Workspaces:** multiple (each with own RAG)
* **Skills:** web-search (SearXNG), code, API

## Cross-references

* **SearXNG** — web-search skill calls SearXNG — see [SearXNG AI Integration](../../runtime/searxng/ai-integration.md)
* **Firecrawl** — can use Firecrawl for extraction — see [Firecrawl AI Integration](../../browsers/firecrawl/ai-integration.md)
* **Graphify** — workspace docs can be graphed — see [Graphify AI Integration](../../memory/graphify/ai-integration.md)
* **Dify** — more advanced workflow platform — see [Dify AI Integration](../../agents/dify/ai-integration.md)
* **OpenWebUI** — lighter chat UI — see [OpenWebUI AI Integration](../openwebui/ai-integration.md)

## Last verified

**2026-08-12** — **v1.15.0** (2026-06-25, latest as of Aug 2026). Deployment, skills, and integration docs originally verified 2026-07-09.

# Citations

[1] [AnythingLLM GitHub](https://github.com/Mintplex-Labs/anything-llm)
[2] [AnythingLLM docs](https://docs.anythingllm.com/)