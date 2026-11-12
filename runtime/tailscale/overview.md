---
type: Concept
title: Tailscale Overview
description: How Tailscale works — a coordination server distributing WireGuard keys and policy, peer-to-peer encrypted connections with NAT traversal, DERP relays as fallback, and identity-based access.
resource: https://tailscale.com/blog/how-tailscale-works
tags: [tailscale, overview, wireguard, nat-traversal, derp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: tailscale-docs
    resource: "https://tailscale.com/kb"
    title: "Tailscale knowledge base"
    author: "site:tailscale.com"
  - id: how-it-works
    resource: "https://tailscale.com/blog/how-tailscale-works"
    title: "How Tailscale works"
    author: "site:tailscale.com"
---

# Tailscale — Overview

## Architecture

* **Coordination server** (Tailscale's control plane, or self-hosted Headscale) authenticates devices through your identity provider and distributes public keys, IP addresses and access policy. It never sees your traffic.
* **Data plane**: devices connect **directly** to each other with WireGuard, using NAT traversal to punch through home routers and firewalls.
* **DERP relays** carry encrypted traffic when a direct path is impossible.

Each device gets a stable private address and a MagicDNS name, so `http://gpu-box:11434` works from any device in the tailnet regardless of physical network.

## Why it suits self-hosted AI

* No open ports on the router, no public exposure of services that lack authentication (like [Ollama](../ollama/index.md) or [SearXNG](../searxng/index.md)).
* Access rules by user, group and device tag: "only my laptop and phone can reach the GPU box".
* Works the same from home, office, mobile data and cloud VMs.

## Related

[Tailscale index](index.md) · [Concepts](concepts.md) · [Self-hosting](../../concepts/self-hosting.md)
