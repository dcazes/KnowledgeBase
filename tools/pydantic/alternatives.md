---
type: Comparison
title: Pydantic Alternatives
description: Pydantic vs dataclasses, attrs/cattrs, marshmallow, TypedDict — data validation options for Python; when Pydantic wins.
resource: https://docs.pydantic.dev
tags: [pydantic, alternatives, dataclasses, comparison]
timestamp: 2026-08-13T00:00:00Z
---

# Alternatives

| Option | Model | Strengths | Fit here |
|---|---|---|---|
| **Pydantic** | typed schema validation | coercion, JSON Schema, Settings, ecosystem (FastAPI/PydanticAI) | the default everywhere in this stack |
| **dataclasses** | stdlib typed containers | zero deps, simple | no validation/coercion built in |
| **attrs + cattrs** | class transform + converters | flexible, mature | manual converter wiring |
| **marshmallow** | schema-based serialization | explicit schemas, serialization focus | older style; more boilerplate |
| **TypedDict** | dict typing | light annotations | type-hints only, no runtime validation |
| **msgspec** | fast binary/JSON | very fast, compact | performance-critical, smaller ecosystem |

## Choosing

* **Agent/API schemas + config** → Pydantic (ecosystem alignment with [PydanticAI](../../agents/pydanticAI/index.md) and FastAPI).
* **Zero-dependency simple containers** → dataclasses.
* **Max performance** → msgspec.
* **No runtime validation wanted** → TypedDict.

# Citations

[1] [Pydantic docs](https://docs.pydantic.dev)
