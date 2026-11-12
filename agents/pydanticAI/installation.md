---
type: Playbook
title: Pydantic AI Installation
description: Install Pydantic AI with uv or pip, choose the slim package with only the provider extras you need, and add the Harness, Evals or Logfire.
resource: https://pydantic.dev/docs/ai/
tags: [pydantic-ai, installation, uv, pip]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pydantic-ai-docs
    resource: "https://pydantic.dev/docs/ai/"
    title: "Pydantic AI documentation"
    author: "site:pydantic.dev"
---

# Pydantic AI — Installation

```bash
uv add pydantic-ai                                   # everything
uv add "pydantic-ai-slim[openai,anthropic]"          # only chosen providers
uv add "pydantic-ai-slim[mcp]"                       # MCP client support
uv add "pydantic-ai-harness[coder]"                  # coding-agent capabilities
uv add pydantic-evals logfire                        # evals and observability
uvx clai                                             # terminal chat with any model
```

Set provider keys as environment variables (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, …).

## Related

[Pydantic AI index](index.md) · [Configuration](configuration.md)
