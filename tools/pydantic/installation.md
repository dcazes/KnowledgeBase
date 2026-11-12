---
type: Playbook
title: Pydantic Installation
description: Install Pydantic, optional extras for email validation and timezone data, and pydantic-settings for configuration.
resource: https://docs.pydantic.dev/latest/install/
tags: [pydantic, installation]
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

# Pydantic — Installation

```bash
uv add pydantic                       # or pip install pydantic
uv add "pydantic[email,timezone]"     # optional validators
uv add pydantic-settings              # settings from env vars and .env
python -c "import pydantic; print(pydantic.VERSION)"
```

## Related

[Pydantic index](index.md) · [Configuration](configuration.md)
