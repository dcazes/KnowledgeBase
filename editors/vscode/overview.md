---
type: Software
title: VSCode — Overview
description: Free open-source AI code editor (VS Code / Code-OSS) — architecture, editions, and its role editing your programs/* repos and agent skills.
resource: https://code.visualstudio.com/
tags: [vscode, editor, ide, code-oss, ai, copilot, development]
generated: { by: "human:daniel", at: "2026-07-09T02:10:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T02:10:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: vs-code-official
    resource: "https://code.visualstudio.com/"
    title: "VS Code official"
    author: "site:code.visualstudio.com"
  - id: vscodium-code-oss-build
    resource: "https://vscodium.com/"
    title: "VSCodium (Code-OSS build)"
    author: "site:vscodium.com"
  - id: local-launcher
    resource: "/../../programs/VSCode.desktop"
    title: "Local launcher"
---

# What VSCode is

**Visual Studio Code** is a free, open-source AI code editor from Microsoft, built on the open-source **Code - OSS** core (Electron + TypeScript). It's the most common editor for working across language stacks and, increasingly, for AI-assisted and agent-driven development.

# Architecture

* **Core:** Code-OSS (MIT-licensed). Microsoft's download bundles proprietary extras (telemetry, some icons/fonts).
* **Runtime:** Electron (Chromium + Node.js). Language servers run out-of-process.
* **Extensions:** a massive marketplace extends languages, debuggers, and AI features. Extensions are JS/TS and run in extension hosts.
* **Settings:** `settings.json` (user + workspace/folder scope), `keybindings.json`, and `.vscode/` per-project config.

# Editions

| | License | Notes |
|--|---------|-------|
| **Code - OSS** | MIT | Pure open source; no MS telemetry/branding |
| **VS Code** (download) | MS EULA | Adds telemetry, proprietary assets |
| **VSCodium** | MIT | Code-OSS build, telemetry stripped |

# Role in this stack

VSCode is the **editor** for:
* Your `programs/*` source repos — Dify, Firecrawl, SearXNG, Camofox, CloakBrowser, etc.
* **Agent skills** you author (Graphify packs, Hermes/OpenCode skills).
* General notes/config in the vault and `kbv2/`.

It is *not* a runtime itself — it launches the tools (Docker, Node, Git) that actually build/run the stack.
