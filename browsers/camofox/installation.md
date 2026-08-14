---
type: Playbook
title: Camofox — Installation & Launch
description: Build and launch the Camofox browser server via make, the Docker image, ports, and the desktop launcher.
resource: https://github.com/daijro/camoufox
tags: [camofox, install, docker, make, launch, deployment]
timestamp: 2026-07-09T01:01:00Z
---

# Source location

The project lives locally (not under `programs/`):
```
/home/daniel/Documents/camofox-browser     # used by the launcher
/home/daniel/Documents/Camox               # alternate clone (per setup note)
```

# Launch (recommended)

The desktop launcher runs:
```bash
sudo make -C /home/daniel/Documents/camofox-browser up
```

You can run the same directly:
```bash
cd /home/daniel/Documents/camofox-browser
make build     # build the Docker image (camofox-browser:135.0.1-x86_64)
make up        # start the server
make down      # stop the server
```

> The launcher uses `sudo` because the Makefile manages Docker. If your user is in the `docker` group, `sudo` may be unnecessary — but keep the launcher as-is for consistency.

# Image & ports

* **Image:** `camofox-browser:135.0.1-x86_64`
* **Port 9377** — the browser **API** endpoint (agents drive the browser here).
* **Port 6080** — **noVNC** viewer (open in a browser to watch/control the live browser). **Opt-in:** only published when `ENABLE_VNC=1` is set (the local launcher sets it).

# Verify

```bash
docker ps | grep camofox                # container running
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:9377/   # API up
# open http://localhost:6080/ in a browser for the VNC view
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `make: command not found` | make not installed | `sudo apt install build-essential` |
| API :9377 down | container not started | `make up` |
| VNC blank | noVNC not exposed | check :6080 published |
| Build fails | Docker not running | `systemctl --user start docker-desktop` |

# Citations

[1] [Local launcher - programs/Camofox Launcher.desktop](/../../programs/Camofox%20Launcher.desktop)
[2] [Local launcher - programs/Camofox Launcher.desktop](/../../programs/Camofox%20Launcher.desktop)
[3] [Camoufox upstream](https://github.com/daijro/camoufox)
