---
type: Reference
title: OpenCode Configuration
description: The .opencode.json structure — model selection, allow/deny permissions, MCP servers, custom tools, and the :4000 OpenAI-compatible proxy.
resource: https://opencode.ai/docs/config
tags: [opencode, config, json, permissions, mcp, proxy]
timestamp: 2026-07-09T03:25:00Z
---

# OpenCode Configuration

OpenCode is configured with a plaintext `.opencode.json` file in the project root. This reference documents its key sections.

## Basic structure

```json
{
  "model": "anthropic/claude-sonnet-4",
  "allow": ["file_read", "file_write", "terminal", "network"],
  "deny": ["file_delete_recursive", "terminal:sudo"],
  "mcpServers": {
    "graphify": { "url": "http://127.0.0.1:8000" },
    "searxng": { "url": "http://127.0.0.1:8080/search" }
  },
  "tools": {
    "web-search": {
      "command": "curl -s ...",
      "description": "...",
      "env": {}
    }
  }
}
```

## Model selection

The `model` key selects the default provider/model. Use provider-prefixed names:

- `anthropic/claude-sonnet-4`
- `openai/gpt-4o`
- `google/gemini-2.5-pro`
- `ollama/llama3.1`
- `nvidia/nemotron`

### Pointing at the `:4000` proxy

The instance runs an OpenAI-compatible failover proxy at `http://localhost:4000/v1` (OpenRouter/NIM). Point a model at it by configuring the OpenAI-compatible endpoint:

```json
{
  "model": "openai/gpt-4o",
  "provider": {
    "openai": {
      "baseURL": "http://localhost:4000/v1",
      "apiKey": "sk-local"
    }
  }
}
```

## Permissions: allow / deny

- `allow` — capabilities the agent may use (e.g. `file_read`, `file_write`, `terminal`, `network`).
- `deny` — explicit blocks (e.g. `file_delete_recursive`, `terminal:sudo`).

The `deny` list always wins over `allow`.

## MCP servers

`"mcpServers"` registers Model Context Protocol servers by URL. Example from this instance:

```json
{
  "mcpServers": {
    "graphify": { "url": "http://127.0.0.1:8000" },
    "searxng": { "url": "http://127.0.0.1:8080/search" }
  }
}
```

## Custom tools

`"tools"` defines custom commands the agent can invoke:

```json
{
  "tools": {
    "web-search": {
      "command": "curl -s 'https://api.example.com/search?q=$QUERY'",
      "description": "Search the web via a custom endpoint",
      "env": { "API_KEY": "..." }
    }
  }
}
```

## Verify

```bash
cd /path/to/project
cat .opencode.json          # inspect config
opencode --version          # confirm binary is active
# Launch and confirm the model + tools load without errors
opencode
```

# Citations
[1] [OpenCode Config Docs](https://opencode.ai/docs/config)
[2] [OpenCode GitHub repository (anomalyco)](https://github.com/anomalyco/opencode)
