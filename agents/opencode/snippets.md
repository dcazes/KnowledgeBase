---
type: Playbook
title: OpenCode Snippets
description: Copy-paste playbook for OpenCode — install, init, @ syntax, .opencode.json examples, MCP config, SearXNG tool, and a cheat sheet.
resource: https://opencode.ai/docs
tags: [opencode, snippets, cheat-sheet, config, mcp, examples]
timestamp: 2026-07-09T03:25:00Z
---

# OpenCode Snippets

A copy-paste playbook for common OpenCode operations on this instance (v1.17.18 at `~/.opencode/bin/opencode`).

## Install

```bash
curl -fsSL https://opencode.ai/install | sh
# or
npm install -g opencode-ai
export PATH="$HOME/.opencode/bin:$PATH"
```

## Initialize a project

```bash
cd /path/to/project
opencode /init
```

## Verify

```bash
opencode --version      # expect 1.17.18
which opencode          # ~/.opencode/bin/opencode
```

## `@` context-file syntax

```bash
opencode "@AGENTS.md what are the build steps?"
opencode "@USER.md @TOOLS.md how do I test this?"
opencode "@kb/graphify/graph.json find orphaned nodes"
```

## `.opencode.json` — minimal

```json
{
  "model": "anthropic/claude-sonnet-4",
  "allow": ["file_read", "file_write", "terminal", "network"],
  "deny": ["file_delete_recursive", "terminal:sudo"]
}
```

## `.opencode.json` — MCP + custom tool

```json
{
  "model": "anthropic/claude-sonnet-4",
  "mcpServers": {
    "graphify": { "url": "http://127.0.0.1:8000" },
    "searxng": { "url": "http://127.0.0.1:8080/search" }
  },
  "tools": {
    "web-search": {
      "command": "curl -s 'http://localhost:8080/search?q=$QUERY&format=json'",
      "description": "Search the web via local SearXNG",
      "env": {}
    }
  }
}
```

## `.opencode.json` — `:4000` proxy

```json
{
  "model": "openai/gpt-4o",
  "provider": {
    "openai": { "baseURL": "http://localhost:4000/v1", "apiKey": "sk-local" }
  }
}
```

## SearXNG custom tool

```json
{
  "tools": {
    "web-search": {
      "command": "curl -s 'http://localhost:8080/search?q=$QUERY&format=json'",
      "description": "Search the web via local SearXNG instance",
      "env": {}
    }
  }
}
```

## Cheat sheet

| Task | Command |
| --- | --- |
| Launch TUI | `opencode` |
| Init project | `opencode /init` |
| Version | `opencode --version` |
| Target context | `opencode "@FILE.md prompt"` |
| Graphify MCP | `http://127.0.0.1:8000` |
| SearXNG | `http://localhost:8080` |
| Failover proxy | `http://localhost:4000/v1` |

# Citations
[1] [OpenCode Documentation](https://opencode.ai/docs)
[2] [OpenCode GitHub repository (anomalyco)](https://github.com/anomalyco/opencode)
