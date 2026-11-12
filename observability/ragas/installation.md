---
type: Playbook
title: Ragas Installation
description: Install Ragas from PyPI or source, configure a judge LLM and embeddings, and scaffold an evaluation project with ragas quickstart.
resource: https://docs.ragas.io
tags: [ragas, installation]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: ragas-github
    resource: "https://github.com/vibrantlabsai/ragas"
    title: "vibrantlabsai/ragas on GitHub"
    author: "site:github.com"
---

# Ragas — Installation

```bash
pip install ragas
ragas quickstart              # list templates
ragas quickstart rag_eval     # scaffold a RAG evaluation project
```

Ragas needs a judge LLM (and embeddings for some metrics); wrap any LangChain/LlamaIndex model or an [OpenAI-compatible](../../concepts/openai-compatible-api.md) endpoint, including local [Ollama](../../runtime/ollama/index.md) or [vLLM](../../runtime/vllm/index.md).

## Related

[Ragas index](index.md) · [Snippets](snippets.md)
