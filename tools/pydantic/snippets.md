---
type: Reference
title: Pydantic Snippets
description: Pydantic snippets — a model with constraints, validators, parsing LLM JSON output with retries in mind, generating a JSON Schema for a tool, and TypeAdapter.
resource: https://docs.pydantic.dev
tags: [pydantic, snippets, python, cheat-sheet]
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

# Pydantic — Snippets

```python
from typing import Literal
from pydantic import BaseModel, Field, field_validator, ValidationError, TypeAdapter

class Ticket(BaseModel):
    title: str = Field(description="Short summary of the issue", max_length=80)
    priority: Literal["low", "normal", "high"]
    tags: list[str] = []

    @field_validator("tags")
    @classmethod
    def lower(cls, v): return [t.lower() for t in v]

raw = '{"title": "Login fails on Safari", "priority": "high", "tags": ["Auth"]}'
try:
    ticket = Ticket.model_validate_json(raw)      # e.g. an LLM response
except ValidationError as e:
    print(e.errors())                             # feed back to the model and retry

print(Ticket.model_json_schema())                 # use as a tool / response schema

Tickets = TypeAdapter(list[Ticket])
Tickets.validate_python([{"title": "x", "priority": "low"}])
```

## Related

[Pydantic index](index.md) · [Structured output](../../concepts/structured-output.md)
