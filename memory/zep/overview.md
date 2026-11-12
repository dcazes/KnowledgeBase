---
type: Concept
title: Zep Overview
description: What Zep provides — governed context graphs over business data (Context Lake), temporal agent memory, Zep Agent Skills learned from agent tasks — and when to choose Zep over self-hosting Graphiti.
resource: https://help.getzep.com
tags: [zep, overview, context-graph, agent-memory, agent-skills]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
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

# Zep — Overview

Zep positions itself as the **context layer** between a company's data and its agents. In 2026 the product has two parts:

| Part | What it does |
|---|---|
| **Context Lake** | Unifies business data (messages, documents, Slack, email, JSON/CSV, fact triples) into governed context graphs that agents query |
| **Zep Agent Skills** | Observes the tasks agents perform and turns them into reusable [skills](../../concepts/agent-skills.md) that agents then follow |

Agent memory — remembering users and threads across sessions — is built on the same context graphs.

## How it works

Under the hood Zep runs [Graphiti](../graphiti/index.md): every message or record becomes an *episode*; entities and facts are extracted into a bi-temporal [knowledge graph](../../concepts/knowledge-graphs.md); old facts are invalidated rather than deleted. Zep adds what Graphiti leaves to you: its own graph database service (Konig), users and threads, ingestion connectors, access governance, a dashboard with graph visualisation, and pre-tuned retrieval (sub-200 ms at scale, per Zep).

The design and its LongMemEval / Deep Memory Retrieval results are described in the paper *Zep: A Temporal Knowledge Graph Architecture for Agent Memory* (arXiv 2501.13956).

## Zep vs Graphiti

| | Zep | [Graphiti](../graphiti/index.md) |
|---|---|---|
| What | Managed platform | Open-source Python framework |
| Graph store | Included | Bring your own (Neo4j, FalkorDB, Neptune) |
| Users, threads, ingestion | Built in | You build them |
| Ops, auth, SLAs | Provided | Your responsibility |
| Deployment | Cloud or BYOC | Self-hosted only |

Zep Community Edition (the old self-hosted server) is no longer maintained; self-hosters use Graphiti directly.

## Related

[Zep index](index.md) · [AI Integration](ai-integration.md) · [Agent memory](../../concepts/agent-memory.md) · [Memory alternatives](../alternatives.md)
