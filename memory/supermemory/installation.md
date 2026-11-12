---
type: Playbook
title: Supermemory Installation
description: Use Supermemory through the hosted API and SDKs, install Supermemory Local as a single binary with optional Ollama for offline use, or add the hosted MCP server to an assistant.
resource: https://supermemory.ai/docs
tags: [supermemory, installation, local, sdk]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: supermemory-github
    resource: "https://github.com/supermemoryai/supermemory"
    title: "supermemoryai/supermemory on GitHub"
    author: "site:github.com"
---

# Supermemory — Installation

## Hosted API

Create an API key in the Supermemory console, then:

```bash
npm install supermemory      # or: pip install supermemory
export SUPERMEMORY_API_KEY=...
```

## Supermemory Local

```bash
curl -fsSL https://supermemory.ai/install | bash
```

One binary, zero config. Bring any model through a provider key, or run fully offline with [Ollama](../../runtime/ollama/index.md). Review install scripts before piping them to a shell.

## MCP only

Add `https://mcp.supermemory.ai/mcp` to your client's MCP config — see [Snippets](snippets.md#mcp).

## Related

[Supermemory index](index.md) · [Configuration](configuration.md) · [Local inference](../../concepts/local-inference.md)
