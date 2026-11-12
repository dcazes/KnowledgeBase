---
type: Playbook
title: LM Studio Installation
description: Install the LM Studio desktop app, bootstrap the lms CLI, start the local server, and run headless with llmster on Linux servers.
resource: https://lmstudio.ai/docs
tags: [lmstudio, installation, cli, llmster]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: lmstudio-docs
    resource: "https://lmstudio.ai/docs"
    title: "LM Studio documentation"
    author: "site:lmstudio.ai"
  - id: lms-github
    resource: "https://github.com/lmstudio-ai/lms"
    title: "lmstudio-ai/lms (CLI)"
    author: "site:github.com"
---

# LM Studio — Installation

1. Download the app for macOS, Windows or Linux from lmstudio.ai.
2. The `lms` CLI ships with the app. If it is not on PATH:

```bash
npx lmstudio install-cli
lms status
```

3. Start the server from the Developer tab or with `lms server start` (default `http://localhost:1234`).

## Headless (llmster)

For servers without a desktop, install **llmster** and run it as a startup task; it provides the same runtimes and API as the app. The docs include a systemd recipe for Linux.

## Related

[LM Studio index](index.md) · [Snippets](snippets.md)
