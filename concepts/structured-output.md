---
type: Concept
title: Structured Output
description: Getting reliable structured data from LLMs — JSON mode versus JSON Schema-constrained decoding, provider and local-server support, validation and retry with Pydantic, and where structured output appears across extraction, memory and agent tools.
resource: https://docs.pydantic.dev
tags: [concept, structured-output, json-schema, validation, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pydantic-docs
    resource: "https://docs.pydantic.dev"
    title: "Pydantic documentation"
    author: "site:docs.pydantic.dev"
  - id: xgrammar
    resource: "https://github.com/mlc-ai/xgrammar"
    title: "XGrammar"
    author: "site:github.com"
---

# Structured Output

**Structured output** means the model returns data in an exact shape — usually JSON matching a schema — rather than free text. It turns LLMs into reliable components: extractors, classifiers, routers and tool callers.

## Levels of reliability

| Method | Guarantee |
|---|---|
| Prompting ("reply in JSON") | None |
| JSON mode | Valid JSON, any shape |
| **Schema-constrained decoding** | Output must match the JSON Schema — tokens that would break it are masked |
| Validate + retry | Parse with [Pydantic](../tools/pydantic/index.md); on error send the message back and retry |

## Support

* Hosted APIs (OpenAI, Anthropic, Gemini) support schema-based outputs.
* Local: [Ollama](../runtime/ollama/snippets.md) `format`, [vLLM](../runtime/vllm/snippets.md) `response_format` via xgrammar/guidance, [llama.cpp](../runtime/llamacpp/snippets.md) GBNF grammars and JSON schema, [LM Studio](../runtime/lmstudio/overview.md).

## Where it matters in this vault

* Agent outputs: [Pydantic AI](../agents/pydanticAI/overview.md) `output_type`, [browser-use](../browsers/browser-use/snippets.md) `output_model_schema`.
* Extraction: [Firecrawl](../browsers/firecrawl/snippets.md) and [Crawl4AI](../browsers/crawl4ai/snippets.md) JSON schemas.
* Memory and graphs: [Graphiti](../memory/graphiti/overview.md) entity extraction needs structured output, which is why small models struggle with it.

## Related

[Tool calling](tool-calling.md) · [Pydantic](../tools/pydantic/index.md) · [Concepts index](index.md)
