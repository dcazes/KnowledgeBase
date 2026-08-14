---
type: Playbook
title: Installing Cursor
description: How to download, sign in to, and verify Cursor on your machine.
resource: https://cursor.com/download
tags: [cursor, install, setup, anysphere]
generated: { by: "human:daniel", at: "2026-07-09T04:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:00:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: cursor-download
    resource: "https://cursor.com/download"
    title: "Cursor Download"
    author: "site:cursor.com"
  - id: cursor-docs
    resource: "https://docs.cursor.com/"
    title: "Cursor Docs"
    author: "site:docs.cursor.com"
---

# Installing Cursor

Cursor ships as a desktop application for macOS, Windows, and Linux (AppImage / deb). It is installed by downloading from the official site and signing in with an account; there is no package-manager install that is guaranteed across platforms.

## Steps

1. **Download** the installer for your platform from `https://cursor.com/download`.
   - Linux: AppImage or `.deb` from the download page.
   - macOS: Universal `.dmg`.
   - Windows: `.exe` installer.
2. **Install / run** the downloaded artifact following your OS conventions (e.g. `chmod +x` the AppImage, or `sudo dpkg -i cursor*.deb`).
3. **Launch** Cursor and **sign in** with your Anysphere/Cursor account (email or SSO). Sign-in is required to use the cloud models and sync settings.
4. **Verify** the install from a terminal:

   ```bash
   cursor --version
   ```

   A successful run prints the Cursor and Electron/VS Code base version.

## Instance note

On this machine, **no local launcher for Cursor was found** in the programs list — it is not currently installed. The steps above document the upstream install flow; once installed, re-run `cursor --version` to confirm.

## Troubleshooting

- `cursor: command not found` — the CLI symlink is created on first launch; restart the terminal or add Cursor's bin directory to `PATH`.
- Sign-in fails — confirm network access to `cursor.com`; cloud models require an active account.
