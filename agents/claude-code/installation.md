---
type: Playbook
title: Claude Code Installation
description: Install Claude Code with the native installer (macOS, Linux, Windows), Homebrew or WinGet — npm is deprecated — then sign in with a Claude subscription, the Anthropic API, or a cloud provider.
resource: https://code.claude.com/docs/en/setup
tags: [claude-code, installation]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: claude-code-docs
    resource: "https://code.claude.com/docs/en/overview"
    title: "Claude Code documentation"
    author: "site:code.claude.com"
  - id: claude-code-github
    resource: "https://github.com/anthropics/claude-code"
    title: "anthropics/claude-code on GitHub"
    author: "site:github.com"
---

# Claude Code — Installation

```bash
curl -fsSL https://claude.ai/install.sh | bash        # macOS / Linux (recommended)
brew install --cask claude-code                       # Homebrew
```

```powershell
irm https://claude.ai/install.ps1 | iex               # Windows (recommended)
winget install Anthropic.ClaudeCode
```

Installing via `npm install -g @anthropic-ai/claude-code` still works but is **deprecated**.

```bash
cd my-project
claude            # sign in on first run
claude doctor     # check the installation
```

Authentication options: a Claude subscription, an Anthropic Console API key, or Amazon Bedrock / Google Vertex AI / Microsoft Foundry via environment variables.

## Related

[Claude Code index](index.md) · [Configuration](configuration.md)
