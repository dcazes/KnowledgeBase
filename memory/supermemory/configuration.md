---
type: Reference
title: Supermemory Configuration
description: Organising Supermemory data with container tags, enabling connectors, choosing models for Supermemory Local, and data-handling considerations.
resource: https://supermemory.ai/docs
tags: [supermemory, configuration, connectors, privacy]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: supermemory-docs
    resource: "https://supermemory.ai/docs"
    title: "Supermemory documentation"
    author: "site:supermemory.ai"
  - id: supermemory-github
    resource: "https://github.com/supermemoryai/supermemory"
    title: "supermemoryai/supermemory on GitHub"
    author: "site:github.com"
---

# Supermemory — Configuration

## Container tags

Every write and query takes a `containerTag` (TS) / `container_tag` (Python). Use one per user for personalisation, or per project or client to keep contexts apart. Plugins call these **projects** so you can separate work and personal memory.

## Connectors

Connect Google Drive, Gmail, Notion, OneDrive or GitHub in the console; documents sync via webhooks and become searchable alongside memories.

## Models (Local)

Supermemory Local accepts any model provider key, or an Ollama endpoint for offline operation. Pick an embedding model that suits your languages and content — see [Embeddings](../../concepts/embeddings.md).

## Data handling

Connectors and plugins capture a lot of personal context. Decide per container what should be stored, and prefer Local for sensitive data. See [Agent security](../../concepts/agent-security.md).

## Related

[Supermemory index](index.md) · [Installation](installation.md)
