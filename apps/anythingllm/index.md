---
type: Software
title: AnythingLLM
description: All-in-one, local-first AI application for chatting with documents and running agents — desktop and Docker editions, workspaces, built-in LLM engine, model routing, memories, scheduled tasks, no-code agent flows, MCP, multi-user permissions and an embeddable chat widget.
resource: https://github.com/Mintplex-Labs/anything-llm
tags: [anythingllm, rag, chat-ui, agents, desktop, local-first]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: anythingllm-github
    resource: "https://github.com/Mintplex-Labs/anything-llm"
    title: "Mintplex-Labs/anything-llm on GitHub"
    author: "site:github.com"
  - id: anythingllm-docs
    resource: "https://docs.anythingllm.com"
    title: "AnythingLLM documentation"
    author: "site:docs.anythingllm.com"
---

# AnythingLLM

**AnythingLLM** packages a private ChatGPT with document RAG and agents into one app that works out of the box: install the desktop app (or run the Docker server for teams), drop in documents, pick a local or cloud model, and start chatting. Its built-in defaults — local LLM engine, embedder and vector store — mean no separate infrastructure is required.

| | |
|---|---|
| Category | [RAG](../../concepts/rag.md) app · chat UI · agents |
| License | MIT |
| Language | JavaScript (Node server, React front end) |
| Latest release | v1.19.0 (2026-10-26) |
| Editions | Desktop (macOS, Windows, Linux) · Docker (multi-user) · Android app · hosted |

## Contents

* [Overview](overview.md) — editions, architecture, defaults
* [Workspaces](workspaces.md) — isolation, chat modes, memories
* [RAG & embeddings](rag-embeddings.md) — ingestion, embedders, vector stores
* [Agent skills](agent-skills.md) — agents, flows, MCP, scheduled tasks
* [Installation](installation.md) — desktop and Docker
* [Snippets](snippets.md) — developer API
* [AI Integration](ai-integration.md) — models, routing, the wider stack

## Related

* Concepts: [RAG](../../concepts/rag.md) · [Vector databases](../../concepts/vector-databases.md) · [MCP](../../concepts/mcp.md)
* Peers: [Open WebUI](../openwebui/index.md), [SurfSense](../../browsers/surfsense/index.md), [Dify](../../agents/dify/index.md)
* Comparison: [Apps alternatives](../alternatives.md)
