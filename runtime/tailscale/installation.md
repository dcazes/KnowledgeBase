---
type: Playbook
title: Tailscale Installation
description: Install Tailscale on desktops, phones and Linux servers, authenticate with auth keys for headless machines, and run it as a Docker sidecar to give a container its own tailnet identity.
resource: https://tailscale.com/kb/1031/install-linux
tags: [tailscale, installation, linux, docker, auth-keys]
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

# Tailscale — Installation

## Desktops and phones

Install the app from tailscale.com/download or your app store and sign in with your identity provider.

## Linux servers

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up                              # interactive login
sudo tailscale up --auth-key=tskey-auth-... --advertise-tags=tag:ai   # headless, tagged
tailscale status
```

Generate auth keys (reusable or one-off, optionally pre-tagged) in the admin console. Review install scripts before running them.

## Docker sidecar

Give a containerised app its own tailnet node so it is reachable as `https://webui.<tailnet>.ts.net`:

```yaml
services:
  ts-webui:
    image: tailscale/tailscale:latest
    hostname: webui
    environment:
      TS_AUTHKEY: ${TS_AUTHKEY}
      TS_STATE_DIR: /var/lib/tailscale
      TS_SERVE_CONFIG: /config/serve.json     # Serve config mapping 443 → http://127.0.0.1:8080
    volumes: [ts-state:/var/lib/tailscale, ./ts:/config]
    cap_add: [NET_ADMIN]
    devices: [/dev/net/tun]
  webui:
    image: ghcr.io/open-webui/open-webui:main
    network_mode: service:ts-webui
volumes: { ts-state: {} }
```

## Related

[Tailscale index](index.md) · [Snippets](snippets.md) · [Docker Compose](../docker/compose.md)
