---
type: Reference
title: OpenWebUI — Features (Plugins, Tools, Agents, Skills, MCP)
description: OpenWebUI's extension model — Functions (Filters/Actions), Pipes, Tools, Skills, and MCP/OpenAPI tool servers.
resource: https://docs.openwebui.com/features/plugin/
tags: [openwebui, plugins, tools, skills, agents, mcp, pipes, functions]
generated: { by: "human:daniel", at: "2026-07-09T02:04:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T02:04:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: plugin-features-docs
    resource: "https://docs.openwebui.com/features/plugin/"
    title: "Plugin/Features docs"
    author: "site:docs.openwebui.com"
  - id: overview-plugin-support
    resource: "overview.md"
    title: "Overview (plugin support)"
  - id: firecrawl-mcp-integration
    resource: "/../../firecrawl/ai-integration.md"
    title: "Firecrawl MCP/integration"
---

# OpenWebUI — Extension model

OpenWebUI is extensible through several building blocks:

* **Functions** — Python snippets that hook the request/response lifecycle:
  * **Filters** — transform input/output (moderation, logging, rewriting).
  * **Actions** — trigger side effects (post to a webhook, save artifacts).
* **Pipes** — custom model routers/gateways that appear as a model in the picker (e.g. load-balance across providers, or wrap a chain).
* **Tools** — let the model call external functions (search, calculators, APIs).
* **Skills** — reusable prompt/behavior packs the model can invoke.

# External tool servers

OpenWebUI connects to external capabilities via:
* **MCP** — Model Context Protocol servers (the same protocol Firecrawl/SearXNG/etc. can expose).
* **MCPO** — an MCP-to-OpenAPI proxy.
* **OpenAPI** — any OpenAPI-spec tool server.

This means tools already documented in this KB (Firecrawl, Graphify's MCP) can be surfaced to OpenWebUI's models.

# Agents

Wrap any base model with custom instructions + tools + knowledge to build a specialized agent. Supports:
* Dynamic variables (`{{user.name}}`, etc.).
* Per-user/group access control.
* Community preset imports via Open WebUI Community.

# Persistent artifact storage

A built-in key-value storage API lets tools persist data (journals, trackers, leaderboards) with personal/shared scopes.

# Practical use here

* Expose **Firecrawl** and **SearXNG** search as Tools/MCP so chats can pull live web context on demand.
* Add a **Graphify** MCP server so a chat can query your knowledge graph.
* Use a Pipe to route chats through the `:4000` proxy with fallback logic.
