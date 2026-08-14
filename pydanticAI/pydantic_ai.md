---
type: Reference
title: Pydantic AI v2
description: Python library for AI-oriented agent development, featuring a capability-first design and a leaner core since the v2 architecture.
resource: https://pydantic.dev/articles/pydantic-ai-v2
tags: [pydantic, ai, agents, python, library]
timestamp: 2026-08-12T00:00:00Z
---

# Pydantic AI v2

## Overview
Pydantic AI v2 is a stable release that introduces a capability‑first architecture, a single primitive that bundles an agent’s instructions, tools, lifecycle hooks, and model settings. It streamlines the agent loop and reduces breaking changes.

## Release Summary
- V2 architecture introduced June 23, 2024 (stable after seven betas).
- **Current version: v2.29.0** (requires Python 3.10+, `pydantic>=2.12`). Security: v2.28.0 patches **GHSA-h4xc-3qfq-jf93** (High — web chat UI CSRF/origin validation; no CVE assigned) — upgrade from earlier 2.x.
- Core is leaner; no breaking changes within a major version; deprecations are announced well before removal.

## Key Features
- **Capability primitive** – a single composable unit that bundles instructions, tools, hooks, and model settings.  
- **Harness‑first architecture** – core stays small; memory, guardrails, context management, file‑system access, code mode, etc., live in the Harness.  
- **Native tool support** – WebSearch, WebFetch, and MCP run natively when the provider supports them, with automatic fallbacks.  
- **Instrumentation v5** – includes aggregated token‑usage attributes.  
- **Function tools** now run alongside successful output tool (`end_strategy='graceful'`).  
- **Upgrade path** – upgrade to latest v1, clear deprecation warnings, then adjust model names and capability definitions.

## Installation
```bash
uv add pydantic-ai        # or
pip install "pydantic-ai"
```
Python 3.10+ is required.

## Quick‑Start Guide
```python
from pydantic_ai import Agent
from pydantic_ai.capabilities import Thinking, WebSearch, Capability
from pydantic_ai.mcp import MCPToolset

agent = Agent(
    "anthropic:claude-opus-4-7",
    instructions="Research thoroughly and cite your sources.",
    capabilities=[
        Thinking(effort="high"),
        WebSearch(),
        Capability(
            id="github",
            description="Lookup GitHub issues and PRs.",
            instructions="Use GitHub tools for repository questions.",
            toolset=MCPToolset("https://mcp.example.com/github"),
            defer_loading=True,
        ),
    ],
)

print(agent.run("What is the capital of France?"))
```

## API Changes (v1 → v2)
- Model names now use the Responses API (`openai-chat:` instead of `openai:`).  
- Capability registration uses the `Capability` class with optional `defer_loading=True`.  
- End‑strategy defaults changed; `end_strategy='graceful'` runs tools alongside output.  
- Instrumentation version bumped to v5.

## Migration Guide
1. Upgrade to the latest v1 and clear all deprecation warnings.  
2. Replace old model‑name imports with the new `Responses`‑based names.  
3. Rewrite capability definitions using the `Capability` class and set `defer_loading=True` where needed.  
4. Review end‑strategy and instrumentation changes; adjust code accordingly.  
5. Run your test suite; most code should work unchanged after the above steps.

## Example Usage
```python
# Minimal agent that prints a result
from pydantic_ai import Agent

agent = Agent("gpt-4", instructions="Say hello.")
print(agent.run())
```

## FAQ
- **Performance:** v2 is faster thanks to a leaner core and lazy loading of capabilities.  
- **Async support:** Capabilities can be async; use `await` on tool calls.  
- **Supported providers:** OpenAI, Anthropic, local LLMs (e.g., Ollama), and community‑provided back‑ends.  
- **Licensing:** MIT.

# Citations

[1] [Pydantic AI release notes](https://github.com/pydantic/pydantic-ai/releases)
[2] [Pydantic AI v2 overview](https://pydantic.dev/articles/pydantic-ai-v2)
[3] [Installation guide](https://pydantic.dev/docs/ai/overview/install/)
[4] [GHSA-h4xc-3qfq-jf93 — High: web chat UI CSRF (patched in 2.28.0)](https://github.com/pydantic/pydantic-ai/security/advisories/GHSA-h4xc-3qfq-jf93)