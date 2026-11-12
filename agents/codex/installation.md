---
type: Playbook
title: Codex Installation
description: Install Codex CLI with the official installers, npm or Homebrew, or download release binaries; then sign in with ChatGPT or configure an API key.
resource: https://github.com/openai/codex
tags: [codex, installation]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: codex-github
    resource: "https://github.com/openai/codex"
    title: "openai/codex on GitHub"
    author: "site:github.com"
---

# Codex — Installation

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh                 # macOS / Linux
npm install -g @openai/codex
brew install --cask codex
```

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"   # Windows
```

Release archives (e.g. `codex-x86_64-unknown-linux-musl.tar.gz`) contain a single binary; rename it to `codex`.

Run `codex`, choose **Sign in with ChatGPT** to use your plan, or set up an API key. IDE users can install the extension for VS Code, Cursor or Windsurf instead.

## Related

[Codex index](index.md) · [Snippets](snippets.md)
