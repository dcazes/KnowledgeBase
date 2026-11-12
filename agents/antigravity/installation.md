---
type: Playbook
title: Antigravity Installation
description: Install the Antigravity 2.0 desktop app from antigravity.google and the Antigravity CLI with the official scripts, then sign in with a Google account or connect a GCP project.
resource: https://antigravity.google
tags: [antigravity, installation, cli]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: antigravity-site
    resource: "https://antigravity.google/"
    title: "Antigravity — official site"
    author: "site:antigravity.google"
  - id: agy-github
    resource: "https://github.com/google-antigravity/antigravity-cli"
    title: "google-antigravity/antigravity-cli"
    author: "site:github.com"
---

# Antigravity — Installation

## Desktop app

Download Antigravity 2.0 for your platform from antigravity.google and sign in with your Google account.

## CLI

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash          # macOS / Linux
```

```powershell
irm https://antigravity.google/cli/install.ps1 | iex                  # Windows PowerShell
```

Run `agy`. Authentication uses the system keyring, falling back to Google Sign-In (a browser locally, an authorisation URL over SSH). Enterprises connect a GCP project during onboarding.

Using the CLI shares interaction data with Google under its terms; check whether that suits your code.

## Related

[Antigravity index](index.md) · [Snippets](snippets.md)
