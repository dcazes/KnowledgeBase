---
type: Reference
title: Ollama Snippets
description: Ollama cheat sheet — CLI model management, native REST chat and embeddings, structured output, the OpenAI-compatible endpoint, and the Python and JavaScript libraries.
resource: https://docs.ollama.com/api
tags: [ollama, snippets, cli, rest, python, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: ollama-github
    resource: "https://github.com/ollama/ollama"
    title: "ollama/ollama on GitHub"
    author: "site:github.com"
  - id: ollama-docs
    resource: "https://docs.ollama.com"
    title: "Ollama documentation"
    author: "site:docs.ollama.com"
---

# Ollama — Snippets

## CLI

```bash
ollama run gemma4                 # pull if needed, then chat
ollama pull qwen3:8b
ollama ls ; ollama ps             # installed / loaded models
ollama show qwen3:8b              # template, parameters, capabilities
ollama stop qwen3:8b ; ollama rm qwen3:8b
```

## REST

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4", "stream": false,
  "messages": [{"role": "user", "content": "Why is the sky blue?"}]}'

curl http://localhost:11434/api/embed -d '{"model": "nomic-embed-text", "input": ["hello world"]}'
```

## Structured output

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "qwen3:8b", "stream": false,
  "messages": [{"role": "user", "content": "Extract: Alice is 31 and lives in Lisbon"}],
  "format": {"type":"object","properties":{"name":{"type":"string"},"age":{"type":"integer"},"city":{"type":"string"}},"required":["name","age","city"]}}'
```

## OpenAI-compatible client

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")   # key is ignored
print(client.chat.completions.create(model="gemma4",
      messages=[{"role": "user", "content": "Hi"}]).choices[0].message.content)
```

## Python and JavaScript

```python
from ollama import chat
print(chat(model="gemma4", messages=[{"role": "user", "content": "Hi"}]).message.content)
```

```javascript
import ollama from "ollama";
const r = await ollama.chat({ model: "gemma4", messages: [{ role: "user", content: "Hi" }] });
```

## Related

[Ollama index](index.md) · [Configuration](configuration.md) · [OpenAI-compatible API](../../concepts/openai-compatible-api.md)
