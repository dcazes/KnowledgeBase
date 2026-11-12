---
type: Concept
title: Continue Overview
description: Continue's design — modes (chat, autocomplete, edit, agent), the YAML configuration of models, context providers, rules and MCP tools, Continue Hub assistants, and what its archival means for users.
resource: https://docs.continue.dev
tags: [continue, overview, config, archived]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: continue-docs
    resource: "https://docs.continue.dev"
    title: "Continue documentation"
    author: "site:docs.continue.dev"
  - id: continue-github
    resource: "https://github.com/continuedev/continue"
    title: "continuedev/continue on GitHub"
    author: "site:github.com"
---

# Continue — Overview

* **Modes:** chat, tab autocomplete, inline edit and agent (tools, terminal, MCP).
* **Configuration as code:** a `config.yaml` lists models per role (chat, autocomplete, edit, embed, rerank), context providers (files, docs, codebase index), rules and [MCP](../../concepts/mcp.md) servers. Shareable "assistants" were published on Continue Hub.
* **Local-first friendly:** first-class [Ollama](../../runtime/ollama/index.md) and [LM Studio](../../runtime/lmstudio/index.md) support made it the default way to use local models in an IDE.

## Status

The repository is read-only after the final release. Existing installs keep working; there will be no fixes for new models or editor versions. The codebase remains a useful reference for building model-agnostic IDE agents.

## Related

[Continue index](index.md) · [Snippets](snippets.md)
