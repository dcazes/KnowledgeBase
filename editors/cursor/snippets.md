---
type: Reference
title: Cursor Snippets
description: Cursor quick reference — keyboard shortcuts, a project rule file, AGENTS.md usage, and MCP server configuration in .cursor/mcp.json.
resource: https://cursor.com/docs
tags: [cursor, snippets, rules, mcp, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: cursor-docs
    resource: "https://cursor.com/docs"
    title: "Cursor documentation"
    author: "site:cursor.com"
---

# Cursor — Snippets

| Shortcut (macOS / Win-Linux) | Action |
|---|---|
| Tab | Accept prediction |
| Cmd/Ctrl+K | Inline edit |
| Cmd/Ctrl+I | Agent / chat panel |
| Cmd/Ctrl+L | Add selection to chat |

## Rule file (`.cursor/rules/testing.mdc`)

```markdown
---
description: Testing conventions
globs: ["**/*.test.ts"]
alwaysApply: false
---
Use vitest. Prefer table-driven tests. Never mock the database layer; use the test container.
```

## MCP (`.cursor/mcp.json`)

```json
{ "mcpServers": {
    "playwright": { "command": "npx", "args": ["@playwright/mcp@latest"] },
    "graphiti":   { "url": "http://localhost:8000/mcp/" } } }
```

## Related

[Cursor index](index.md) · [Features](features.md)
