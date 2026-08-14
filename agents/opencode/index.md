---
type: Reference
title: OpenCode
description: Terminal-native open-source AI coding agent (anomalyco/opencode, v1.18.18) — no daemons, per-project isolation, MCP + custom tools.
resource: https://opencode.ai/docs
tags: [opencode, ai-agent, terminal, coding, anomalyco, opencode-ai]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: opencode-github
    resource: "https://github.com/anomalyco/opencode"
    title: "OpenCode GitHub"
    author: "site:github.com"
---

# OpenCode

OpenCode terminal AI agent (v1.18.18); skills, tools, delegation. A lightweight alternative for code-focused tasks. The repo moved from sst/opencode to anomalyco/opencode (Jan 2026); the npm package is `opencode-ai`.

## Contents

* [Overview](overview.md) - what OpenCode is, architecture
* [Installation](installation.md) - setup, config
* [Configuration](configuration.md) - config.yaml, providers
* [Hierarchical Structure](hierarchical-structure.md) - project/workspace organization
* [AI Integration](ai-integration.md) - SearXNG, Graphify, Firecrawl
* [Alternatives](alternatives.md) - Hermes, OpenClaw, Cursor, Windsurf
* [Snippets](snippets.md) - common tasks cheat sheet

## Instance facts

* **Config:** `~/.opencode/config.yaml` (or project-level)
* **Providers:** OpenAI-compatible (incl. :4000 proxy), Anthropic, local

## Cross-references

* **Graphify** — `graphify install --platform opencode` — see [Graphify AI Integration](../../memory/graphify/ai-integration.md)
* **SearXNG** — web search via SearXNG — see [SearXNG AI Integration](../../runtime/searxng/ai-integration.md)
* **Firecrawl** — web extraction — see [Firecrawl AI Integration](../../browsers/firecrawl/ai-integration.md)
* **Hermes** — fellow terminal agent — see [Hermes AI Integration](../hermes/ai-integration.md)

## Last verified

**2026-08-12** — Config and integration docs verified. OpenCode v1.18.18; repo at github.com/anomalyco/opencode; npm package opencode-ai.
