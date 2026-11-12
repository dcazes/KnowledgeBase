---
type: Playbook
title: Mem0 Installation
description: Install Mem0 as a Python or Node library (with the optional NLP extra for hybrid search), run the self-hosted server with Docker, or use the Mem0 CLI.
resource: https://docs.mem0.ai/open-source/overview
tags: [mem0, installation, docker, pip, npm, cli]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: mem0-readme
    resource: "https://github.com/mem0ai/mem0"
    title: "Mem0 README — Quickstart"
    author: "site:github.com"
  - id: mem0-oss-setup
    resource: "https://docs.mem0.ai/open-source/setup"
    title: "Mem0 self-hosted setup"
    author: "site:docs.mem0.ai"
---

# Mem0 — Installation

## Library

```bash
pip install mem0ai                      # Python 3.10+
pip install "mem0ai[nlp]"               # adds BM25 keyword + entity extraction for hybrid search
python -m spacy download en_core_web_sm # required by the nlp extra

npm install mem0ai                      # Node 18+; import { Memory } from "mem0ai/oss"
```

With no configuration, the Python library uses OpenAI (`gpt-5-mini` for extraction, `text-embedding-3-small` for embeddings) and a local [Qdrant](../../databases/qdrant/index.md). Set `OPENAI_API_KEY`, or point it at a local model — see [Configuration](configuration.md).

## Self-hosted server

The server lives in the `server/` folder of the main repo and runs with [Docker Compose](../../runtime/docker/index.md):

```bash
git clone https://github.com/mem0ai/mem0 && cd mem0/server
make bootstrap            # start the stack, create an admin, issue the first API key
# or
docker compose up -d      # then finish setup in the browser wizard at http://localhost:3000
```

Authentication is **on by default**. When upgrading from a pre-auth build, set `ADMIN_API_KEY`, register an admin through the wizard, or set `AUTH_DISABLED=true` for local development only.

## CLI

```bash
npm install -g @mem0/cli      # or: pip install mem0-cli
mem0 init                     # interactive; `mem0 init --agent` lets an agent mint its own platform key
mem0 add "Prefers dark mode and vim keybindings" --user-id alice
mem0 search "What does Alice prefer?" --user-id alice
```

## Upgrading from v1.x / early v2

The 2026 memory algorithm is a breaking change: entity ids moved into `filters` for `search()`/`get_all()`, `top_k` defaults to 20, a `threshold` of 0.1 is applied, reranking is off by default, and graph store config is ignored. Read the official [migration guide](https://docs.mem0.ai/migration/oss-v2-to-v3) before upgrading.

## Related

[Mem0 index](index.md) · [Snippets](snippets.md) · [Docker](../../runtime/docker/index.md) · [Self-hosting](../../concepts/self-hosting.md)
