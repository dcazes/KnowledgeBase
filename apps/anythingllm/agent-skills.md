---
type: Reference
title: AnythingLLM — Agent Skills
description: AnythingLLM's agent tools (web search, browser, code, files, API, MCP) and how they connect to your stack (SearXNG, Graphify).
resource: https://docs.anythingllm.com/agent-skills
tags: [anythingllm, agents, skills, tools, mcp, web-search, playwright]
timestamp: 2026-07-09T02:34:00Z
---

# Agent skills

In agent mode, AnythingLLM can invoke **skills** (tools) during a conversation. Built-ins include:

| Skill | Purpose |
|-------|---------|
| **Web Search** | Query search engines — incl. **SearXNG**, DuckDuckGo, or custom |
| **Browser Automation** | Playwright for headed/headless scraping |
| **Code Execution** | Run Python/Node snippets safely |
| **File Operations** | Read/write/search local files |
| **Database Query** | SQL against connected DBs |
| **API Calls** | HTTP to external services |
| **MCP tools** | Any MCP server (e.g. **Graphify**) |

# Wiring SearXNG (web search)

Configure the Web Search skill to use your local SearXNG:
```
Provider: SearXNG
URL:      http://searxng:8080     # or http://localhost:8080
```
Now the agent pulls live web results (via your private metasearch) into answers.

# Wiring Graphify (MCP)

Add Graphify's MCP server so the agent can query your knowledge graph:
```
MCP server: graphify  (stdio: python -m graphify.serve)
```
The agent then calls Graphify tools for graph-backed retrieval.

# Browser automation

Playwright-based; can scrape pages the agent needs. (Same engine Firecrawl uses for rendering — but here it's AnythingLLM's own skill.)

# Custom skills

You can add your own tools (API/code) for domain tasks. Scope them per workspace.

# Citations

[1] [Agent skills docs](https://docs.anythingllm.com/agent-skills)
[2] [SearXNG integration](ai-integration.md)
[3] [Graphify MCP](/../../graphify/mcp-server.md)
[4] [Skills notes (prior, grounding)](/../../kb/anythingllm/agent-skills.md)
