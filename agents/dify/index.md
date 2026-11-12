---
type: Software
title: Dify
description: Open-source LLM application platform with a visual workflow canvas, RAG knowledge pipelines, sandboxed autonomous agents, a plugin marketplace for models and tools, MCP support, LLMOps observability and APIs for every app. Self-hosted with Docker Compose or Dify Cloud.
resource: https://github.com/langgenius/dify
tags: [dify, low-code, workflows, rag, agents, llmops, python]
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
  - id: dify-releases
    resource: "https://github.com/langgenius/dify/releases"
    title: "Dify release notes"
    author: "site:github.com"
---

# Dify

**Dify** is the most widely used open-source platform for building LLM apps visually: chatbots, workflows, RAG assistants and agents are assembled on a canvas, tested in a prompt IDE, monitored in production, and exposed through APIs. It is the low-code counterpart to code-first frameworks like [LangGraph](../langgraph/index.md).

| | |
|---|---|
| Category | [Workflow automation](../../concepts/workflow-automation.md) · [RAG](../../concepts/rag.md) · [Agent frameworks](../../concepts/agent-frameworks.md) |
| License | Dify Open Source License (Apache-2.0 with additional conditions on multi-tenant SaaS use and branding) |
| Language | Python (API, workers), TypeScript (web) |
| Latest release | 1.19.0 (2026-11-04) |
| Deployment | Docker Compose (min 2 CPU, 4 GB RAM) · Kubernetes (community Helm) · Dify Cloud |

## Contents

* [Overview](overview.md) — app types and key features
* [Architecture](architecture.md) — services in the stack
* [Installation](installation.md) — Docker Compose, upgrades
* [Model providers](model-providers.md) — plugins for hosted and local models
* [RAG pipeline](rag-pipeline.md) — knowledge bases and pipelines
* [Workflows & agents](workflows-agents.md) — nodes, agent strategies, sandboxed agents
* [API](api.md) — app and knowledge APIs
* [Snippets](snippets.md) — curl examples
* [AI Integration](ai-integration.md) — MCP, observability, memory, the wider stack

## Related

* Concepts: [Workflow automation](../../concepts/workflow-automation.md) · [RAG](../../concepts/rag.md) · [LLM observability](../../concepts/llm-observability.md)
* Peers: [n8n](../../apps/n8n/index.md), [AnythingLLM](../../apps/anythingllm/index.md), [Open WebUI](../../apps/openwebui/index.md), [LangGraph](../langgraph/index.md)
* Comparison: [Agents alternatives](../alternatives.md)
