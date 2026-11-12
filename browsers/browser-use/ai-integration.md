---
type: Playbook
title: browser-use AI Integration
description: Where browser-use fits — giving coding agents a browser through its skill, embedding it in agent frameworks, choosing models, and the safety controls that matter when an LLM drives a logged-in browser.
resource: https://docs.browser-use.com
tags: [browser-use, integration, agents, security]
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

# browser-use — AI Integration

## Patterns

* **Coding agents:** the CLI skill lets [Claude Code](../../agents/claude-code/index.md) or [Codex](../../agents/codex/index.md) hand a web task to browser-use.
* **Framework tool:** call `Agent(...).run()` from a [LangGraph](../../agents/langgraph/index.md) node or a [PydanticAI](../../agents/pydanticAI/index.md) tool when a step needs a real browser.
* **Stealthier browsing:** point it at [CloakBrowser](../cloakbrowser/index.md) or a cloud browser when sites block automation (within their terms).

## Models

Browser tasks reward strong reasoning and code writing; small local models struggle on long tasks. Use a capable model and keep tasks narrow.

## Safety

* A browser agent with your logged-in profile can do anything you can — prefer a fresh or copied profile.
* Use `allowed_domains` and domain-scoped `sensitive_data`.
* Web pages can inject instructions; keep a human in the loop for purchases, messages and deletions. See [Agent security](../../concepts/agent-security.md).

## Related

[browser-use index](index.md) · [Browser automation](../../concepts/browser-automation.md)
