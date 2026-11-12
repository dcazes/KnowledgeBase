---
type: Software
title: n8n
description: Fair-code workflow automation platform with native AI — a visual canvas plus JavaScript/Python code, 1,500+ integrations, AI agent and LangChain-based nodes, vector stores, MCP client and server triggers, human approvals, and self-hosting with Docker.
resource: https://n8n.io
tags: [n8n, workflow-automation, ai-agents, low-code, self-hosting, typescript]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: n8n-github
    resource: "https://github.com/n8n-io/n8n"
    title: "n8n-io/n8n on GitHub"
    author: "site:github.com"
  - id: n8n-docs
    resource: "https://docs.n8n.io"
    title: "n8n documentation"
    author: "site:docs.n8n.io"
  - id: n8n-ai
    resource: "https://docs.n8n.io/advanced-ai/"
    title: "n8n advanced AI"
    author: "site:docs.n8n.io"
---

# n8n

**n8n** ("nodemation") connects apps and APIs with visual workflows and has become a leading place to build practical AI agents: an AI Agent node with tools, memory and any model, wired to 1,500+ integrations (email, Slack, CRMs, databases, webhooks). It is self-hostable and source-available.

| | |
|---|---|
| Category | [Workflow automation](../../concepts/workflow-automation.md) · [Agent frameworks](../../concepts/agent-frameworks.md) |
| License | Sustainable Use License (fair-code, source-available) + n8n Enterprise License |
| Language | TypeScript |
| Latest release | n8n@2.47.5 (2026-11-12) |
| Deployment | Docker / npm self-hosted · n8n Cloud |

## Contents

* [Overview](overview.md) — workflows, triggers, nodes, AI capabilities
* [Installation](installation.md) — Docker, Compose with Postgres, npm
* [Snippets](snippets.md) — webhook-triggered AI agent, API calls, code nodes
* [AI Integration](ai-integration.md) — models, vector stores, MCP, memory, the wider stack

## Related

* Concepts: [Workflow automation](../../concepts/workflow-automation.md) · [Tool calling](../../concepts/tool-calling.md) · [MCP](../../concepts/mcp.md) · [RAG](../../concepts/rag.md)
* Peers: [Dify](../../agents/dify/index.md), [LangGraph](../../agents/langgraph/index.md), [CrewAI](../../agents/crewai/index.md)
* Comparison: [Apps alternatives](../alternatives.md)
