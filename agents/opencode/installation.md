---
type: Playbook
title: OpenCode Installation
description: Install OpenCode with the install script, npm, Homebrew, pacman/AUR, mise or Nix, or the desktop app; then connect a provider.
resource: https://opencode.ai/docs
tags: [opencode, installation]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: opencode-github
    resource: "https://github.com/anomalyco/opencode"
    title: "anomalyco/opencode on GitHub"
    author: "site:github.com"
---

# OpenCode — Installation

```bash
curl -fsSL https://opencode.ai/v2/install | bash     # installs to ~/.opencode/bin
npm i -g @opencode/cli@latest                        # or bun / pnpm / yarn
brew install anomalyco/tap/opencode-v2               # macOS/Linux, always current
brew install opencode                                # official formula, updated less often
sudo pacman -S opencode                              # Arch
mise use -g opencode
nix run github:anomalyco/opencode
```

Desktop (beta): `brew install --cask opencode-desktop` or download for macOS, Windows and Linux from opencode.ai/download. Remove versions older than 0.1.x first.

## First run

```bash
cd my-project
opencode            # TUI
/connect            # add a provider key, or sign in with a supported subscription
/init               # generate AGENTS.md for the project
```

## Related

[OpenCode index](index.md) · [Configuration](configuration.md)
