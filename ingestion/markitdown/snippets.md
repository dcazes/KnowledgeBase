---
type: Reference
title: MarkItDown Snippets
description: MarkItDown CLI and Python snippets — convert files and stdin, enable plugins, and add LLM image descriptions.
resource: https://github.com/microsoft/markitdown
tags: [markitdown, snippets, cli, python, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: markitdown-github
    resource: "https://github.com/microsoft/markitdown"
    title: "microsoft/markitdown on GitHub"
    author: "site:github.com"
---

# MarkItDown — Snippets

```bash
markitdown report.pdf > report.md
markitdown slides.pptx -o slides.md
cat page.html | markitdown
markitdown --use-plugins file.ext
```

```python
from markitdown import MarkItDown
md = MarkItDown(enable_plugins=False)
print(md.convert("budget.xlsx").text_content)

from openai import OpenAI
md = MarkItDown(llm_client=OpenAI(), llm_model="gpt-5-mini")   # captions for images
print(md.convert("diagram.png").text_content)
```

## Related

[MarkItDown index](index.md) · [AI Integration](ai-integration.md)
