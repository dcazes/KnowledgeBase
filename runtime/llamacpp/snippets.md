---
type: Reference
title: llama.cpp Snippets
description: llama.cpp snippets — run and serve models straight from Hugging Face, key server flags (context, GPU layers, parallel slots, API key), OpenAI-compatible requests, and GBNF / JSON-schema constrained output.
resource: https://github.com/ggml-org/llama.cpp/tree/master/tools/server
tags: [llamacpp, snippets, server, cli, cheat-sheet, gbnf]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: llamacpp-github
    resource: "https://github.com/ggml-org/llama.cpp"
    title: "ggml-org/llama.cpp on GitHub"
    author: "site:github.com"
  - id: llamacpp-server
    resource: "https://github.com/ggml-org/llama.cpp/tree/master/tools/server"
    title: "llama.cpp server README"
    author: "site:github.com"
---

# llama.cpp — Snippets

## Run and serve

```bash
llama cli   -hf ggml-org/Qwen3.5-0.8B-GGUF                # chat in the terminal
llama serve -hf ggml-org/Qwen3.5-0.8B-GGUF                # OpenAI-compatible server
llama-server -m model.gguf -c 32768 -ngl 99 --port 8080 \
  --parallel 4 --api-key local-secret --jinja              # classic binary, common flags
```

| Flag | Meaning |
|---|---|
| `-c` | Context length |
| `-ngl` | Layers offloaded to GPU (`99` = all) |
| `--parallel` | Concurrent request slots |
| `--jinja` | Use the model's chat template (needed for tool calling) |
| `--api-key` | Require a bearer token |

The server also serves a built-in web chat UI at its root URL.

## OpenAI-compatible request

```bash
curl http://localhost:8080/v1/chat/completions -H "Authorization: Bearer local-secret" \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Hello"}]}'
```

## Constrained output

```bash
curl http://localhost:8080/v1/chat/completions -d '{
  "messages": [{"role": "user", "content": "Name a colour"}],
  "response_format": {"type": "json_schema", "json_schema": {"schema":
      {"type": "object", "properties": {"colour": {"type": "string"}}, "required": ["colour"]}}}}'
```

GBNF grammars (`--grammar-file`) constrain output to any formal grammar — the mechanism behind [structured output](../../concepts/structured-output.md) in many local tools.

## Related

[llama.cpp index](index.md) · [Installation](installation.md)
