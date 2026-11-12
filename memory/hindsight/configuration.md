---
type: Reference
title: Hindsight Configuration
description: Configure Hindsight's LLM provider (25+ hosted and local options), storage backend, and per-bank settings through HINDSIGHT_API_* environment variables.
resource: https://hindsight.vectorize.io/developer/configuration
tags: [hindsight, configuration, ollama, postgres, env]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hindsight-docs
    resource: "https://hindsight.vectorize.io"
    title: "Hindsight documentation"
    author: "site:hindsight.vectorize.io"
  - id: hindsight-github
    resource: "https://github.com/vectorize-io/hindsight"
    title: "vectorize-io/hindsight on GitHub"
    author: "site:github.com"
---

# Hindsight — Configuration

## LLM provider

Set `HINDSIGHT_API_LLM_PROVIDER`, `HINDSIGHT_API_LLM_MODEL` and `HINDSIGHT_API_LLM_API_KEY`. Providers include hosted (`openai`, `anthropic`, `gemini`, `groq`, `bedrock`, `vertexai`, `deepseek`, …) and local options such as `ollama` and other [OpenAI-compatible](../../concepts/openai-compatible-api.md) servers like [vLLM](../../runtime/vllm/index.md) and [LM Studio](../../runtime/lmstudio/index.md).

Retain makes LLM calls for extraction; reflect makes more. Use a capable model for reflect and a cheaper one for retain if your provider setup allows.

## Storage

* Embedded `pg0` PostgreSQL (default in the single container) — simplest.
* External PostgreSQL via Docker Compose or Helm — for production and backups ([pgvector](../../databases/pgvector/index.md)-style vector search inside Postgres).
* Oracle AI Database — enterprise option with feature parity.

## Banks

Each bank holds its own memories and settings, including a **disposition** that shapes how `reflect` answers. Create one bank per user, agent or repository.

## Related

[Hindsight index](index.md) · [Installation](installation.md) · [Local inference](../../concepts/local-inference.md)
