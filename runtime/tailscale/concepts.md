---
type: Concept
title: Tailscale Concepts
description: Tailscale building blocks — MagicDNS, ACLs and grants, tags, Tailscale Serve and Funnel, Tailscale SSH, exit nodes, subnet routers, tsidp and golink.
resource: https://tailscale.com/kb
tags: [tailscale, concepts, acl, serve, funnel, ssh]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: tailscale-docs
    resource: "https://tailscale.com/kb"
    title: "Tailscale knowledge base"
    author: "site:tailscale.com"
  - id: tsidp
    resource: "https://github.com/tailscale/tsidp"
    title: "tailscale/tsidp"
    author: "site:github.com"
  - id: golink
    resource: "https://github.com/tailscale/golink"
    title: "tailscale/golink"
    author: "site:github.com"
---

# Tailscale — Concepts

| Concept | What it does |
|---|---|
| MagicDNS | Device names resolve automatically inside the tailnet; HTTPS certificates available for `*.ts.net` names |
| ACLs / grants | A policy file (HuJSON) deciding which users, groups and tags can reach which devices and ports |
| Tags | Identities for servers (`tag:gpu`, `tag:ai`) so access does not depend on a person's account |
| **Serve** | Publish a local port to the tailnet with automatic HTTPS: `tailscale serve 3000` |
| **Funnel** | Publish a port to the **public internet** through Tailscale — use sparingly, and only for services with their own auth |
| Tailscale SSH | SSH authenticated by tailnet identity, no keys to manage |
| Exit node | Route all internet traffic through a chosen device |
| Subnet router | Expose a whole LAN to the tailnet without installing Tailscale on every device |
| tsidp | An OIDC/OAuth identity provider for the tailnet — single sign-on for self-hosted apps |
| golink | Private short links (`go/webui`) for the tailnet |

## Related

[Tailscale index](index.md) · [Snippets](snippets.md) · [AI Integration](ai-integration.md)
