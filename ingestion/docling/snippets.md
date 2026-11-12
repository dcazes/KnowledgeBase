---
type: Reference
title: Docling Snippets
description: Docling Python snippets — convert a PDF or URL, export Markdown and JSON, iterate tables, and chunk with the hybrid chunker for embedding.
resource: https://docling-project.github.io/docling/
tags: [docling, snippets, python, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: docling-docs
    resource: "https://docling-project.github.io/docling/"
    title: "Docling documentation"
    author: "site:docling-project.github.io"
---

# Docling — Snippets

```python
from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker

conv = DocumentConverter()
result = conv.convert("https://arxiv.org/pdf/2408.09869")
doc = result.document

print(doc.export_to_markdown()[:1000])
doc.save_as_json("report.json")                      # lossless DoclingDocument

for table in doc.tables:
    print(table.export_to_dataframe(doc).head())

for chunk in HybridChunker(max_tokens=512).chunk(doc):
    text = chunk.text                                # embed this; chunk.meta holds headings and page refs
```

## Related

[Docling index](index.md) · [AI Integration](ai-integration.md)
