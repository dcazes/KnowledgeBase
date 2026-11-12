---
type: Reference
title: Frigate Cameras
description: Adding cameras to Frigate — separate detect and record streams, go2rtc restreaming and WebRTC live view, hardware decoding presets, zones, masks and object filters.
resource: https://docs.frigate.video/configuration/cameras
tags: [frigate, cameras, go2rtc, zones, rtsp]
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

# Frigate — Cameras

```yaml
go2rtc:
  streams:
    driveway: [rtsp://user:pass@camera-ip:554/main]
    driveway_sub: [rtsp://user:pass@camera-ip:554/sub]
cameras:
  driveway:
    ffmpeg:
      hwaccel_args: preset-vaapi
      inputs:
        - path: rtsp://127.0.0.1:8554/driveway_sub
          roles: [detect]
        - path: rtsp://127.0.0.1:8554/driveway
          roles: [record]
    detect: { width: 1280, height: 720, fps: 5 }
    zones:
      driveway_zone:
        coordinates: 0.1,0.9,0.9,0.9,0.9,0.4,0.1,0.4
        friendly_name: Driveway
    objects:
      filters:
        person: { min_score: 0.6 }
```

* Detect on the low-resolution substream, record the main stream.
* **go2rtc** restreams each camera once, providing low-latency WebRTC/MSE live view.
* Zones scope alerts; motion masks hide timestamps and swaying trees.

FFmpeg 8 (0.18) needs a small go2rtc tweak for hardware-transcoded streams — see the release notes.

## Related

[Frigate index](index.md) · [Configuration](configuration.md)
