---
type: Software
title: browser-use
description: Open-source browser agent library — the model drives a real Chrome by writing Python against CDP in a persistent REPL (v1.0, built on Pydantic AI), with typed results, secrets handling, domain restrictions, custom tools, a CLI skill and a hosted cloud.
resource: https://github.com/browser-use/browser-use
tags: [browser-use, browser-automation, agents, cdp, python, pydantic-ai]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: browser-use-github
    resource: "https://github.com/browser-use/browser-use"
    title: "browser-use/browser-use on GitHub"
    author: "site:github.com"
  - id: browser-use-docs
    resource: "https://docs.browser-use.com"
    title: "Browser Use documentation"
    author: "site:docs.browser-use.com"
  - id: browser-use-migrating
    resource: "https://github.com/browser-use/browser-use/blob/main/MIGRATING.md"
    title: "Migrating from 0.x"
    author: "site:github.com"
---

# browser-use

**browser-use** gives an LLM a real browser and a task — "find the earliest driving-test slot and book it" — and lets it work until done. Version 1.0 (late 2026) reduced the agent to its essentials: *the model, a persistent Python REPL, and the Chrome DevTools Protocol*. The model writes code cells (`new_tab(url)`, `bu.click(41)`) that run against the browser and sees the output.

| | |
|---|---|
| Category | [Browser automation](../../concepts/browser-automation.md) · [Agent frameworks](../../concepts/agent-frameworks.md) |
| License | MIT |
| Language | Python 3.11+ (`browser-use`), built on [PydanticAI](../../agents/pydanticAI/index.md) |
| Latest release | 1.0.3 (2026-11-12) |
| Modes | Python library · CLI + agent skill · Browser Use Cloud (hosted agent and stealth browsers) |

## Contents

* [Overview](overview.md) — the REPL + CDP design, browsers, features
* [Installation](installation.md) — library, CLI skill, cloud
* [Snippets](snippets.md) — local browser with your model, typed output, secrets, tools
* [AI Integration](ai-integration.md) — inside coding agents, frameworks and safety

## Related

* Concepts: [Browser automation](../../concepts/browser-automation.md) · [Agent security](../../concepts/agent-security.md) · [Tool calling](../../concepts/tool-calling.md)
* Peers: [Playwright MCP](../playwright-mcp/index.md), [Camofox](../camofox/index.md), [CloakBrowser](../cloakbrowser/index.md), [Firecrawl](../firecrawl/index.md) interact
* Comparison: [Browser & web alternatives](../alternatives.md)
