---
type: Reference
title: Frigate — Configuration
description: Anatomy of config.yml — go2rtc streams, detectors (ONNX), ffmpeg hwaccel, cameras, recording; secrets redacted.
resource: https://docs.frigate.video/configuration/
tags: [frigate, config, go2rtc, detector, onnx, ffmpeg, redacted-secrets]
generated: { by: "human:daniel", at: "2026-07-09T04:17:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:17:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: configuration-docs
    resource: "https://docs.frigate.video/configuration/"
    title: "Configuration docs"
    author: "site:docs.frigate.video"
  - id: go2rtc
    resource: "https://docs.frigate.video/configuration/go2rtc/"
    title: "go2rtc"
    author: "site:docs.frigate.video"
  - id: detectors
    resource: "https://docs.frigate.video/configuration/detectors/"
    title: "Detectors"
    author: "site:docs.frigate.video"
  - id: local-config
    resource: "/../../programs/frigate/config.yml"
    title: "Local config"
---

# config.yml anatomy (this machine)

```yaml
go2rtc:
  streams:
    reolink_main:
      - ffmpeg:http://192.168.68.61/flv?port=1935&app=bcs&stream=channel0_main.bcs&user=admin&password=<REDACTED>
    reolink_sub:
      - ffmpeg:http://192.168.68.61/flv?port=1935&app=bcs&stream=channel0_ext.bcs&user=admin&password=<REDACTED>

detectors:
  onnx:
    type: onnx
    model:
      path: internal

ffmpeg:
  hwaccel_args: preset-nvidia

cameras:
  reolink_camera:
    ffmpeg:
      inputs:
        - path: rtsp://127.0.0.1:8554/reolink_sub
          input_args: preset-rtsp-restream
          roles: [detect]
        - path: rtsp://127.0.0.1:8554/reolink_main
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

# Sections

* **go2rtc** — pulls the Reolink feed over HTTP-FLV (stable) and republishes as RTSP at `127.0.0.1:8554`. Camera creds are here **in plaintext** → keep `<REDACTED>` in any copy.
* **detectors** — `onnx` with `model.path: internal` (built-in model). (The `config (copy).yml` instead uses the `tensorrt` detector for the `:stable-tensorrt` image — but note the TensorRT detector was **removed in 0.16.0**; NVIDIA GPUs now use the ONNX detector with CUDA Graphs since 0.17. The active image is `:stable`.)
* **ffmpeg** — `preset-nvidia` for GPU decode.
* **cameras** — per-camera inputs (detect vs record roles), detect resolution/fps, recording toggle.

# Security

* ⚠️ The real `config.yml` contains the **camera password** and the compose sets `FRIGATE_RTSP_PASSWORD`. Never record literal values in this KB.
* Consider moving secrets to an env file / Docker secret and referencing them.
