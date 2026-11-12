---
type: Software
title: Zep
description: Managed enterprise context platform for agents, built on the open-source Graphiti engine — Context Lake (governed context graphs over business data), agent memory, and Zep Agent Skills, reached through MCP or SDKs.
resource: https://www.getzep.com
tags: [zep, agent-memory, knowledge-graph, context-graph, managed-service, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: zep-site
    resource: "https://www.getzep.com"
    title: "Zep — official site"
    author: "site:getzep.com"
  - id: zep-docs
    resource: "https://help.getzep.com"
    title: "Zep documentation"
    author: "site:help.getzep.com"
  - id: zep-github
    resource: "https://github.com/getzep/zep"
    title: "getzep/zep — examples and integrations"
    author: "site:github.com"
  - id: zep-paper
    resource: "https://arxiv.org/abs/2501.13956"
    title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
    author: "Rasmussen et al., arXiv 2501.13956"
---

# Zep

**Zep** is a commercial context platform for production agents. It ingests users' conversations and business data into governed, temporal **context graphs** and serves the relevant context to agents over [MCP](../../concepts/mcp.md) or SDKs. The graph construction engine inside Zep is the open-source [Graphiti](../graphiti/index.md) framework.

| | |
|---|---|
| Category | [Agent memory](../../concepts/agent-memory.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md) |
| Delivery | Zep Cloud (managed) or bring-your-own-cloud; the self-hosted Community Edition is no longer developed |
| SDKs | Python `zep-cloud` 4.1.0 · TypeScript `@getzep/zep-cloud` · Go `zep-go/v4` |
| Open source | [Graphiti](../graphiti/index.md) (engine), `getzep/zep` (examples, integrations, `zep-ingest`, benchmarks) |

## Contents

* [Overview](overview.md) — Context Lake, agent memory, Agent Skills, Zep vs Graphiti
* [Installation](installation.md) — account, SDKs, MCP, coding-agent plugins
* [Snippets](snippets.md) — users, threads, messages, context retrieval, ontology
* [AI Integration](ai-integration.md) — framework integrations and the memory loop

## Related

* Concepts: [Agent memory](../../concepts/agent-memory.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md) · [Context engineering](../../concepts/context-engineering.md) · [Agent skills](../../concepts/agent-skills.md)
* Peers: [Graphiti](../graphiti/index.md), [Mem0](../mem0/index.md), [Letta](../letta/index.md), [Supermemory](../supermemory/index.md), [Honcho](../honcho/index.md)
* Comparison: [Memory alternatives](../alternatives.md)
