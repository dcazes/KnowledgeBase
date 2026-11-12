---
type: Concept
title: AnythingLLM Agent Skills
description: AnythingLLM agents — @agent invocation, built-in skills (web browsing and search, scraping, document and file tools, charts, SQL), custom JavaScript skills, no-code agent flows, MCP servers, and scheduled tasks.
resource: https://docs.anythingllm.com/agent/overview
tags: [anythingllm, agents, skills, mcp, agent-flows]
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

# AnythingLLM — Agent Skills

Type `@agent` in a workspace chat to hand the turn to an agent with tools.

* **Built-in skills:** web search (including [SearXNG](../../runtime/searxng/index.md)), web scraping, RAG search, save files, summarise documents, generate charts, SQL queries.
* **Custom skills:** small JavaScript packages with a manifest, installed per instance or from the community hub.
* **Agent flows:** a no-code builder for multi-step agent workflows.
* **MCP:** connect [MCP](../../concepts/mcp.md) servers to add tools such as [Playwright MCP](../../browsers/playwright-mcp/index.md) or [Graphify](../../memory/graphify/mcp-server.md).
* **Intelligent skill selection** keeps many tools available without sending every schema each turn — a [context engineering](../../concepts/context-engineering.md) optimisation.
* **Scheduled tasks** run agent prompts on a cron.

Agents need a model with reliable [tool calling](../../concepts/tool-calling.md).

## Related

[AnythingLLM index](index.md) · [AI Integration](ai-integration.md)
