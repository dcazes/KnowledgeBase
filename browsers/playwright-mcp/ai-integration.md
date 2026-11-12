---
type: Playbook
title: Playwright MCP AI Integration
description: Using Playwright MCP with AI — end-to-end test authoring and debugging in coding agents, web research from chat clients, local-model browsing in LM Studio or Open WebUI, and safety limits.
resource: https://github.com/microsoft/playwright-mcp
tags: [playwright-mcp, integration, testing, coding-agents]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: playwright-mcp-github
    resource: "https://github.com/microsoft/playwright-mcp"
    title: "microsoft/playwright-mcp on GitHub"
    author: "site:github.com"
---

# Playwright MCP — AI Integration

* **Testing:** coding agents ([Claude Code](../../agents/claude-code/index.md), [Cursor](../../editors/cursor/index.md), [VS Code](../../editors/vscode/index.md) Copilot) explore an app, reproduce a bug, then write Playwright tests using `browser_generate_locator`.
* **Research:** chat clients navigate docs and read pages the model could not fetch directly.
* **Local models:** add it to [LM Studio](../../runtime/lmstudio/index.md) or [Open WebUI](../../apps/openwebui/index.md) to let local models browse; choose models with solid [tool calling](../../concepts/tool-calling.md).
* **Hardened sites:** attach to a stealth browser with `--cdp-endpoint`, or use [Camofox](../camofox/index.md).

## Safety

Prefer `--isolated` profiles, restrict origins, and avoid `browser_run_code_unsafe` unless needed. Page content can contain prompt injection; require confirmation for irreversible actions ([Agent security](../../concepts/agent-security.md)).

## Related

[Playwright MCP index](index.md) · [Browser automation](../../concepts/browser-automation.md)
