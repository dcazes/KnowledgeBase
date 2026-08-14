---
type: Playbook
title: Antigravity 2.0 Snippets
description: Copy-paste snippets for Antigravity 2.0 — downloading/signing in, Antigravity CLI basics, and migrating from Gemini CLI. Conservative, web-verified commands only.
resource: Antigravity 2.0
tags: [google, antigravity, cli, snippets, migration, gemini-cli]
timestamp: 2026-07-09T03:28:00Z
---

# Antigravity 2.0 Snippets

Conservative, verified-as-of-2026-07-09 snippets. Antigravity is a newer product — treat exact CLI binary names and flags as **verify-before-use** against official docs; this page avoids asserting unverified commands.

## Download & sign in

```
# 1. Open the official site and confirm platform support (incl. Linux)
#    https://antigravity.google/
#    https://antigravity.google/product/antigravity-2
#    https://antigravity.google/download   <-- verify a Linux build exists

# 2. Download the Antigravity 2.0 desktop app for your platform

# 3. Launch and sign in with your Google account
#    (same identity as Google AI Pro/Ultra or Gemini Code Assist)
```

## Antigravity CLI basics

> The CLI surface is now **Antigravity CLI**, the successor to Gemini CLI. Exact binary name / subcommands should be confirmed from official docs; the shape below is illustrative.

```
# Check the CLI is available (verify the real binary name first)
antigravity --help
antigravity --version

# Authenticate with your Google account
# (follow the official auth flow / sign-in prompt)

# Create / run an agent in its sandbox (see agents.md for the model)
# antigravity agents create <name>
# antigravity agents run <name>
```

## Migrate from Gemini CLI

Context: on **June 18, 2026**, Gemini CLI and Gemini Code Assist IDE extensions stopped serving requests for Google AI Pro/Ultra and free Gemini Code Assist for individuals.

```
# OLD (deprecated after 2026-06-18):
#   gemini            # Gemini CLI
#   Gemini Code Assist IDE extension

# NEW (migration target):
#   antigravity       # Antigravity CLI
#   Antigravity 2.0 desktop app

# Action: export any relevant config/scripts that called `gemini`,
# then reinstall auth under Antigravity CLI with your Google account.
```

## Verify after setup

- [ ] Desktop app launches and shows your signed-in Google account.
- [ ] CLI binary responds to `--help` / `--version`.
- [ ] A test agent runs inside its sandbox successfully.
- [ ] Old `gemini`/Code Assist individual requests are confirmed deprecated.

## Related

- [Installation](installation.md)
- [Agents](agents.md)
- Migration source: [Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)

# Citations
[1] [Antigravity — official site](https://antigravity.google/)
[2] [Antigravity 2.0 product page](https://antigravity.google/product/antigravity-2)
[3] [Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
