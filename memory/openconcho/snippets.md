---
type: Reference
title: OpenConcho Snippets
description: OpenConcho command cheat sheet — dev servers, production builds, Docker make targets and Helm install.
resource: https://github.com/offendingcommit/openconcho
tags: [openconcho, snippets, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openconcho-github
    resource: "https://github.com/offendingcommit/openconcho"
    title: "offendingcommit/openconcho on GitHub"
    author: "site:github.com"
---

# OpenConcho — Snippets

```bash
pnpm install && pnpm dev                                  # web dev server :5173
pnpm --filter @openconcho/desktop dev                     # desktop dev
pnpm build                                                # web → packages/web/dist/
pnpm --filter @openconcho/desktop build                   # desktop bundles
make prod | make up | make down | make clean              # Docker web app on :8080
helm install openconcho oci://ghcr.io/offendingcommit/charts/openconcho --set honcho.defaultUrl=...
```

## Related

[OpenConcho index](index.md) · [Installation](installation.md)
