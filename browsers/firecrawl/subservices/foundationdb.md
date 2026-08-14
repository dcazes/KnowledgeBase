---
type: Reference
title: Firecrawl Subservice — FoundationDB
description: The foundationdb container — experimental queue backend (NUQ_BACKEND=fdb) as an alternative to NUQ Postgres.
resource: https://github.com/firecrawl/firecrawl
tags: [firecrawl, foundationdb, subservice, fdb, queue, experimental]
generated: { by: "human:daniel", at: "2026-07-09T00:37:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:37:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: local-compose-foundationdb-services
    resource: "/../../programs/firecrawl/firecrawl/docker-compose.yaml"
    title: "Local compose (foundationdb services)"
---

# Role

FoundationDB is an **experimental alternative** job/state backend. By default Firecrawl uses NUQ-Postgres; setting `NUQ_BACKEND=fdb` switches the queue to FoundationDB. The api reads the shared cluster file from the `fdb-cluster-file` volume.

# Containers involved

* `foundationdb` — `foundationdb/foundationdb:7.3.63`, stores data in `fdb-data` volume, shares `/var/fdb` via `fdb-cluster-file`.
* `foundationdb-init` — one-shot; runs `fdbcli ... configure new single ssd` on first boot (no-op afterwards), then exits (`restart: "no"`).

# Activation

```bash
# in the api service env:
NUQ_BACKEND=fdb
FDB_CLUSTER_FILE=${NUQ_BACKEND:+/var/fdb/fdb.cluster}   # set when NUQ_BACKEND=fdb
```

The api container mounts `fdb-cluster-file:/var/fdb:ro` so it can reach the cluster.

# When to use

Leave it **off** unless you specifically want FDB's distributed store. It's marked experimental in the compose comments ("Enable by setting NUQ_BACKEND=fdb; replaces nuq-postgres once stable"). For a single-machine deploy, NUQ-Postgres is the simpler, supported default.

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| API can't reach FDB | cluster file missing | ensure `fdb-cluster-file` volume shared; re-run init |
| DB not configured | init didn't run | `docker compose up foundationdb-init` |
