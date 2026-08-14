---
type: Playbook
title: Frigate — Installation
description: Deploying Frigate via the local docker-compose.yml (stable image, ports, NVIDIA GPU, storage).
resource: https://docs.frigate.video/installation/
tags: [frigate, install, docker-compose, gpu, ports, storage]
generated: { by: "human:daniel", at: "2026-07-09T04:16:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:16:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: install-docs
    resource: "https://docs.frigate.video/installation/"
    title: "Install docs"
    author: "site:docs.frigate.video"
  - id: local-compose
    resource: "/../../programs/frigate/docker-compose.yml"
    title: "Local compose"
  - id: configuration
    resource: "configuration.md"
    title: "Configuration"
---

# Frigate — Deploy (this machine)

From `programs/frigate/`:
```bash
docker compose -f docker-compose.yml up -d
```

The active compose uses `ghcr.io/blakeblackshear/frigate:stable` with:
* `privileged: true` (hardware/driver access)
* `shm_size: "256mb"`
* NVIDIA GPU device reservation (`deploy.resources`)
* tmpfs `/tmp/cache` (1GB, reduces drive wear)

# Ports

| Port | Purpose |
|------|---------|
| `8971` | **Authenticated UI & API** (no TLS — reverse proxies terminate TLS here) |
| `5000` | Internal unauthenticated UI & API (limit access; for in-network services) |
| `8554` | RTSP re-stream |
| `8555/tcp` + `8555/udp` | WebRTC |

# Volumes

* `config.yml` → `/config/config.yml`
* `/media/daniel/New Volume/frigate` → `/media/frigate` (recordings)
* `/etc/localtime` (timezone)
* tmpfs `/tmp/cache` (1GB)

# Verify

```bash
docker ps | grep frigate
curl -sk -o /dev/null -w "%{http_code}\n" https://localhost:8971
```

# ⚠️ Security

The compose sets `FRIGATE_RTSP_PASSWORD` and `config.yml` holds the **camera password in plaintext**. Keep both out of the KB; rotate if exposed.

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| UI unreachable | container down | `docker start frigate` |
| No detection | GPU/detector misconfig | check detector type + `preset-nvidia` |
| Camera offline | go2rtc/creds | verify `go2rtc` streams + redacted creds |
| Drive wear | recordings | tmpfs cache helps; point storage at fast disk |
