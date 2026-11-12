---
type: Playbook
title: pgvector Installation
description: Install pgvector from distribution packages or the pgvector Docker image, enable the extension in a database, or use a managed Postgres that ships it.
resource: https://github.com/pgvector/pgvector
tags: [pgvector, installation, docker, postgres]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pgvector-github
    resource: "https://github.com/pgvector/pgvector"
    title: "pgvector/pgvector on GitHub"
    author: "site:github.com"
---

# pgvector — Installation

```bash
sudo apt install postgresql-17-pgvector             # Debian/Ubuntu (match your Postgres major)
brew install pgvector                               # macOS
docker run -d --name pg -p 127.0.0.1:5432:5432 -e POSTGRES_PASSWORD=change-me pgvector/pgvector:pg17
```

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

Managed services (RDS, Aurora, Supabase, Neon, Azure Database for PostgreSQL, Cloud SQL) usually only need the `CREATE EXTENSION`.

## Related

[pgvector index](index.md) · [Snippets](snippets.md)
