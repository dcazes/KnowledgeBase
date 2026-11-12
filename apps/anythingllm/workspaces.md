---
type: Concept
title: AnythingLLM Workspaces
description: AnythingLLM workspaces — isolated containers of documents, settings and chat history, per-workspace models and prompts, chat versus query modes, memories, and user access.
resource: https://docs.anythingllm.com
tags: [anythingllm, workspaces, chat-modes]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: anythingllm-docs
    resource: "https://docs.anythingllm.com"
    title: "AnythingLLM documentation"
    author: "site:docs.anythingllm.com"
---

# AnythingLLM — Workspaces

A **workspace** is like a project: its own documents, embeddings, system prompt, model choice and chat history. Documents can be shared across workspaces without re-embedding.

| Setting | Effect |
|---|---|
| Chat mode | Uses the model's knowledge plus retrieved documents |
| Query mode | Answers only from documents; says so when nothing is found — reduces hallucination |
| Model override | Different LLM per workspace (or via model routing) |
| Similarity threshold, top-N | Retrieval tuning |
| Memories | Facts the assistant keeps about you or the workspace |

In the Docker edition, admins assign users to workspaces.

## Related

[AnythingLLM index](index.md) · [RAG & embeddings](rag-embeddings.md)
