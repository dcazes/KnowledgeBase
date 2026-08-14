---
type: Playbook
title: VSCode — Snippets & Cheat Sheet
description: Copy-paste VS Code commands for launching, editing programs/* repos, and registering MCP servers.
resource: https://code.visualstudio.com/docs
tags: [vscode, snippets, cheat-sheet, cli, mcp, workflow]
timestamp: 2026-07-09T02:15:00Z
---

# Launch / open

```bash
code                              # editor only
code .                            # current folder
code programs/firecrawl/firecrawl
code --goto main.py:42:10        # open at line:col
code --diff a.py b.py            # diff
code --list-extensions           # list installed
code --status                    # install status
```

# Register an MCP server (`.vscode/mcp.json`)

```json
{
  "servers": {
    "graphify": { "type": "stdio", "command": "python", "args": ["-m", "graphify.serve"] },
    "firecrawl": { "type": "sse", "url": "http://localhost:3002/mcp" }
  }
}
```

# Per-project config (`.vscode/`)

* `settings.json` — formatter, Docker/Py/TS defaults
* `launch.json` — debug
* `tasks.json` — `docker compose up`, `make`, `npm`

# Verify

```bash
code --version
code --list-extensions
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `code` not found | not installed | install .deb / flatpak |
| MCP tools missing | server not registered | add to mcp.json, reload |
| Copilot off | no license | sign in to GitHub Copilot |

# Citations

[1] [Installation](installation.md)
[2] [AI Features (MCP)](ai-features.md)
[3] [Workflow](workflow.md)
