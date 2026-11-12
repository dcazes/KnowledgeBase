---
type: Playbook
title: Letta Installation
description: Install Letta Code with npm, uv or pipx, choose the cloud or local backend, connect your own model keys, and run the App Server for self-hosted agents.
resource: https://docs.letta.com/platform/cli
tags: [letta, installation, npm, uv, pipx, self-hosting]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: letta-code-github
    resource: "https://github.com/letta-ai/letta-code"
    title: "letta-ai/letta-code on GitHub"
    author: "site:github.com"
  - id: letta-docs
    resource: "https://docs.letta.com"
    title: "Letta documentation"
    author: "site:docs.letta.com"
---

# Letta — Installation

```bash
npm install -g @letta-ai/letta-code     # Node.js
uv tool install letta                   # or: pipx install letta  (Node.js is bundled; Python 3.9+)
```

Supported platforms: glibc Linux 2.28+ (x86-64/ARM64), macOS 14+, Windows x64. If `npm install -g` fails with `EACCES`, use uv/pipx, a user-owned npm prefix or nvm rather than `sudo` (root ownership breaks self-updates).

Other channels: AUR (`letta-code`, `letta-code-git`) and a Nix flake (`nix run github:letta-ai/letta-code`).

## First run

```bash
cd my-project
letta                                         # interactive terminal UI
letta --new-agent --personality tutorial      # guided tutorial agent
```

On first launch choose **Letta Cloud** (agent state stored by Letta) or **local**. Change later with `letta setup`, `letta backend cloud` or `letta backend local`.

Inside the UI, `/connect` adds your own LLM keys (OpenAI or ChatGPT, Anthropic, Z.ai and others) and `/model` switches models.

## Self-hosted App Server

```bash
letta server                                  # serve local or self-hosted agents
letta server --computer-name "work-laptop"    # register this machine as a remote computer (needs a Letta login)
```

## Related

[Letta index](index.md) · [Snippets](snippets.md) · [Self-hosting](../../concepts/self-hosting.md)
