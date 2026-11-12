---
type: Concept
title: Dify Overview
description: Dify's app types (chatbot, agent, workflow, chatflow, text generator) and features — visual workflows, hundreds of models, prompt IDE, RAG, sandboxed agents, LLMOps, backend-as-a-service APIs, plugins and app packages.
resource: https://docs.dify.ai
tags: [dify, overview, app-types, features]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: dify-github
    resource: "https://github.com/langgenius/dify"
    title: "langgenius/dify on GitHub"
    author: "site:github.com"
  - id: dify-docs
    resource: "https://docs.dify.ai"
    title: "Dify documentation"
    author: "site:docs.dify.ai"
---

# Dify — Overview

## App types

| Type | Use |
|---|---|
| Chatbot / Chatflow | Conversational apps; chatflow adds a workflow canvas with memory |
| Agent | Autonomous tool-using agent, now with its own sandbox |
| Workflow | Single-run automations (batch, triggers, APIs) |
| Text generator | One-shot generation from a form |

## Key features

* **Visual workflow** canvas with LLM, knowledge retrieval, code, HTTP, iteration, loop, condition and tool nodes.
* **Models:** hundreds of hosted and self-hosted models via provider plugins ([Model providers](model-providers.md)).
* **Prompt IDE** for comparing prompts and models.
* **RAG pipeline** from ingestion to retrieval ([RAG pipeline](rag-pipeline.md)).
* **Agents** that run commands and handle files in a sandbox ([Workflows & agents](workflows-agents.md)).
* **LLMOps:** logs, annotations, nested workflow tracing to external observability tools.
* **Backend-as-a-service:** every app has an API ([API](api.md)).
* **Plugins and app packages:** marketplace plugins for models, tools and agent strategies; apps export as portable packages; `difyctl` CLI and OpenAPI (1.18+).

## Recent releases

* **1.19** — nested workflow tracing to observability tools, portable Workflow Tools, Skill Hub automation.
* **1.18** — agents that route workflows, app packages, Agent Knowledge Base, `difyctl`.
* **1.17.1** — bundled Weaviate upgraded 1.27 → 1.39 (requires a staged manual upgrade on existing installs).

## Related

[Dify index](index.md) · [Architecture](architecture.md)
