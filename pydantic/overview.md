---
type: Concept
title: Pydantic Overview
description: What Pydantic is — typed data validation, model_dump/model_validate serialization, JSON Schema export, Settings; v2 API surface.
resource: https://docs.pydantic.dev
tags: [pydantic, overview, validation, v2]
timestamp: 2026-08-13T00:00:00Z
---

# Overview

Pydantic v2 (Rust core) validates your data at the edge: define a schema as a class, hand it untrusted input, and get a typed, validated object or a structured error.

## Core concepts

* **`BaseModel`** — schema classes. Field types annotate the schema; instantiation validates.
* **Validation** — type coercion + constraint checks (ranges, patterns, literals, nested models, `EmailStr`, …).
* **Serialization** — `model_dump()` (dict) / `model_dump_json()` / `model_copy()`.
* **De-serialization** — `model_validate()` / `model_validate_json()`.
* **JSON Schema** — `model_json_schema()` exports the schema (used to constrain LLM output).
* **`pydantic-settings`** — `BaseSettings` reads env/.env into typed config.

## Why it's everywhere

- **LLM contracts** — validated output schemas for agents ([PydanticAI](../pydanticAI/index.md) is built on it).
- **API layers** — FastAPI request/response models.
- **Config** — typed env loading via Settings.
- **Tooling** — most of this stack's Python tools validate configs with it.

## Version notes

- v2 is current (this machine: 2.9.0 system / 2.13.4 venv); v1 API differs (`parse_obj`, `.dict()`).
- **Security**: see [PydanticAI → CVEs](../pydanticAI/index.md) — pydantic >= 2.12 required for the 2026-07 fixes.

# Citations

[1] [Pydantic docs](https://docs.pydantic.dev)
[2] [Pydantic GitHub](https://github.com/pydantic/pydantic)
