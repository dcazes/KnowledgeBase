---
type: Reference
title: vLLM Snippets
description: vLLM snippets — vllm serve with common flags, OpenAI client calls, tool calling, structured output, offline batch inference, and multi-GPU serving.
resource: https://docs.vllm.ai
tags: [vllm, snippets, serve, python, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: vllm-docs
    resource: "https://docs.vllm.ai"
    title: "vLLM documentation"
    author: "site:docs.vllm.ai"
---

# vLLM — Snippets

## Serve

```bash
vllm serve Qwen/Qwen3-8B --port 8000 \
  --max-model-len 32768 \
  --enable-auto-tool-choice --tool-call-parser hermes \
  --api-key local-secret
vllm serve meta-llama/Llama-3.3-70B-Instruct --tensor-parallel-size 4    # 4 GPUs
```

Tool-call and reasoning parsers are model-specific; check the docs for the right `--tool-call-parser`.

## Query (OpenAI client)

```python
from openai import OpenAI
c = OpenAI(base_url="http://localhost:8000/v1", api_key="local-secret")
r = c.chat.completions.create(model="Qwen/Qwen3-8B",
                              messages=[{"role": "user", "content": "Summarise PagedAttention"}])
```

## Structured output

```python
r = c.chat.completions.create(
    model="Qwen/Qwen3-8B",
    messages=[{"role": "user", "content": "Give a city and its country"}],
    response_format={"type": "json_schema", "json_schema": {"name": "place", "schema": {
        "type": "object", "properties": {"city": {"type": "string"}, "country": {"type": "string"}},
        "required": ["city", "country"]}}},
)
```

## Offline batch inference

```python
from vllm import LLM, SamplingParams
llm = LLM(model="Qwen/Qwen3-8B")
outs = llm.generate(["Hello", "What is RAG?"], SamplingParams(temperature=0.2, max_tokens=128))
for o in outs:
    print(o.outputs[0].text)
```

## Related

[vLLM index](index.md) · [Installation](installation.md) · [Structured output](../../concepts/structured-output.md)
