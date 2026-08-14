---
type: Playbook
title: OpenWebUI — Installation
description: Deploy OpenWebUI via Docker (ports, data volume, first-run access) — documented as available-to-deploy; not currently running on this machine.
resource: https://docs.openwebui.com/getting-started/
tags: [openwebui, install, docker, deployment, self-hosted]
timestamp: 2026-07-09T02:01:00Z
---

# This machine (deployment notes)

If deployed, the container exposes `:3001` (mapped from the image's `8080`):
* Image: `ghcr.io/open-webui/open-webui:ollama`
* Published: host **:3001** → container **:8080**
* Data volume: `open-webui` (at `/app/backend/data` inside the container)
* Access: **http://localhost:3001**

# Deploy (if rebuilding from scratch)

```bash
docker run -d -p 3001:8080 \
  -v open-webui:/app/backend/data \
  --name open-webui --restart always \
  ghcr.io/open-webui/open-webui:ollama
```

> The `:ollama` tag bundles an Ollama runtime. On this machine Ollama is **not** used (no Ollama on host) — inference goes through the `:4000` proxy instead. The `:ollama` tag is harmless; you simply don't point OpenWebUI at an Ollama server.

# First run

Open `http://localhost:3001` and create the admin account. Then add a model connection (see [Configuration](configuration.md)).

# Host-network variant

If the container can't reach other services, you can run with `--network=host`; the port then becomes **:8080** (access `http://localhost:8088`).

# Offline mode

To stop internet model fetches:
```bash
-e HF_HUB_OFFLINE=1
```

# Verify

```bash
docker ps | grep open-webui
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:3001
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Can't reach :3001 | container down | `docker start open-webui` |
| "Server connection error" | can't reach model backend | set OpenAI-compatible URL to the :4000 proxy; or use `--network=host` |
| Models missing | no connection configured | see Configuration |
| Data lost on recreate | volume missing | ensure `-v open-webui:/app/backend/data` |

# Citations

[1] [Getting started (docs)](https://docs.openwebui.com/getting-started/)
[2] [Docker quick start (README)](https://github.com/open-webui/open-webui#quick-start-with-docker-)
[3] [Troubleshooting](https://docs.openwebui.com/troubleshooting/)
