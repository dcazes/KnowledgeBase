---
type: Concept
title: Model Context Protocol (MCP)
description: The Model Context Protocol — an open standard for connecting AI applications to tools, data and prompts — covering hosts, clients and servers, tools, resources and prompts, stdio and Streamable HTTP transports, authorization, the 2026 spec, security risks, and the MCP servers and clients in this vault.
resource: https://modelcontextprotocol.io
tags: [concept, mcp, protocol, tools, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: mcp-spec
    resource: "https://modelcontextprotocol.io/specification"
    title: "Model Context Protocol specification"
    author: "site:modelcontextprotocol.io"
  - id: mcp-github
    resource: "https://github.com/modelcontextprotocol/modelcontextprotocol"
    title: "modelcontextprotocol/modelcontextprotocol"
    author: "site:github.com"
---

# Model Context Protocol (MCP)

**MCP** is an open protocol, introduced by Anthropic in late 2024 and now governed as an open standard with broad industry adoption, that standardises how AI applications connect to external tools and data. Write a tool server once; any MCP client — coding agents, chat apps, IDEs — can use it. It is the "USB-C for AI tools" and the most-linked concept in this vault.

## Architecture

* **Host** — the AI application (e.g. [Claude Code](../agents/claude-code/index.md), [Cursor](../editors/cursor/index.md), [Open WebUI](../apps/openwebui/index.md)).
* **Client** — a connection inside the host to one server.
* **Server** — exposes capabilities:
  * **Tools** — functions the model can call ([Tool calling](tool-calling.md)).
  * **Resources** — readable data (files, records).
  * **Prompts** — reusable templates.
* **Transports** — **stdio** for local processes; **Streamable HTTP** for remote servers (with OAuth-based authorization). The specification is versioned by date; the latest release is 2026-07-28.

## Servers documented here

| Server | Gives agents |
|---|---|
| [Playwright MCP](../browsers/playwright-mcp/index.md), [Camofox](../browsers/camofox/index.md) | A browser |
| [Firecrawl](../browsers/firecrawl/ai-integration.md), [Crawl4AI](../browsers/crawl4ai/ai-integration.md) | Web scraping and search |
| [Graphiti](../memory/graphiti/mcp-server.md), [Graphify](../memory/graphify/mcp-server.md), [Hindsight](../memory/hindsight/snippets.md), [Honcho](../memory/honcho/ai-integration.md), [Supermemory](../memory/supermemory/snippets.md), [Cognee](../memory/cognee/ai-integration.md) | Memory and knowledge graphs |
| [Docling](../ingestion/docling/ai-integration.md), [MarkItDown](../ingestion/markitdown/ai-integration.md) | Document reading |
| [Qdrant](../databases/qdrant/ai-integration.md), [Neo4j](../databases/neo4j/ai-integration.md) | Databases |
| [n8n](../apps/n8n/ai-integration.md), [Dify](../agents/dify/workflows-agents.md) | Workflows as tools |

Gateways: [Docker MCP Gateway](../runtime/docker/gpu-ai.md#mcp-toolkit-and-gateway), [LiteLLM](../runtime/litellm/overview.md).

## Costs and risks

* **Context cost** — every tool schema consumes tokens; many servers can crowd out the task. Skills or CLIs are sometimes leaner ([Playwright MCP vs CLI](../browsers/playwright-mcp/overview.md)).
* **Security** — servers run code with your permissions; tool descriptions and results can carry prompt injection; reference servers often lack auth ([Graphiti MCP](../memory/graphiti/mcp-server.md)). See [Agent security](agent-security.md).

## Related

[A2A](a2a.md) (agent-to-agent) · [Agent skills](agent-skills.md) · [Tool calling](tool-calling.md) · [Concepts index](index.md)
