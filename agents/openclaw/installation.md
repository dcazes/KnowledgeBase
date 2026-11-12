---
type: Playbook
title: OpenClaw Installation
description: Install OpenClaw with the official installer on macOS, Linux, WSL2 or Windows, or with npm on a supported Node.js; run onboarding, install the daemon and open the Control UI.
resource: https://docs.openclaw.ai/install
tags: [openclaw, installation, npm, onboarding]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openclaw-github
    resource: "https://github.com/openclaw/openclaw"
    title: "openclaw/openclaw on GitHub"
    author: "site:github.com"
  - id: openclaw-docs
    resource: "https://docs.openclaw.ai"
    title: "OpenClaw documentation"
    author: "site:docs.openclaw.ai"
---

# OpenClaw — Installation

```bash
curl -fsSL https://openclaw.ai/install.sh | bash          # macOS, Linux, WSL2
```

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex            # Windows
```

The installer provisions Node.js if needed and starts onboarding. With your own Node (24.16+ or 26.1+):

```bash
npm install -g openclaw@latest --allow-scripts=openclaw     # npm 11.16+/12
openclaw onboard --install-daemon
openclaw gateway status
openclaw dashboard
```

Onboarding verifies model access, creates the workspace and configures the Gateway. Docker and Nix deployments are documented.

## Related

[OpenClaw index](index.md) · [Snippets](snippets.md)
