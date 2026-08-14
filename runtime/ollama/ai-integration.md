---
type: Concept
title: Ollama AI Integration
description: Wire Ollama into the stack — OpenAI-compatible :11434 endpoint for LiteLLM/OpenWebUI/AnythingLLM, local embeddings for Mem0/LightRAG, python SDK.
resource: https://docs.ollama.com
tags: [ollama, integration, openai-compatible, embeddings]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: ollama-docs-openai-compatibility
    resource: "https://docs.ollama.com/api/openai-compatibility"
    title: "Ollama docs — OpenAI compatibility"
    author: "site:docs.ollama.com"
  - id: ollama-docs-embeddings
    resource: "https://docs.ollama.com/api/embed"
    title: "Ollama docs — embeddings"
    author: "site:docs.ollama.com"
---

# Ollama — AI Integration

Ollama is the **local inference hub** — anything that speaks OpenAI-compatible REST can use it via `/v1`.

## OpenAI-compatible endpoint

```bash
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "llama3.1", "messages": [{"role": "user", "content": "hi"}]}'
```

Same surface as `/v1/embeddings` for `nomic-embed-text`.

## Stack wiring

* **[LiteLLM](../../agents/agent-stack/index.md)** — model entry `ollama/llama3.1` in the proxy config → unified `/v1` for the agent stack.
* **[AnythingLLM](../../apps/anythingllm/index.md)** — provider "Ollama", base URL `http://host.docker.internal:11434` (or `localhost` on host install).
* **[OpenWebUI](../../apps/openwebui/index.md)** — Ollama connection on :11434 pulls/uses models natively.
* **[Mem0](../../memory/mem0/index.md)** — `provider: "ollama"` for LLM + embedder.
* **[LightRAG](../../memory/lightrag/index.md)** — `LLM_BINDING=ollama`, `EMBEDDING_BINDING=ollama`.

## Python

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
r = client.chat.completions.create(model="llama3.1", messages=[{"role":"user","content":"hi"}])
```
