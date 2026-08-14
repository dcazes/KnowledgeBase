---
type: Reference
title: AnythingLLM — Workspaces
description: Isolated knowledge domains in AnythingLLM — each with its own vector store, prompts, agent skills, and chat history.
resource: https://docs.anythingllm.com/workspaces
tags: [anythingllm, workspaces, knowledge, isolation, multi-user]
generated: { by: "human:daniel", at: "2026-07-09T02:32:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T02:32:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: workspaces-docs
    resource: "https://docs.anythingllm.com/workspaces"
    title: "Workspaces docs"
    author: "site:docs.anythingllm.com"
  - id: overview
    resource: "overview.md"
    title: "Overview"
---

# What a workspace is

A **workspace** is an isolated knowledge domain. Each one keeps its own:
* **Vector index** (default LanceDB) — documents uploaded there stay separate.
* **System prompt** — workspace-specific instructions.
* **Agent skills** — which tools the agent may use.
* **Chat history** — separate per workspace.

This lets you separate, e.g., a "personal notes" workspace from a "project codebase" workspace from a "team docs" workspace, without cross-contamination.

# Creating a workspace

In the UI: **New Workspace** → name it → upload documents / set prompt / enable skills. Each workspace shows in the sidebar; switch to scope the chat to that knowledge.

# Multi-user

In Docker/multi-user mode, workspaces can be:
* **Private** — only you.
* **Shared** — visible to specific users/teams (admin-configured).

# Why it matters here

You can mirror parts of your `kbv2/` or `vault/` into a workspace for RAG chat, while keeping a separate workspace for, say, the `programs/*` source. SearXNG web search (see [AI Integration](ai-integration.md)) can augment any workspace.

# Tips

* Keep one workspace per distinct knowledge domain (don't dump everything into one).
* Set a tight system prompt per workspace for better answers.
* Enable only the agent skills a workspace needs (least privilege).
