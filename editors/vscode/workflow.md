---
type: Reference
title: VSCode — Workflow (programs/* & Agent Skills)
description: Using VS Code to edit the local programs/* repos and to author agent skills (Graphify/Hermes/OpenCode).
resource: https://code.visualstudio.com/docs
tags: [vscode, workflow, programs, agent-skills, graphify, hermes, opencode]
timestamp: 2026-07-09T02:13:00Z
---

# Editing the programs/* repos

Your stack's source lives under `/home/daniel/Desktop/programs/`. Open a repo directly:

```bash
code programs/firecrawl/firecrawl
code programs/dify/dify
code programs/firecrawl/firecrawl
```

Recommended per-project setup (`.vscode/` in each repo):
* `settings.json` — Docker/Python/TS defaults, formatter on save.
* `launch.json` — debug configs (Node/Python).
* `tasks.json` — `docker compose up`, `make`, `npm` tasks.
* `mcp.json` — register Graphify/Firecrawl MCP servers for Agent Mode.

# Authoring agent skills

VS Code is where you write the **agent skills** this KB documents:
* **Graphify packs** — `graphify add` content, then edit the generated graph/skill files.
* **Hermes / OpenCode skills** — markdown/code skills the agents load (Python helpers, web-search wrappers, etc.).
* **Firecrawl skills** — `firecrawl-cli` task scripts.

Workflow:
1. Open the skill folder in VS Code.
2. Edit the markdown/code.
3. Test by invoking the skill from the agent (Hermes/OpenCode) or running the snippet.
4. Commit via the built-in Git UI.

# Tips

* Use **multi-root workspaces** to keep several `programs/*` repos open at once.
* Enable **Settings Sync** (or commit `.vscode/`) to share config across machines.
* For Docker-heavy repos, install the **Docker** extension for Compose-aware editing.

# Citations

[1] [VS Code docs](https://code.visualstudio.com/docs)
[2] [AI Features (MCP)](ai-features.md)
[3] [Graphify skills](/../../graphify/ai-integration.md)
