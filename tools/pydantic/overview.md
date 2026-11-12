---
type: Concept
title: Pydantic Overview
description: Pydantic v2 concepts — BaseModel and fields, strict versus lax validation, field and model validators, serialization, JSON Schema generation, TypeAdapter for arbitrary types, and the Rust core.
resource: https://docs.pydantic.dev
tags: [pydantic, overview, validation]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pydantic-docs
    resource: "https://docs.pydantic.dev"
    title: "Pydantic documentation"
    author: "site:docs.pydantic.dev"
---

# Pydantic — Overview

| Concept | Meaning |
|---|---|
| `BaseModel` | Class whose annotated attributes are validated on construction |
| `Field(...)` | Constraints, defaults, aliases and descriptions (descriptions flow into JSON Schema — and into LLM tool descriptions) |
| Lax vs strict | Lax coerces `"3"` → `3`; strict mode refuses |
| Validators | `@field_validator`, `@model_validator` for custom rules |
| Serialization | `model_dump()`, `model_dump_json()` with include/exclude and aliases |
| JSON Schema | `Model.model_json_schema()` |
| `TypeAdapter` | Validate any type (lists, unions, TypedDicts) without a model |

The v2 core is written in Rust, making validation fast enough to sit on hot paths such as parsing every LLM response.

## Related

[Pydantic index](index.md) · [Snippets](snippets.md)
