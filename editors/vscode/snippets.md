---
type: Reference
title: VS Code Snippets
description: VS Code AI snippets — MCP server configuration in .vscode/mcp.json, a Copilot instructions file, a prompt file, and useful CLI commands.
resource: https://code.visualstudio.com/docs
tags: [vscode, snippets, mcp, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: vscode-site
    resource: "https://code.visualstudio.com"
    title: "Visual Studio Code"
    author: "site:code.visualstudio.com"
---

# VS Code — Snippets

## `.vscode/mcp.json`

```json
{
  "servers": {
    "playwright": { "command": "npx", "args": ["@playwright/mcp@latest"] },
    "graphiti":   { "type": "http", "url": "http://localhost:8000/mcp/" }
  }
}
```

## `.github/copilot-instructions.md`

```markdown
- Use pnpm, not npm.
- Run `pnpm test` after changes; fix failures before finishing.
- Follow the error-handling pattern in src/lib/errors.ts.
```

## Prompt file (`.github/prompts/review.prompt.md`)

```markdown
---
mode: agent
description: Review the current diff for security issues
---
Review the staged changes for injection, auth and secrets problems. List findings with file and line.
```

## CLI

```bash
code .                       # open folder
code --install-extension anthropic.claude-code
code --list-extensions
code tunnel                  # remote access via a tunnel
```

## Related

[VS Code index](index.md) · [AI features](ai-features.md)
