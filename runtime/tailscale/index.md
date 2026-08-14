---
type: Reference
title: Tailscale
description: Zero Trust, identity-based mesh networking over WireGuard that connects devices, servers, clouds, and AI workloads without port forwarding.
resource: https://tailscale.com/
tags: [tailscale, vpn, mesh, wireguard, zero-trust, networking, tailnet]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: tailscale-official
    resource: "https://tailscale.com/"
    title: "Tailscale official"
    author: "site:tailscale.com"
  - id: local-dir-programs-tailscale-tailscale
    resource: "/../../programs/tailscale/tailscale"
    title: "Local dir - programs/tailscale/tailscale"
---

# Tailscale

A **Zero Trust, identity-based connectivity platform** that builds a private mesh overlay network (a *tailnet*) across your devices, servers, clouds, and AI workloads — replacing legacy VPNs. On this machine it can securely expose your local services (`:4000` LiteLLM proxy, `:3001` OpenWebUI, `:8088` SearXNG) to your other devices without opening ports.

## Contents

* [Overview](overview.md) - what Tailscale is, how it fits
* [Installation](installation.md) - install the client, `tailscale up`, auth
* [Concepts](concepts.md) - tailnet, WireGuard, MagicDNS, DERP, ACLs, exit nodes, funnel
* [AI Integration](ai-integration.md) - secure access to your AI stack + Aperture
* [Alternatives](alternatives.md) - WireGuard, Headscale, ZeroTier, OpenVPN, Cloudflare Tunnel
* [Snippets](snippets.md) - cheat sheet

## Instance facts

* **Local dir:** `programs/tailscale/tailscale` (Tailscale client/scripts)
* **Version:** stable **v1.102.2** (2026-08-04)
* **Role here:** private mesh to reach local services from other devices; zero-trust access to AI agents
* **Upstream:** Zero Trust connectivity platform (WireGuard-based)

## Cross-references

* **SearXNG** — expose on tailnet via funnel/serve — see [SearXNG Installation](../searxng/installation.md)
* **OpenWebUI** — access from phone/laptop via Tailscale IP — see [OpenWebUI Installation](../../apps/openwebui/installation.md)
* **Firecrawl / Dify / AnythingLLM** — expose internal ports securely — see respective installation docs
* **:4000 OpenRouter proxy** — expose to tailnet for remote agent access — see [Graphify AI Integration](../../memory/graphify/ai-integration.md)
* **Hermes** — can run on any tailnet device — see [Hermes Overview](../../agents/hermes/overview.md)

## Last verified

**2026-08-12** — Client config, funnel/serve concepts, and AI stack exposure patterns verified against upstream tailscale.com/kb. Stable v1.102.2 (2026-08-04).
