---
type: Reference
title: Windsurf Snippets
description: Windsurf / Devin Desktop snippets — a workspace rules file, a saved workflow, and MCP server configuration.
resource: https://docs.devin.ai
tags: [windsurf, snippets, rules, mcp, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: devin-docs
    resource: "https://docs.devin.ai"
    title: "Devin documentation"
    author: "site:docs.devin.ai"
---

# Windsurf — Snippets

## Workspace rule (`.windsurf/rules/style.md`)

```markdown
Use TypeScript strict mode. Prefer small pure functions. Every new module needs a test.
```

## Workflow (`.windsurf/workflows/release.md`)

```markdown
# Release
1. Run the test suite and stop on failure.
2. Bump the version in package.json.
3. Update CHANGELOG.md from merged PR titles.
```

Invoke with `/release`.

## MCP (`mcp_config.json`)

```json
{ "mcpServers": { "playwright": { "command": "npx", "args": ["@playwright/mcp@latest"] } } }
```

## Related

[Windsurf index](index.md) · [Features](features.md)
