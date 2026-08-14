---
type: Playbook
title: AnythingLLM — Installation
description: Deploy AnythingLLM via Docker (port 3001, storage volume, UID 1000 gotcha) or install the Desktop AppImage.
resource: https://docs.anythingllm.com/installation-docker
tags: [anythingllm, install, docker, appimage, deployment, uid-1000]
generated: { by: "human:daniel", at: "2026-07-09T02:31:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T02:31:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: docker-install-docs
    resource: "https://docs.anythingllm.com/installation-docker"
    title: "Docker install docs"
    author: "site:docs.anythingllm.com"
  - id: anythingllm-github-releases-appimage
    resource: "https://github.com/Mintplex-Labs/anything-llm/releases"
    title: "AnythingLLM GitHub releases (AppImage)"
    author: "site:github.com"
---

# Option A — Docker (multi-user / server)

```bash
# 1) storage dir MUST be owned by UID 1000 (container writes as 1000)
mkdir -p ~/anythingllm-storage
sudo chown -R 1000:1000 ~/anythingllm-storage

# 2) run
docker run -d --name anythingllm \
  -p 3001:3001 \
  -v /home/daniel/anythingllm-storage:/app/server/storage \
  -e STORAGE_DIR=/app/server/storage \
  --restart unless-stopped \
  mintplexlabs/anythingllm:latest

# 3) access
# http://localhost:3001  (first run: create admin, pick LLM + embeddings)
```

## The UID 1000 gotcha

AnythingLLM's container runs as **UID 1000**. If the host storage dir isn't owned by 1000, SQLite fails:
```
EACCES: permission denied, open '/app/server/storage/database.sqlite'
```
**Fix:** `sudo chown -R 1000:1000 ~/anythingllm-storage` (do it before first run).

# Option B — Desktop AppImage (single user)

The upstream desktop AppImage is the single-user install path. On this machine it was previously noted via a local `installer.sh`; that file is **not currently present** (no `programs/anythingllm/` directory), so use the upstream release directly:

```bash
# download the latest AppImage from the AnythingLLM GitHub releases page
chmod +x AnythingLLMDesktop*.AppImage
./AnythingLLMDesktop*.AppImage
```

# Verify

```bash
docker ps | grep anythingllm
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:3001
docker logs anythingllm --tail 20
```

# Upgrade

```bash
docker pull mintplexlabs/anythingllm:latest
docker stop anythingllm && docker rm anythingllm
# re-run the docker run command above (storage persists via volume)
```

# Backup

```bash
docker stop anythingllm
tar -czvf anythingllm-backup-$(date +%Y%m%d).tar.gz ~/anythingllm-storage/
docker start anythingllm
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `EACCES database.sqlite` | storage UID ≠ 1000 | `sudo chown -R 1000:1000 ~/anythingllm-storage` |
| Container exits | port 3001 in use | free port or change `-p` |
| AppImage won't start | AppArmor/SUID | run installer (creates profile) |
| Can't reach from LAN | firewall | `sudo ufw allow 3001/tcp` |
