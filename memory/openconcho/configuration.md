---
type: Reference
title: OpenConcho Configuration
description: Connecting OpenConcho to Honcho instances, optional auth tokens, and the Docker proxy's environment variables including the SSRF upstream allowlist.
resource: https://github.com/offendingcommit/openconcho/blob/main/docs/docker.md
tags: [openconcho, configuration, security, proxy]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openconcho-github
    resource: "https://github.com/offendingcommit/openconcho"
    title: "offendingcommit/openconcho on GitHub"
    author: "site:github.com"
---

# OpenConcho — Configuration

## Connecting

1. Enter the Honcho base URL, e.g. `http://localhost:8000`.
2. Optionally add an API token.
3. **Test connection** — the health check detects whether auth is required.
4. **Save**. Add more instances any time and switch between them.

## Docker proxy variables

| Variable | Purpose |
|---|---|
| `OPENCONCHO_DEFAULT_HONCHO_URL` | Seeds the first instance (absolute URL) |
| `OPENCONCHO_UPSTREAM_ALLOWLIST` | Comma-separated host globs the proxy may reach — set it whenever the proxy is exposed, to prevent server-side request forgery |

The browser calls `/api` on the same origin and names the upstream in an `X-Honcho-Upstream` header.

## Security notes

The UI can read every memory in the connected workspace. Keep it on a private network (for example behind [Tailscale](../../runtime/tailscale/index.md)) or behind authentication, and use demo mode when sharing screens. See [Agent security](../../concepts/agent-security.md).

## Related

[OpenConcho index](index.md) · [Installation](installation.md)
