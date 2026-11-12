---
type: Playbook
title: Microsoft GraphRAG Installation
description: Install the graphrag package, initialise a workspace with settings.yaml and .env, configure OpenAI or Azure OpenAI models, and handle version upgrades.
resource: https://microsoft.github.io/graphrag/get_started/
tags: [graphrag, installation, pip, settings, azure-openai]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphrag-docs
    resource: "https://microsoft.github.io/graphrag"
    title: "GraphRAG documentation"
    author: "site:microsoft.github.io"
  - id: graphrag-github
    resource: "https://github.com/microsoft/graphrag"
    title: "microsoft/graphrag on GitHub"
    author: "site:github.com"
---

# Microsoft GraphRAG — Installation

Requires Python 3.10–3.12.

```bash
mkdir graphrag_quickstart && cd graphrag_quickstart
python -m venv .venv && source .venv/bin/activate
python -m pip install graphrag
graphrag init            # prompts for default chat and embedding models
```

`graphrag init` creates:

* `input/` — put your `.txt` (or configured) files here
* `.env` — `GRAPHRAG_API_KEY=<your key>`
* `settings.yaml` — models, chunking, extraction prompts, storage, search settings

## Azure OpenAI

In `settings.yaml` under `models:`, set `model_provider: azure`, `azure_deployment_name`, `api_base` and `api_version`. For managed identity, set `auth_method: azure_managed_identity` and remove `api_key`, then `az login`.

## Upgrading

Run `graphrag init --root <path> --force` between minor versions to refresh the config format; use the provided migration notebook between major versions to avoid re-indexing.

## Cost warning

Indexing can consume a lot of LLM tokens. Try the tutorial dataset with a small, cheap model first.

## Related

[GraphRAG index](index.md) · [Snippets](snippets.md)
