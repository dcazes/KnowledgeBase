---
type: Reference
title: browser-use Snippets
description: browser-use 1.0 snippets — default cloud run, local Chromium with your own or a local OpenAI-compatible model, typed output, secrets with domain scoping, domain restrictions and custom tools.
resource: https://github.com/browser-use/browser-use
tags: [browser-use, snippets, python, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: browser-use-github
    resource: "https://github.com/browser-use/browser-use"
    title: "browser-use/browser-use on GitHub"
    author: "site:github.com"
---

# browser-use — Snippets

## Default (cloud model and browser)

```python
from browser_use import Agent
print(Agent("Find the number of stars of the browser-use repo").run_sync().final_result())
```

## Local browser, your model

```python
from browser_use import Agent, Browser, ChatOpenAI

agent = Agent(
    "Find the cheapest flight from Lisbon to Berlin next Friday",
    llm=ChatOpenAI("qwen3:14b", base_url="http://localhost:11434/v1"),   # any OpenAI-compatible server
    browser=Browser("chromium", allowed_domains=["*.google.com", "*.kayak.com"]),
)
print(agent.run_sync().final_result())
```

`ChatAnthropic` and `ChatGoogle` are built in; any [PydanticAI](../../agents/pydanticAI/index.md) model string also works.

## Typed output and secrets

```python
from pydantic import BaseModel

class Invoice(BaseModel):
    vendor: str
    total_eur: float

agent = Agent("Log in and read my last invoice total", output_model_schema=Invoice,
              sensitive_data={"https://*.example.com": {"password": "..."}})
print(agent.run_sync().structured_output)
```

## Custom tool

```python
from browser_use import Tools
tools = Tools()

@tools.action("Save a note to disk")
def save_note(text: str) -> str:
    open("notes.txt", "a").write(text + "\n")
    return "saved"

Agent("Collect the top 3 headlines and save each as a note", tools=tools).run_sync()
```

## Related

[browser-use index](index.md) · [Overview](overview.md)
