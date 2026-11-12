---
type: Playbook
title: Frigate Installation
description: Install Frigate with Docker Compose — choose the image for your accelerator, pass through devices, size shared memory, mount config and media, and back up before upgrading.
resource: https://docs.frigate.video/frigate/installation
tags: [frigate, installation, docker, gpu, coral]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: frigate-docs
    resource: "https://docs.frigate.video"
    title: "Frigate documentation"
    author: "site:docs.frigate.video"
---

# Frigate — Installation

```yaml
services:
  frigate:
    image: ghcr.io/blakeblackshear/frigate:stable        # or :stable-tensorrt, :stable-rocm, …
    restart: unless-stopped
    shm_size: "512mb"                                    # scale with camera count and resolution
    devices:
      - /dev/dri/renderD128                              # Intel/AMD hardware decoding
      # - /dev/apex_0                                    # PCIe Coral
    volumes:
      - ./config:/config
      - ./media:/media/frigate
      - type: tmpfs
        target: /tmp/cache
        tmpfs: { size: 1000000000 }
    ports:
      - "127.0.0.1:8971:8971"                            # authenticated UI
      - "8554:8554"                                      # RTSP restream
    environment:
      FRIGATE_RTSP_PASSWORD: "change-me"
```

For NVIDIA use the `-tensorrt` image with a GPU reservation (see [Docker GPU & AI](../../runtime/docker/gpu-ai.md)).

## Upgrading

0.18 contains breaking config changes. Copy your config file and `frigate.db` before upgrading; Frigate migrates config automatically but some cases need manual edits.

## Related

[Frigate index](index.md) · [Configuration](configuration.md) · [Docker](../../runtime/docker/index.md)
