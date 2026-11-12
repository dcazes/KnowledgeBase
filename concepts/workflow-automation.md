---
type: Concept
title: Workflow Automation
description: Workflows versus agents — deterministic pipelines with LLM steps, visual builders, triggers, human approvals and integrations — and how n8n, Dify, LangGraph and CI tools combine automation with agentic decisions.
resource: https://docs.n8n.io/advanced-ai/
tags: [concept, workflow-automation, low-code, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: n8n-ai
    resource: "https://docs.n8n.io/advanced-ai/"
    title: "n8n advanced AI"
    author: "site:docs.n8n.io"
  - id: dify-docs
    resource: "https://docs.dify.ai"
    title: "Dify documentation"
    author: "site:docs.dify.ai"
---

# Workflow Automation

A **workflow** is a predefined sequence of steps; an **agent** decides its own steps. Most reliable AI systems are workflows with a few agentic decisions inside: classify this email, extract these fields, draft a reply — then route, store and notify deterministically.

## Building blocks

* **Triggers:** webhooks, schedules, app events, chat messages, MCP calls.
* **LLM steps:** generation, classification, extraction with [structured output](structured-output.md), retrieval ([RAG](rag.md)).
* **Agent steps:** a bounded agent with tools for open-ended sub-tasks.
* **Control flow:** branches, loops, retries, error handlers, **human approvals**.
* **Integrations:** email, chat, CRMs, databases, ticketing.

## Tools in this vault

| Tool | Strength |
|---|---|
| [n8n](../apps/n8n/index.md) | 1,500+ integrations, AI Agent node, MCP in and out |
| [Dify](../agents/dify/index.md) | LLM-centric canvas, RAG, app APIs |
| [LangGraph](../agents/langgraph/index.md) | Code-first graphs with durability and interrupts |
| [CrewAI Flows](../agents/crewai/overview.md) | Event-driven control around crews |
| [Codex](../agents/codex/snippets.md) `exec`, [Claude Code](../agents/claude-code/snippets.md) `-p` | Agents as steps in CI pipelines |

## Related

[Agent frameworks](agent-frameworks.md) · [Tool calling](tool-calling.md) · [Apps alternatives](../apps/alternatives.md) · [Concepts index](index.md)
