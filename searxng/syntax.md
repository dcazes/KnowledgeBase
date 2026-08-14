---
type: Reference
title: SearXNG — Search Syntax
description: Query operators and shortcuts — engine/category/language prefixes, boolean logic, site:/filetype: filters, and time ranges.
resource: https://docs.searxng.org/user/search-syntax.html
tags: [searxng, syntax, operators, shortcuts, search-syntax]
timestamp: 2026-07-08T23:55:00Z
---

# Overview

SearXNG supports a rich query language. Prefixes start with `!`; most operators work the same as on the upstream engines they forward to. This is the syntax you use in the UI search box *and* in the `q` parameter of the [API](api.md).

# Bang-style shortcuts (`!`)

Prefixing `!` routes the query to a specific target. Order is flexible; common pattern is `!category !language !engine <query>`.

## Engine shortcuts

| Shortcut | Engine | Category |
|----------|--------|----------|
| `!google` | Google | general |
| `!bing` | Bing | general |
| `!ddg` | DuckDuckGo | general |
| `!brave` | Brave | general |
| `!github` | GitHub | code |
| `!gitlab` | GitLab | code |
| `!stackoverflow` | Stack Overflow | code |
| `!wikipedia` | Wikipedia | general |
| `!youtube` | YouTube | videos |
| `!vimeo` | Vimeo | videos |
| `!arxiv` | arXiv | academic |
| `!scholar` | Google Scholar | academic |
| `!reddit` | Reddit | social/news |
| `!hackernews` | Hacker News | news |

```text
!github python async
!wikipedia quantum computing
!arxiv transformer attention
```

## Category shortcuts

Prefix `!` with a category name to limit the whole query to that category:

```text
!code docker containerization
!images mountain landscape
!videos python tutorial
!news AI regulation
!academic machine learning
!maps tokyo restaurants
```

Available categories: `general`, `images`, `videos`, `news`, `code`, `academic`, `maps`, `music`, `files`.

## Language shortcuts

```text
!en machine learning
!es aprendizaje automático
!de maschinelles lernen
!fr apprentissage automatique
!ja 機械学習
```

Common codes: `en`, `es`, `de`, `fr`, `it`, `pt`, `ru`, `ja`, `zh`, `ko`.

## Combining

```text
!code !en !github docker permissions
!academic !en !arxiv transformer optimization
```

# Boolean & filtering operators

| Operator | Example | Effect |
|----------|---------|--------|
| `"phrase"` | `"UID 1000" docker` | Exact phrase match |
| `-term` | `docker -compose` | Exclude results containing the term |
| (implicit AND) | `docker permissions` | All terms required |
| `OR` | `docker OR container` | Either term |
| `( )` | `(docker OR container) permissions` | Grouping / precedence |
| `site:` | `site:docs.docker.com docker` | Restrict to a domain |
| `filetype:` | `filetype:pdf machine learning` | Specific file format |
| `intitle:` | `intitle:"docker tutorial"` | Match page title |

# Time range

Two ways:

* **API parameter** (recommended, reliable): `time_range=day|week|month|year`
  ```bash
  curl "http://127.0.0.1:8088/search?q=docker&time_range=week&format=json"
  ```
* **Some engines** accept syntax like `after:2024-01-01` / `before:2023-12-31`, but support varies — prefer the parameter.

# Practical patterns

```text
# GitHub repos on a topic
!github !en "knowledge graph" python

# Stack Overflow error
!stackoverflow "permission denied" docker volume

# Docs only, exclude tutorials
docker permissions site:docs.docker.com -tutorial

# Real issue trackers (not blog posts)
"permission denied" docker site:github.com/issues

# Today's news
!news AI regulation time_range:day

# Compare tools
anythingllm vs llama-index vs langchain
```

# Engine quirks

| Engine | Quirk | Mitigation |
|--------|-------|-----------|
| Google | Aggressive CAPTCHA under load | Use sparingly; enable caching; disable if hammered |
| Bing | More permissive | Good high-volume fallback |
| DuckDuckGo | Slower but private | Reliable default |
| GitHub | Unauthenticated rate limits | Moderate `!github` use; add token in config if needed |
| arXiv | Excellent API | Reliable for academic |

# Testing your syntax

```bash
# Confirm the intended engine answered
curl -s "http://127.0.0.1:8088/search?q=!github+docker&format=json" \
  | python3 -c "import sys,json; print(set(r['engine'] for r in json.load(sys.stdin)['results']))"
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Engine shortcut ignored | Engine disabled | Enable in `/preferences` or config |
| No results | Too restrictive | Drop some exclusions |
| Wrong language | Auto-detect wrong | Set `!en` explicitly |
| Slow | Too many engines | Narrow `categories` |

# Citations

[1] [Search syntax](https://docs.searxng.org/user/search-syntax.html)
[2] [Configured engines](https://docs.searxng.org/user/configured_engines.html)
