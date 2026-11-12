# AI Knowledge Base

An interlinked, research-backed knowledge base on the **self-hostable AI stack** — local models and gateways, agent memory and GraphRAG, coding and personal agents, MCP and agent skills, web and document ingestion, and evaluation, observability and security.

It is an [Obsidian](https://obsidian.md) vault: every note is plain Markdown with relative links, so it reads well on GitHub and turns into an explorable **knowledge graph** in Obsidian's graph view.

## What's inside

| | |
|---|---|
| **59 tools** in 10 categories | runtime, memory, databases, agents, browsers, ingestion, apps, editors, observability, tools |
| **25 concept hubs** | RAG, GraphRAG, agent memory, MCP, A2A, agent skills, context engineering, evals, agent security, … |
| **Comparison docs** | one `alternatives.md` per category with decision guides |
| **Landscape overview** | [AI landscape (late 2026)](landscape.md) |

Each tool has a standard set of notes — `index`, `overview`, `installation`, `snippets`, `ai-integration` (plus configuration and topic notes where useful). Facts are checked against upstream repositories, release notes, package registries and papers; every note lists its sources in YAML frontmatter ([Open Knowledge Format](AGENTS.md) conventions) with a `verified` date and a `stale_after` date.

## Explore

* **On GitHub:** start at [index.md](index.md) or [landscape.md](landscape.md).
* **In Obsidian:** clone the repo, *Open folder as vault*, and open **Graph view**. Nodes are coloured by category; concept hubs sit at the centre of their clusters.

```bash
git clone https://github.com/dcazes/KnowledgeBase.git
```

## How the graph is shaped

* Tool notes link to their tool `index.md`.
* Each tool index links to the **concepts** it implements and to **peer tools**.
* Concept hubs link to every implementing tool and to related concepts.
* Category comparison docs connect peers; the root index and landscape connect categories.

## Quality checks

`scripts/check_vault.py` validates every internal link, required frontmatter, unique source ids, and flags machine-specific content (home paths, private IPs). It runs on every push via GitHub Actions.

```bash
python3 scripts/check_vault.py
```

## Contributing / updating

Notes go stale quickly in this field. Each note has a `stale_after` date (180 days after verification); re-verify against the sources listed in its frontmatter and bump `verified`. See [AGENTS.md](AGENTS.md) for conventions.

## License

Content is released under [CC BY 4.0](LICENSE). Product names and trademarks belong to their owners.
