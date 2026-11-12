---
type: Playbook
title: Camofox Usage
description: Working with Camofox — creating tabs, navigating, reading accessibility snapshots, acting on element refs, search macros, sessions and cookies, extraction and paging through large pages.
resource: https://github.com/jo-inc/camofox-browser
tags: [camofox, usage, workflow, browser-automation]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: camofox-github
    resource: "https://github.com/jo-inc/camofox-browser"
    title: "jo-inc/camofox-browser on GitHub"
    author: "site:github.com"
---

# Camofox — Usage

## The loop

1. **Create a tab** (optionally in a named session with its own cookies).
2. **Navigate** to a URL or run a search macro such as `@google_search`.
3. **Snapshot** the page — an accessibility tree where interactive elements carry refs (`e1`, `e2`…).
4. **Act** on refs: click, type, press, select, scroll, drag, upload.
5. **Snapshot again** and repeat; use offsets to page through large snapshots.
6. **Extract** structured data with a JSON Schema mapped to refs, or take a screenshot.

## Tool groups (MCP / OpenClaw)

* Tabs and navigation: `camofox_create_tab`, `camofox_navigate`, `camofox_back`, `camofox_refresh`…
* Reading: `camofox_snapshot`, `camofox_links`, `camofox_table_rows`, `camofox_extract`, `camofox_screenshot`
* Interacting: `camofox_click`, `camofox_type`, `camofox_press`, `camofox_select`, `camofox_scroll`, `camofox_upload`
* State: `camofox_import_cookies`, `camofox_export_storage_state`, `camofox_evaluate`

## Authenticated sites

Log in once through the noVNC view, export storage state, and import it into the agent's session — the agent never sees the password. See [Agent security](../../concepts/agent-security.md).

## Related

[Camofox index](index.md) · [Snippets](snippets.md)
