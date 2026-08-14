---
type: CheatSheet
title: Ollama Snippets
description: Ollama cheat sheet — pull/run/list/ps, Modelfile, /api calls, OpenAI-compatible curl, python client, embeddings.
resource: https://docs.ollama.com
tags: [ollama, snippets, cheat-sheet]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: ollama-docs
    resource: "https://docs.ollama.com"
    title: "Ollama docs"
    author: "site:docs.ollama.com"
---

# Snippets

## CLI

```bash
ollama pull llama3.1              # download model
ollama run llama3.1               # interactive chat
ollama list                       # local models
ollama ps                         # currently loaded
ollama rm qwen2.5:7b              # delete
ollama show llama3.1              # details (params, context, modelfile)
```

## Serve

```bash
ollama serve                      # :11434 (default bind 127.0.0.1)
docker compose up -d              # local checkout's compose
```

## Raw API

```bash
curl http://localhost:11434/api/generate -d '{"model":"llama3.1","prompt":"Hi","stream":false}'
curl http://localhost:11434/api/chat -d '{"model":"llama3.1","messages":[{"role":"user","content":"Hi"}]}'
curl http://localhost:11434/api/tags                  # model list
```

## OpenAI-compatible

```bash
curl http://localhost:11434/v1/chat/completions -H "Content-Type: application/json" \
  -d '{"model":"llama3.1","messages":[{"role":"user","content":"Hi"}]}'
curl http://localhost:11434/v1/embeddings -H "Content-Type: application/json" \
  -d '{"model":"nomic-embed-text","input":"embed me"}'
```

## Python (openai SDK)

```python
from openai import OpenAI
c = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
print(c.chat.completions.create(model="llama3.1", messages=[{"role":"user","content":"Hi"}]).choices[0].message.content)
```

## Modelfile (bake defaults)

```
FROM llama3.1
PARAMETER temperature 0.7
PARAMETER num_ctx 8192
```

```bash
ollama create mymodel -f Modelfile
```
