---
type: CheatSheet
title: Hindsight Snippets
description: Hindsight cheat sheet — CLI, client SDK calls, API probes, skill wiring, learning-loop pattern (v0.8.4).
resource: https://hindsight.vectorize.io
tags: [hindsight, snippets, cheat-sheet]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: hindsight-docs
    resource: "https://hindsight.vectorize.io"
    title: "Hindsight docs"
    author: "site:hindsight.vectorize.io"
  - id: hindsight-github
    resource: "https://github.com/vectorize-io/hindsight"
    title: "Hindsight GitHub"
    author: "site:github.com"
---

# Hindsight — Snippets

## CLI

```bash
cd programs/hindsight/hindsight-cli
cargo run -- --help          # or cargo build --release -> target/release/hindsight
hindsight --version          # 0.8.4
hindsight --help             # memory pass / recall commands per build
```

## Client (JS)

```js
import { HindsightClient } from "@vectorize-io/hindsight-client";

const h = new HindsightClient({ baseUrl: "http://localhost:PORT" });

// record an experience
await h.remember({ session: "s1", events: [{ role: "user", content: "…" }] });

// run/recall learned memory
const mem = await h.recall({ query: "preferences for X" });
```

## API probe

```bash
curl -s http://localhost:PORT/health      # per service
```

## Skills wiring

```bash
# copy a skill from the checkout into your agent's skill dir
cp -r programs/hindsight/skills/<skill> ~/.config/opencode/skills/
```

## Learning loop (pattern)

```text
1. task executes → capture events
2. hindsight.remember(events)
3. next task start → hindsight.recall("what did we learn…")
4. agent acts on recalled knowledge
```
