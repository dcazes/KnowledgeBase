---
type: Reference
title: Pydantic
description: Data validation & settings management in Python — the foundation under PydanticAI and the whole agent stack; system 2.9.0 / venv 2.13.4 on this machine.
resource: https://docs.pydantic.dev
tags: [pydantic, python, validation, schemas, settings]
timestamp: 2026-08-13T00:00:00Z
---

# Pydantic

**Data validation and settings management** in Python — schemas defined as typed classes, validated at instantiation, with serialization, JSON Schema export, and Pydantic Settings for env config. It is the foundation under [PydanticAI](../pydanticAI/index.md) and most of this stack's tooling.

On this machine: system python has **pydantic 2.9.0**; the `programs/pydantic/.venv` has **2.13.4**. The `programs/pydantic/` dir contains a `pydantic_ai_template.py` (schema-reuse + agent example) and `pydantic_init.ipynb` (intro notebook) — no source checkout.

## Contents

* [Overview](overview.md) — BaseModel, validation, serialization, JSON Schema, Settings
* [Installation](installation.md) — pip install, versions on this machine, verify
* [Configuration](configuration.md) — model_config, Field constraints, validators, Settings
* [AI Integration](ai-integration.md) — schemas as agent contracts with PydanticAI; template usage
* [Snippets](snippets.md) — BaseModel, Field, validators, model_dump/validate, Settings cheat sheet
* [Alternatives](alternatives.md) — attrs/cattrs, dataclasses, marshmallow, TypedDict vs Pydantic

## Related

* [PydanticAI](../pydanticAI/index.md) — the agent framework built on this (v2.28.0)
* Template: `programs/pydantic/pydantic_ai_template.py`

# Citations

[1] [Pydantic docs](https://docs.pydantic.dev)
[2] [Pydantic GitHub](https://github.com/pydantic/pydantic)
[3] [Pydantic on PyPI](https://pypi.org/project/pydantic/)

## Last verified

**2026-08-13** — System pydantic 2.9.0, `programs/pydantic/.venv` 2.13.4 (2026-08-12 recon); template + notebook present, no source checkout.
