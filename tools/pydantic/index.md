---
type: Software
title: Pydantic
description: Python's standard data-validation library — type-hint-driven models with a Rust core, JSON Schema generation, serialization and settings management — and the backbone of structured output and tool schemas across the AI ecosystem.
resource: https://docs.pydantic.dev
tags: [pydantic, python, validation, json-schema, structured-output]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pydantic-github
    resource: "https://github.com/pydantic/pydantic"
    title: "pydantic/pydantic on GitHub"
    author: "site:github.com"
  - id: pydantic-docs
    resource: "https://docs.pydantic.dev"
    title: "Pydantic documentation"
    author: "site:docs.pydantic.dev"
---

# Pydantic

**Pydantic** validates data against Python type hints. Define a `BaseModel`, and input is parsed, coerced and checked; errors are precise; and the model can emit **JSON Schema**. That last feature is why Pydantic sits under so much AI tooling: tool definitions, [structured outputs](../../concepts/structured-output.md) and agent configs are all JSON Schema.

| | |
|---|---|
| Category | Python library · [Structured output](../../concepts/structured-output.md) |
| License | MIT |
| Language | Python with a Rust core (`pydantic-core`) |
| Latest release | v2.14.3 (2026-11-05); `pydantic-settings` 2.16 |

## Contents

* [Overview](overview.md) — models, validation, schema, performance
* [Installation](installation.md)
* [Configuration](configuration.md) — model config and pydantic-settings
* [Snippets](snippets.md) — models, validators, JSON Schema, TypeAdapter
* [AI Integration](ai-integration.md) — where Pydantic appears across AI tools

## Related

* Built on it: [Pydantic AI](../../agents/pydanticAI/index.md), [Graphiti](../../memory/graphiti/concepts.md) ontologies, [browser-use](../../browsers/browser-use/index.md), [CrewAI](../../agents/crewai/index.md), FastAPI
* Concepts: [Structured output](../../concepts/structured-output.md) · [Tool calling](../../concepts/tool-calling.md)
* Comparison: [Tools alternatives](../alternatives.md)
