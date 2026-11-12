---
type: Concept
title: n8n Overview
description: "How n8n works — triggers and nodes, items and expressions, code nodes, sub-workflows, error handling and human approvals, plus its AI layer: the AI Agent node, chat models, memory, tools, vector stores, chains and evaluations."
resource: https://docs.n8n.io
tags: [n8n, overview, workflows, ai-agent]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: n8n-docs
    resource: "https://docs.n8n.io"
    title: "n8n documentation"
    author: "site:docs.n8n.io"
  - id: n8n-ai
    resource: "https://docs.n8n.io/advanced-ai/"
    title: "n8n advanced AI"
    author: "site:docs.n8n.io"
---

# n8n — Overview

## Workflows

A workflow starts from a **trigger** (webhook, schedule, app event, chat message, form, MCP call) and passes **items** through **nodes**. Expressions reference earlier data; **Code** nodes run JavaScript or Python; **sub-workflows** compose logic; error workflows and retries handle failures; **Wait** and approval steps add humans in the loop.

## AI layer (LangChain-based)

| Node family | Purpose |
|---|---|
| AI Agent | Tool-calling agent with a chat model, memory and tools |
| Chat models | OpenAI, Anthropic, Gemini, Mistral, [Ollama](../../runtime/ollama/index.md), OpenRouter, and OpenAI-compatible endpoints |
| Memory | Window buffer, Redis, Postgres, Zep and others ([Agent memory](../../concepts/agent-memory.md)) |
| Tools | Any n8n node or sub-workflow as a tool, HTTP, code, [MCP](../../concepts/mcp.md) client |
| Vector stores | [Qdrant](../../databases/qdrant/index.md), [pgvector](../../databases/pgvector/index.md), Pinecone, Supabase, in-memory ([RAG](../../concepts/rag.md)) |
| Chains | Summarisation, Q&A, information extraction, text classification |
| Evaluations | Test workflows against datasets ([Evals](../../concepts/evals.md)) |

The **MCP Server Trigger** exposes workflows as MCP tools to [Claude Code](../../agents/claude-code/index.md) and other clients.

## Strengths

The integration catalogue: agents can act on real systems (send mail, update CRMs, open tickets) without custom glue code.

## Related

[n8n index](index.md) · [Snippets](snippets.md) · [Workflow automation](../../concepts/workflow-automation.md)
