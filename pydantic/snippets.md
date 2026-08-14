---
type: CheatSheet
title: Pydantic Snippets
description: Pydantic cheat sheet — BaseModel, Field, validators, dump/validate, Settings, JSON Schema export (v2).
resource: https://docs.pydantic.dev
tags: [pydantic, snippets, cheat-sheet]
timestamp: 2026-08-13T00:00:00Z
---

# Snippets

## Basic model

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    tags: list[str] = []

u = User(id=1, name="alice")
u.model_dump()               # {'id': 1, 'name': 'alice', 'tags': []}
u.model_dump_json()          # JSON string
```

## Validate from dict/JSON

```python
u2 = User.model_validate({"id": 2, "name": "bob"})
u3 = User.model_validate_json('{"id": 3, "name": "carol"}')
```

## Errors

```python
try:
    User(id="nope", name="x")
except ValidationError as e:
    print(e.errors())        # structured error list
```

## Field + constraints

```python
class Item(BaseModel):
    price: float = Field(..., gt=0, le=1000)
    sku: str = Field(..., pattern=r"^[A-Z]{2}\d{4}$")
```

## Copy / mutate

```python
u2 = u.model_copy(update={"name": "alicia"})
```

## JSON Schema (for LLM structured output)

```python
schema = User.model_json_schema()
```

## Settings

```python
from pydantic_settings import BaseSettings

class S(BaseSettings):
    api_key: str
    model_config = {"env_prefix": "MY_"}

s = S()          # reads MY_API_KEY from env
```

# Citations

[1] [Pydantic docs](https://docs.pydantic.dev)
