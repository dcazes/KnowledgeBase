---
type: Playbook
title: Camofox — Snippets & Cheat Sheet
description: Copy-paste commands to launch Camofox, verify ports, and the watch/login workflow.
resource: https://github.com/daijro/camoufox
tags: [camofox, snippets, cheat-sheet, launch, novnc, browser]
timestamp: 2026-07-09T01:06:00Z
---

# Launch

```bash
# via the desktop launcher's command:
sudo make -C /home/daniel/Documents/camofox-browser up

# directly:
cd /home/daniel/Documents/camofox-browser
make build     # image: camofox-browser:135.0.1-x86_64
make up
make down
```

# Verify

```bash
docker ps | grep camofox
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:9377/   # API
# browser: http://localhost:6080/  (noVNC viewer)
```

# Watch / login (noVNC)

Open `http://localhost:6080/` in a browser to see the live Firefox and solve CAPTCHAs/logins.

# Agent drive (conceptual)

```python
import requests
BASE = "http://localhost:9377"
# open session, navigate, interact — confirm exact endpoints against the running server
r = requests.post(f"{BASE}/session", json={"url": "https://example.com"})
print(r.json())
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| API down | not started | `make up` |
| VNC blank | :6080 not published | check container ports |
| Build fails | Docker off | `systemctl --user start docker-desktop` |
| sudo prompt | launcher uses sudo | run with sudo or join docker group |

# Citations

[1] [Installation](installation.md)
[2] [Usage (API + VNC)](usage.md)
