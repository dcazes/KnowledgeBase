---
type: HowTo
title: Pydantic Installation
description: Install Pydantic — pip install pydantic (+ pydantic-settings), versions on this machine (2.9.0 / 2.13.4), verify.
resource: https://docs.pydantic.dev
tags: [pydantic, installation, pip]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: pydantic-docs-install
    resource: "https://docs.pydantic.dev"
    title: "Pydantic docs — install"
    author: "site:docs.pydantic.dev"
  - id: pydantic-on-pypi
    resource: "https://pypi.org/project/pydantic/"
    title: "Pydantic on PyPI"
    author: "site:pypi.org"
---

# Pydantic — Installation

## pip

```bash
pip install pydantic                # core (v2 current)
pip install pydantic-settings       # BaseSettings / env config
# or the pinned safe version (post-2026-07 CVEs):
pip install "pydantic>=2.12"
```

## Versions on this machine (verified 2026-08-12)

```bash
python -c "import pydantic; print(pydantic.VERSION)"
# system python : 2.9.0
# programs/pydantic/.venv : 2.13.4
```

Note the system copy (2.9.0) is **older than the 2.12 minimum** for the 2026-07 CVE fixes — use a venv (2.13.4) or upgrade when running agent code. See [PydanticAI → CVEs](../../agents/pydanticAI/index.md).

## Verify

```python
from pydantic import BaseModel

class M(BaseModel):
    x: int

m = M(x="42")          # coerces to int
assert m.x == 42
print(m.model_dump())  # {'x': 42}
```
