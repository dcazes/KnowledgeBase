---
type: Playbook
title: Frigate — Snippets & Cheat Sheet
description: Deploy, ports, verify, and config notes for Frigate (secrets redacted).
resource: https://docs.frigate.video/
tags: [frigate, snippets, cheat-sheet, compose, ports, gpu]
generated: { by: "human:daniel", at: "2026-07-09T04:21:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:21:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: installation
    resource: "installation.md"
    title: "Installation"
  - id: configuration
    resource: "configuration.md"
    title: "Configuration"
  - id: cameras
    resource: "cameras.md"
    title: "Cameras"
---

# Deploy (from programs/frigate/)

```bash
docker compose -f docker-compose.yml up -d
```

# Ports

```
8971  Authenticated UI & API (TLS via reverse proxy)
5000  Internal unauthenticated UI & API
8554  RTSP re-stream
8555  WebRTC (tcp+udp)
```

# Verify

```bash
docker ps | grep frigate
curl -sk -o /dev/null -w "%{http_code}\n" https://localhost:8971
```

# Config key points (secrets REDACTED)

* go2rtc pulls Reolink HTTP-FLV → republishes RTSP `127.0.0.1:8554`.
* detector: `onnx` (internal model); `ffmpeg.hwaccel_args: preset-nvidia`.
* camera `reolink_camera`: sub-stream=detect, main=record; 640×480 @5fps.

# ⚠️ Secrets

Camera password (in `go2rtc` URLs) and `FRIGATE_RTSP_PASSWORD` are plaintext in config/compose. Keep them `<REDACTED>` outside the real files; rotate if leaked.

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| UI down | container stopped | `docker start frigate` |
| No detect | GPU/detector | verify `onnx` + `preset-nvidia` |
| Cam offline | go2rtc/creds | check go2rtc streams (creds redacted) |
