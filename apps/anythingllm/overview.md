---
type: Concept
title: AnythingLLM Overview
description: AnythingLLM's design — desktop versus Docker editions, built-in LLM engine, embedder and LanceDB vector store, provider flexibility, dynamic model routing, memories, scheduled tasks, white-labeling and the developer API.
resource: https://docs.anythingllm.com
tags: [anythingllm, overview, editions]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: anythingllm-docs
    resource: "https://docs.anythingllm.com"
    title: "AnythingLLM documentation"
    author: "site:docs.anythingllm.com"
  - id: anythingllm-github
    resource: "https://github.com/Mintplex-Labs/anything-llm"
    title: "Mintplex-Labs/anything-llm on GitHub"
    author: "site:github.com"
---

# AnythingLLM — Overview

| | Desktop | Docker |
|---|---|---|
| Users | Single | Multi-user with permissions |
| Embeddable chat widget | No | Yes |
| Typical use | Personal knowledge assistant | Team or customer-facing deployments |

## Built-in defaults

* **LLM engine** for local models on CPU or GPU (NVIDIA via CUDA, AMD and Intel via Vulkan) — or connect [Ollama](../../runtime/ollama/index.md), [LM Studio](../../runtime/lmstudio/index.md) and 30+ hosted providers.
* **Embedder** running locally; **LanceDB** vector store embedded — see [RAG & embeddings](rag-embeddings.md).

## 2026 features

* **Dynamic model routing** — rules send each chat to the best provider/model.
* **Memories** — automatic and user-managed ([Agent memory](../../concepts/agent-memory.md)).
* **Scheduled tasks** — cron-scheduled prompts with full agent capabilities.
* **Intelligent skill selection** — many tools available while cutting tool-schema tokens.
* **No-code agent flows**, [MCP](../../concepts/mcp.md) compatibility, custom agents.
* White-labeling and themes; full developer API.

## Related

[AnythingLLM index](index.md) · [Workspaces](workspaces.md)
