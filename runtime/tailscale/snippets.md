---
type: Reference
title: Tailscale Snippets
description: Tailscale CLI cheat sheet — status and IPs, Serve and Funnel, SSH, exit nodes, subnet routes, file transfer, and an example ACL for AI services.
resource: https://tailscale.com/kb/1080/cli
tags: [tailscale, snippets, cli, acl, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: tailscale-docs
    resource: "https://tailscale.com/kb"
    title: "Tailscale knowledge base"
    author: "site:tailscale.com"
---

# Tailscale — Snippets

```bash
tailscale status                    # peers and connection type (direct / relay)
tailscale ip -4                     # this device's tailnet IP
tailscale ping gpu-box              # path check
tailscale serve --bg 3000           # HTTPS on the tailnet → localhost:3000
tailscale serve status ; tailscale serve reset
tailscale funnel --bg 3000          # public internet — think twice
tailscale ssh user@gpu-box
tailscale set --exit-node=home-router
sudo tailscale up --advertise-routes=192.0.2.0/24     # subnet router (example range)
tailscale file cp notes.md phone:
```

## Example policy: AI box reachable only by you

```json
{
  "tagOwners": { "tag:ai": ["autogroup:admin"] },
  "grants": [
    { "src": ["autogroup:member"], "dst": ["tag:ai"], "ip": ["443", "11434", "4000"] }
  ]
}
```

## Related

[Tailscale index](index.md) · [Concepts](concepts.md)
