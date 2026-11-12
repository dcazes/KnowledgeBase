---
type: Reference
title: Antigravity Snippets
description: Antigravity CLI basics — starting agy, signing out, remote use over SSH, exporting sessions to the desktop app, and migrating from Gemini CLI.
resource: https://github.com/google-antigravity/antigravity-cli
tags: [antigravity, snippets, cli, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: agy-github
    resource: "https://github.com/google-antigravity/antigravity-cli"
    title: "google-antigravity/antigravity-cli"
    author: "site:github.com"
---

# Antigravity — Snippets

```bash
agy                 # start the terminal agent in the current project
```

| Action | How |
|---|---|
| Sign out | `/logout` |
| Remote / SSH | Run `agy` on the server; it prints an authorisation URL to open locally |
| Continue in the GUI | Export the session to Antigravity 2.0 |

## Migrating from Gemini CLI

Replace `gemini` invocations with `agy` and sign in with the same Google account. Project instruction files and MCP server configs need to be re-created in Antigravity's settings; check the official docs for supported formats.

## Related

[Antigravity index](index.md) · [Installation](installation.md)
