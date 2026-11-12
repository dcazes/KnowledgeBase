---
type: Reference
title: Microsoft GraphRAG Snippets
description: GraphRAG CLI snippets — index a sample book, run global, local, DRIFT and basic queries, auto-tune prompts, and point it at a local OpenAI-compatible model.
resource: https://microsoft.github.io/graphrag
tags: [graphrag, snippets, cli, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphrag-docs
    resource: "https://microsoft.github.io/graphrag"
    title: "GraphRAG documentation"
    author: "site:microsoft.github.io"
---

# Microsoft GraphRAG — Snippets

## Index a sample corpus

```bash
graphrag init
curl https://www.gutenberg.org/cache/epub/24022/pg24022.txt -o ./input/book.txt
graphrag index           # writes Parquet tables to ./output
```

## Query

```bash
graphrag query "What are the top themes in this story?"                      # global is the default
graphrag query "Who is Scrooge and what are his main relationships?" --method local
graphrag query "How does Scrooge's relationship with Fred change?" --method drift
graphrag query "Where does the story take place?" --method basic
```

## Prompt tuning

Default extraction prompts are generic. Generate domain-adapted prompts from your own data before a large index:

```bash
graphrag prompt-tune --root . --domain "legal contracts"
```

## Local models

Set `api_base` for the chat and embedding models in `settings.yaml` to an [OpenAI-compatible](../../concepts/openai-compatible-api.md) server such as [Ollama](../../runtime/ollama/index.md) (`http://localhost:11434/v1`), [vLLM](../../runtime/vllm/index.md) or a [LiteLLM](../../runtime/litellm/index.md) proxy. Extraction quality drops noticeably with small models.

## Related

[GraphRAG index](index.md) · [Installation](installation.md)
