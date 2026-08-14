---
type: Reference
title: VSCode — AI Features
description: VS Code's AI capabilities — GitHub Copilot, Agent Mode, chat, and MCP server integration.
resource: https://code.visualstudio.com/docs/copilot/overview
tags: [vscode, ai, copilot, agent-mode, chat, mcp]
timestamp: 2026-07-09T02:12:00Z
---

# AI in VS Code

VS Code has become an **AI-first editor**. Core AI surfaces:

* **GitHub Copilot** — inline completions, chat, and edits (requires a Copilot subscription/key).
* **Agent Mode** — the model plans and executes multi-step edits across files, runs terminals, and iterates. Manage **multi-agent workflows** across environments (per the official site).
* **Copilot Chat** — ask about code, generate, explain, fix.
* **Edits / Apply** — apply diffs the model proposes.

# MCP integration

VS Code can connect to **MCP servers** (the same protocol used by Firecrawl/Graphify in this KB). Configure via `.vscode/mcp.json` or user settings:

```json
{
  "servers": {
    "graphify": { "type": "stdio", "command": "python", "args": ["-m", "graphify.serve"] }
  }
}
```
Once registered, the agent/model can call those tools from chat/agent mode.

# Why it matters here

* You can drive **Graphify** (build a knowledge graph from a repo) and **Firecrawl** (scrape) directly from the editor via MCP.
* Agent Mode + your `programs/*` repos = an AI pair-programmer that edits Dify/Firecrawl/SearXNG code with context.

# Notes

* Copilot needs a GitHub account + license; the *editor* itself is free/OSS.
* MCP tool availability depends on what servers you register.
* Telemetry: VS Code (MS build) sends usage data; VSCodium/Code-OSS do not.

# Citations

[1] [Copilot overview (docs)](https://code.visualstudio.com/docs/copilot/overview)
[2] [VS Code + MCP](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)
[3] [Official site (AI editor)](https://code.visualstudio.com/)
