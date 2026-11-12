---
type: Reference
title: Cognee Snippets
description: Cognee snippets — remember and recall in Python, sessions, CLI usage, the REST API container, and plugin installs for Claude Code and Codex.
resource: https://github.com/topoteretes/cognee
tags: [cognee, snippets, cheat-sheet, python, cli]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: cognee-github
    resource: "https://github.com/topoteretes/cognee"
    title: "topoteretes/cognee on GitHub"
    author: "site:github.com"
  - id: cognee-docs
    resource: "https://docs.cognee.ai"
    title: "Cognee documentation"
    author: "site:docs.cognee.ai"
---

# Cognee — Snippets

## Remember and recall (Python)

```python
import asyncio, cognee

async def main():
    await cognee.remember(
        "Marie Curie was born in Warsaw and worked at the University of Paris.",
        dataset_name="physics",
    )
    for r in await cognee.recall("Where was Marie Curie born?", datasets=["physics"]):
        print(r)

asyncio.run(main())
```

## CLI

```bash
cognee-cli remember "Marie Curie was born in Warsaw." -d physics
cognee-cli recall "Where was Marie Curie born?" -d physics
cognee-cli demo
```

## Coding-agent plugins

```bash
# Claude Code
claude plugin marketplace add topoteretes/cognee-integrations
claude plugin install cognee-memory@cognee

# Codex (enable hooks first)
codex features enable hooks
codex plugin marketplace add topoteretes/cognee-integrations --ref main
codex plugin add cognee@cognee
```

## Related

[Cognee index](index.md) · [AI Integration](ai-integration.md)
