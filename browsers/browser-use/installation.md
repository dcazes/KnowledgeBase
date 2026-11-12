---
type: Playbook
title: browser-use Installation
description: Install browser-use as a pinned Python dependency, set up the CLI and its agent skill for coding agents, or use Browser Use Cloud with an API key.
resource: https://docs.browser-use.com
tags: [browser-use, installation, uv, cli, skill]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: browser-use-github
    resource: "https://github.com/browser-use/browser-use"
    title: "browser-use/browser-use on GitHub"
    author: "site:github.com"
---

# browser-use — Installation

## Python library

```bash
uv init --python 3.12 my-agent && cd my-agent
uv add 'browser-use==1.0.3'            # pin exactly; releases can break things
export BROWSER_USE_API_KEY=bu_...      # only for the default cloud model/browser
```

Bring your own model and a local browser to avoid the cloud entirely (see [Snippets](snippets.md)).

## CLI + skill for coding agents

```bash
uv tool install browser-use==1.0.3
browser-use skill install              # registers an agent skill
```

Works with [Claude Code](../../agents/claude-code/index.md), [Codex](../../agents/codex/index.md), [Hermes](../../agents/hermes/index.md), [OpenClaw](../../agents/openclaw/index.md) — see [Agent skills](../../concepts/agent-skills.md).

## Upgrading from 0.x

The 1.0 architecture changed substantially; follow `MIGRATING.md` in the repo.

## Related

[browser-use index](index.md) · [Snippets](snippets.md)
