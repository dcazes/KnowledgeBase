---
type: Playbook
title: Docker — Installation & Setup
description: Install Docker on this Linux machine, start it as a user service, fix permissions, and verify the install.
resource: https://docs.docker.com/desktop/setup/install/linux/
tags: [docker, install, setup, linux]
timestamp: 2026-07-08T22:35:00Z
---

# Your setup

This machine runs **Docker Desktop for Linux** (installed from `programs/docker/docker-desktop-amd64.deb`). Docker Desktop is launched as a **user-level systemd service**, not the system-wide engine:

```bash
# From programs/docker/run
systemctl --user start docker-desktop
```

Verify it worked:

```bash
docker version          # client + server details (expect Docker 29.7.2)
docker info             # daemon config, drivers, resource usage
docker run hello-world  # pulls a tiny image and prints a confirmation
```

# Installing Docker Desktop from the .deb (reference)

If you ever need to reinstall:

```bash
# Install the package (requires apt dependencies first)
sudo apt-get update
sudo apt-get install -y ./programs/docker/docker-desktop-amd64.deb

# Start as a user service (no sudo needed at runtime)
systemctl --user start docker-desktop
systemctl --user enable docker-desktop   # auto-start on login
```

> Note: the folder also contains `docker-desktop-amd64.deb.1` — a duplicate of the same file. You only need one.

# Post-install: permissions & socket

With Docker Desktop, the CLI talks to the daemon over the user socket — you normally do **not** need the `sudo usermod -aG docker` step that the classic engine requires. If you ever run the standalone engine instead:

```bash
sudo usermod -aG docker $USER   # add user to docker group
newgrp docker                   # re-load group in current shell (or re-login)
docker ps                       # should now work without sudo
```

# Useful install checks

```bash
docker compose version   # Compose v5.4.0 (Mont Blanc)
docker system df         # disk used by images/containers/volumes
systemctl --user status docker-desktop
```

# Troubleshooting

| Symptom | Fix |
|---------|-----|
| `Cannot connect to the Docker daemon` | `systemctl --user start docker-desktop` |
| Daemon doesn't start after reboot | `systemctl --user enable docker-desktop` |
| Permission denied on socket | Use Docker Desktop (user socket) or join the `docker` group (engine) |
| Port already in use | Change the host port mapping, e.g. `"8082:8080"` (see [Compose](compose.md)) |

# Citations

[1] [Install Docker Desktop on Linux](https://docs.docker.com/desktop/setup/install/linux/)
[2] [Docker Desktop post-install](https://docs.docker.com/desktop/setup/install/linux/)
[3] [Local install notes - programs/docker/](/../../programs/docker/)
