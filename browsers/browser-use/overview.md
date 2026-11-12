---
type: Concept
title: browser-use Overview
description: How browser-use 1.0 works — code-writing agent over CDP in a persistent REPL, browser choices (cloud, fresh local Chromium, your own Chrome or profile), ultrafast accessibility-tree mode, structured output, uploads, downloads, secrets and domain limits.
resource: https://docs.browser-use.com
tags: [browser-use, overview, cdp, repl]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: browser-use-github
    resource: "https://github.com/browser-use/browser-use"
    title: "browser-use/browser-use on GitHub"
    author: "site:github.com"
  - id: browser-use-migrating
    resource: "https://github.com/browser-use/browser-use/blob/main/MIGRATING.md"
    title: "Migrating from 0.x"
    author: "site:github.com"
---

# browser-use — Overview

## Design

Earlier versions (0.x) asked the model to pick from a fixed action list each step. 1.0 lets the model **write Python** in a persistent REPL connected to Chrome over CDP: it can loop, branch, run JavaScript and combine actions in one step, then call `finish(result)`. This "code as action" approach mirrors how [coding agents](../../concepts/coding-agents.md) work and usually needs fewer model calls.

## Browsers

| Option | What the agent drives |
|---|---|
| `Browser()` | A Browser Use Cloud browser (default) |
| `Browser('chromium')` | A fresh local Chrome/Chromium/Edge with a temporary profile |
| `Browser('chrome')` | Your running Chrome with your logins (enable remote debugging) |
| `Browser('chrome', profile='Work')` | A temporary copy of a named Chrome profile |

## Features

* **Typed results:** `output_model_schema=MyModel` → `result.structured_output` ([structured output](../../concepts/structured-output.md)).
* **Secrets:** `sensitive_data={...}`, optionally scoped per domain; the model types placeholders and never sees the values.
* **Domain restrictions:** `allowed_domains`, `prohibited_domains`, `block_ip_addresses`.
* **Uploads and downloads** through a workspace folder.
* **Custom tools** via `@tools.action('description')`.
* **Ultrafast mode** acting on accessibility-tree ids; built-in web search (billed via Browser Use).
* Pin the exact version — the project moves fast.

## Related

[browser-use index](index.md) · [Snippets](snippets.md) · [Browser automation](../../concepts/browser-automation.md)
