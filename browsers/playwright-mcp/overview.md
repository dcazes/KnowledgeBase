---
type: Concept
title: Playwright MCP Overview
description: How Playwright MCP works — accessibility snapshots and refs, its tool families (navigation, input, forms, storage, network, tracing, code generation), optional vision/pdf/devtools capabilities, and when the Playwright CLI with skills is the better fit.
resource: https://github.com/microsoft/playwright-mcp
tags: [playwright-mcp, overview, tools, accessibility-tree]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: playwright-mcp-github
    resource: "https://github.com/microsoft/playwright-mcp"
    title: "microsoft/playwright-mcp on GitHub"
    author: "site:github.com"
  - id: playwright-cli
    resource: "https://github.com/microsoft/playwright-cli"
    title: "microsoft/playwright-cli"
    author: "site:github.com"
---

# Playwright MCP — Overview

## Snapshot-first

`browser_snapshot` returns the page's accessibility tree with refs; tools like `browser_click` and `browser_type` take those refs. No pixels, no coordinates — fast, cheap and deterministic. Screenshots and coordinate tools exist for edge cases (`--caps vision`).

## Tool families

| Family | Examples |
|---|---|
| Navigation | `browser_navigate`, `browser_navigate_back`, tabs, waits |
| Input | `browser_click`, `browser_type`, `browser_press_key`, `browser_select_option`, `browser_drag`, `browser_hover` |
| Forms and files | `browser_fill_form`, `browser_file_upload`, `browser_handle_dialog` |
| Reading | `browser_snapshot`, `browser_find`, `browser_console_messages`, `browser_network_requests` |
| State | cookies, localStorage and sessionStorage get/set/clear, `browser_set_storage_state` |
| Network | `browser_route` (mock or block requests), network state emulation |
| Debugging | tracing, video recording, `browser_generate_locator`, `browser_pdf_save` |
| Escape hatches | `browser_evaluate`, `browser_run_code_unsafe` |

## MCP or CLI + skills?

Microsoft notes that **coding agents** increasingly prefer the Playwright CLI exposed as [skills](../../concepts/agent-skills.md), because CLI calls avoid loading large tool schemas and snapshots into context. MCP remains better for exploratory, stateful loops that reason over page structure across many steps. This trade-off — tool schemas cost tokens — is a general [context engineering](../../concepts/context-engineering.md) concern with MCP.

## Related

[Playwright MCP index](index.md) · [Snippets](snippets.md) · [MCP](../../concepts/mcp.md)
