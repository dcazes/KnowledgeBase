---
type: Reference
title: Frigate — Cameras
description: The Reolink camera setup — go2rtc HTTP-FLV ingest, RTSP restream, detect vs record input roles, detection settings.
resource: https://docs.frigate.video/configuration/cameras/
tags: [frigate, camera, reolink, go2rtc, detect, record, rtsp]
generated: { by: "human:daniel", at: "2026-07-09T04:18:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:18:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: camera-config
    resource: "https://docs.frigate.video/configuration/cameras/"
    title: "Camera config"
    author: "site:docs.frigate.video"
  - id: go2rtc
    resource: "https://docs.frigate.video/configuration/go2rtc/"
    title: "go2rtc"
    author: "site:docs.frigate.video"
  - id: configuration
    resource: "configuration.md"
    title: "Configuration"
---

# Reolink camera (`reolink_camera`)

The camera at `192.168.68.61` is pulled via **go2rtc** using Reolink's HTTP-FLV stream (more stable than raw RTSP), then Frigate consumes it as a local RTSP restream.

```yaml
cameras:
  reolink_camera:
    ffmpeg:
      inputs:
        - path: rtsp://127.0.0.1:8554/reolink_sub   # sub-stream
          input_args: preset-rtsp-restream
          roles: [detect]
        - path: rtsp://127.0.0.1:8554/reolink_main  # main stream
          input_args: preset-rtsp-restream
          roles: [record]
    detect:
      enabled: true
      width: 640
      height: 480
      fps: 5
    record:
      enabled: true
```

# Roles

* **detect** — uses the lower-res sub-stream (640×480 @ 5fps) for efficient object detection.
* **record** — uses the higher-res main stream for storage/playback.

# Why go2rtc first

Reolink cameras are notorious for dropping raw RTSP. go2rtc's HTTP-FLV pull + RTSP republish stabilizes the feed before Frigate touches it.

# Tips

* Match `detect.width/height` to the sub-stream's actual resolution.
* Enable `record` per camera (events or continuous, per your policy).
* Set motion/mask zones in the UI to reduce false positives.

# ⚠️ Secrets

The go2rtc URLs embed the camera password. Keep it `<REDACTED>` outside the real config.
