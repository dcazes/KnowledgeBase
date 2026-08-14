---
type: HowTo
title: Pydantic Configuration
description: Configure Pydantic models — model_config options, Field constraints, validators, aliases, BaseSettings env loading.
resource: https://docs.pydantic.dev
tags: [pydantic, configuration, settings, validators]
timestamp: 2026-08-13T00:00:00Z
---

# Configuration

## model_config

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(
        extra="forbid",          # reject unknown fields ("ignore" | "allow")
        frozen=True,             # immutable after creation
        strict=True,             # no type coercion
        validate_assignment=True,  # re-validate on attribute set
        str_strip_whitespace=True,
    )
    name: str
```

## Field constraints

```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    id: int = Field(..., gt=0, description="positive id")
    code: str = Field(..., pattern=r"^[A-Z]{3}$")
    tags: list[str] = Field(default_factory=list, max_length=10)
    role: Literal["admin", "editor", "viewer"] = "viewer"
```

## Validators

```python
from pydantic import BaseModel, field_validator, model_validator

class Order(BaseModel):
    qty: int

    @field_validator("qty")
    @classmethod
    def check_positive(cls, v):
        if v <= 0:
            raise ValueError("qty must be > 0")
        return v
```

## Settings (pydantic-settings)

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    ollama_host: str = "http://localhost:11434"

    model_config = {"env_prefix": "AGENT_"}   # reads AGENT_OPENAI_API_KEY etc.
```

# Citations

[1] [Pydantic docs — model_config](https://docs.pydantic.dev)
[2] [Pydantic docs — settings](https://docs.pydantic.dev/concepts/settings/)
