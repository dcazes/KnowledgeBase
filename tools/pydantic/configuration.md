---
type: Reference
title: Pydantic Configuration
description: Model-level configuration with ConfigDict (strictness, extra fields, aliases, frozen models) and application settings with pydantic-settings — environment variables, .env files, nested settings and secrets.
resource: https://docs.pydantic.dev/latest/concepts/pydantic_settings/
tags: [pydantic, configuration, settings, env]
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

# Pydantic — Configuration

## Model config

```python
from pydantic import BaseModel, ConfigDict

class Event(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True, populate_by_name=True)
    name: str
```

`extra="forbid"` is useful for LLM outputs: unexpected keys become errors instead of silent data.

## Settings

```python
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")
    openai_api_key: SecretStr
    ollama_url: str = "http://localhost:11434"
    max_tokens: int = 2000

settings = Settings()          # reads APP_OPENAI_API_KEY etc.
```

`SecretStr` keeps keys out of logs and reprs.

## Related

[Pydantic index](index.md) · [Snippets](snippets.md)
