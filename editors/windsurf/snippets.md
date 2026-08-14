---
type: Playbook
title: Windsurf — Snippets & Cheat Sheet
description: Copy-paste install, sign-in, agent (Devin Local, ex-Cascade) usage, and MCP registration for Windsurf (now Devin Desktop).
resource: https://docs.windsurf.com/
tags: [windsurf, snippets, cheat-sheet, cascade, mcp, flows]
timestamp: 2026-07-09T03:35:00Z
---

# Install + launch

```bash
# download from windsurf.com/download, then:
windsurf
```
Sign in with Codeium on first launch.

# Use Devin Local (ex-Cascade)

* Open a repo, open the Devin Local panel.
* Ask: "Refactor X to use the new endpoint" → review multi-file diff → accept.
* Save repetitive steps as a **Flow**.

# Register MCP servers (verify path in docs.windsurf.com)

```json
{
  "mcpServers": {
    "graphify": { "url": "http://localhost:8000" },
    "firecrawl": { "url": "http://localhost:3002" },
    "searxng": { "url": "http://localhost:8080" }
  }
}
```

# Verify

```bash
windsurf --version
# confirm Devin Local reachable + Codeium signed in
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Devin Local offline | not signed in | sign in with Codeium |
| MCP tools missing | not registered | add servers in settings; reload |
| Model errors | plan/quota | check Codeium tier |

# Citations

[1] [Installation](installation.md)
[2] [Features](features.md)
[3] [AI Integration](ai-integration.md)
