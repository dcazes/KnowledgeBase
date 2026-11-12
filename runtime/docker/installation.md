---
type: Playbook
title: Docker Installation
description: Install Docker Engine on Linux from Docker's apt repository or Docker Desktop on macOS, Windows and Linux; post-install steps for non-root use, rootless mode, and verification.
resource: https://docs.docker.com/engine/install/
tags: [docker, installation, linux, desktop]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: docker-docs
    resource: "https://docs.docker.com"
    title: "Docker documentation"
    author: "site:docs.docker.com"
---

# Docker — Installation

## Docker Engine on Linux (Ubuntu/Debian)

```bash
sudo apt-get update && sudo apt-get install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Optional: `docker-model-plugin` adds `docker model` on Engine.

## Docker Desktop

Download the installer for macOS, Windows or Linux from docker.com. Desktop bundles Engine, Compose, BuildKit, Model Runner, the MCP Toolkit and Docker Agent. Larger companies need a paid subscription.

## Post-install (Linux)

```bash
sudo usermod -aG docker $USER      # run docker without sudo (log out and back in)
sudo systemctl enable --now docker
```

Membership of the `docker` group is effectively root access. **Rootless mode** (`dockerd-rootless-setuptool.sh install`) avoids that at the cost of some features.

## Verify

```bash
docker version
docker compose version
docker run --rm hello-world
```

## Related

[Docker index](index.md) · [Snippets](snippets.md) · [GPU & AI](gpu-ai.md)
