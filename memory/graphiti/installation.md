---
type: Playbook
title: Graphiti Installation
description: Install graphiti-core with the right backend and LLM-provider extras, set provider keys and concurrency, and start a graph database with Docker.
resource: https://github.com/getzep/graphiti
tags: [graphiti, installation, pip, uv, docker]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphiti-github
    resource: "https://github.com/getzep/graphiti"
    title: "getzep/graphiti on GitHub"
    author: "site:github.com"
---

# Graphiti — Installation

## Requirements

* Python 3.10+
* A graph database (see [Backends](backends.md))
* An LLM and embedder. The default is OpenAI (`OPENAI_API_KEY`); Anthropic, Gemini and Groq are supported via extras; anything [OpenAI-compatible](../../concepts/openai-compatible-api.md), including [Ollama](../../runtime/ollama/index.md), [vLLM](../../runtime/vllm/index.md), [llama.cpp](../../runtime/llamacpp/index.md) and [LM Studio](../../runtime/lmstudio/index.md), works through `OpenAIGenericClient`.

## Install

```bash
pip install graphiti-core                        # or: uv add graphiti-core
pip install "graphiti-core[falkordb]"            # FalkorDB driver
pip install "graphiti-core[anthropic,google-genai,groq]"   # extra LLM providers
pip install "graphiti-core[neptune]"             # Amazon Neptune
```

## Environment

```bash
export OPENAI_API_KEY=...
export SEMAPHORE_LIMIT=10       # concurrent LLM operations during ingestion; lower on 429s
```

## Start a database

```bash
git clone https://github.com/getzep/graphiti && cd graphiti
docker compose up                       # Neo4j
docker compose --profile falkordb up    # FalkorDB
```

## Verify

Run `examples/quickstart` from the repo: it connects, builds indices, adds text and JSON episodes, and runs hybrid edge and node searches.

## Related

[Graphiti index](index.md) · [Backends](backends.md) · [Snippets](snippets.md) · [Docker](../../runtime/docker/index.md)
