---
type: Playbook
title: CrewAI Installation
description: Install CrewAI and its tools package, scaffold a project with the crewai CLI, and run it.
resource: https://docs.crewai.com/installation
tags: [crewai, installation, cli]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: crewai-docs
    resource: "https://docs.crewai.com"
    title: "CrewAI documentation"
    author: "site:docs.crewai.com"
---

# CrewAI — Installation

```bash
uv tool install crewai            # CLI
crewai create crew research_team  # scaffold: agents.yaml, tasks.yaml, crew.py
cd research_team && crewai install
crewai run
pip install crewai 'crewai[tools]' # as a library
```

Requires Python 3.10+. Set model keys in `.env` (e.g. `OPENAI_API_KEY`, or `MODEL=ollama/qwen3:14b` with `API_BASE`).

## Related

[CrewAI index](index.md) · [Snippets](snippets.md)
