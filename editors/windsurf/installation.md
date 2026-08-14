---
type: Playbook
title: Windsurf — Installation
description: Downloading Windsurf, signing in with Codeium, and verifying the install.
resource: https://docs.windsurf.com/
tags: [windsurf, install, codeium, login, setup]
generated: { by: "human:daniel", at: "2026-07-09T03:31:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T03:31:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: download
    resource: "https://windsurf.com/download"
    title: "Download"
    author: "site:windsurf.com"
  - id: docs
    resource: "https://docs.windsurf.com/"
    title: "Docs"
    author: "site:docs.windsurf.com"
---

# Install

Download the Windsurf app from **windsurf.com** (or your package manager / package for your OS). Codeium provides builds for Linux, macOS, and Windows.

```bash
# Linux (example via package manager / .deb); exact command depends on distro
# See https://windsurf.com/download
windsurf            # launch after install
```

# Sign in

On first launch, sign in with your **Codeium** account (or your org.s SSO). This enables Devin Local (formerly Cascade) and the SWE-1 models.

# Verify

```bash
windsurf --version      # if a CLI is available
# or: open the app, confirm Devin Local is reachable in the sidebar
```

# Notes

* No launcher was found in `programs/` on this machine — install when you want it.
* A Codeium account (free tier available) is required for AI features.

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Won't launch | not installed | download from windsurf.com |
| Devin Local offline | not signed in | sign in with Codeium |
| Model errors | plan/quota | check Codeium account tier |
