---
type: Playbook
title: VS Code Installation
description: Install VS Code on Windows, macOS or Linux (deb/rpm repos, snap), enable the code CLI, and set up Copilot or alternative AI extensions.
resource: https://code.visualstudio.com/download
tags: [vscode, installation]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: vscode-site
    resource: "https://code.visualstudio.com"
    title: "Visual Studio Code"
    author: "site:code.visualstudio.com"
---

# VS Code — Installation

* **Windows / macOS:** installer from code.visualstudio.com.
* **Linux:** `.deb` / `.rpm` packages (which add Microsoft's repository for updates), snap, or tarball.
* **CLI:** `code .` opens a folder; on macOS run *Shell Command: Install 'code' command in PATH*.
* **VSCodium** offers Microsoft-telemetry-free builds of the same source, using Open VSX.

Then sign in to GitHub for Copilot, or install other AI extensions ([Claude Code](../../agents/claude-code/index.md), [Codex](../../agents/codex/index.md)).

## Related

[VS Code index](index.md) · [Snippets](snippets.md)
