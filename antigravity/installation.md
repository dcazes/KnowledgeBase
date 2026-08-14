---
type: Playbook
title: Installing Antigravity 2.0
description: How to get the Antigravity 2.0 desktop app and Antigravity CLI — download, sign in with a Google account, and verify the install. Includes a Linux platform-availability caveat.
resource: Antigravity 2.0
tags: [google, antigravity, install, cli, gemini, linux]
timestamp: 2026-07-09T03:28:00Z
---

# Installing Antigravity 2.0

> **Caveat:** Antigravity is a newer product. Confirm current platform support (including Linux) on the official download page before relying on a desktop build for your OS. This playbook documents the expected flow from official sources; treat exact download URLs/installer names as verify-before-use.

## Steps

1. **Open the official site.**
   Go to `https://antigravity.google/` and follow the link to the download / product page (`antigravity.google/download` or `antigravity.google/product/antigravity-2`).

2. **Verify platform support.**
   Confirm a build exists for your OS. The user runs **Linux** — check explicitly that a Linux desktop build is offered. If none is listed, note it as unavailable rather than assuming parity with macOS/Windows.

3. **Download the desktop app.**
   Download the Antigravity 2.0 desktop application installer for your platform.

4. **Install and launch.**
   Run the installer / app bundle and launch Antigravity 2.0.

5. **Sign in with your Google account.**
   Authenticate with a Google account (the same identity used for Google AI Pro/Ultra or Gemini Code Assist). This is the migration target from the deprecated Gemini CLI / Code Assist individual tiers.

6. **Install / use the Antigravity CLI.**
   The command-line surface is now **Antigravity CLI** (successor to Gemini CLI). Install it per the official instructions and authenticate with the same Google account.

## Verify

- [ ] Antigravity 2.0 desktop app launches and shows your signed-in Google account.
- [ ] `antigravity` (or the documented CLI binary name) is on your `PATH` and responds to `--help` / a version command.
- [ ] A test agent can be created and run inside its sandbox (per [agents.md](agents.md)).
- [ ] Before June-18-2026-era tooling: confirm Gemini CLI / Code Assist individual requests are deprecated and you are on Antigravity CLI instead.

> Do not assert a successful live install in this KB — verification is left as a step for the user to run.

## Related

- [Overview](overview.md)
- [Agents](agents.md)
- Migration context: [Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)

# Citations
[1] [Antigravity — official site](https://antigravity.google/)
[2] [Antigravity 2.0 product page](https://antigravity.google/product/antigravity-2)
[3] [Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
