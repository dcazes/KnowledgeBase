---
type: Reference
title: Parser Service — NOTES
description: Integration notes and official sources for the Docling/MinerU parser-service prototype.
resource: https://github.com/opendatalab/mineru
tags: [parser, docling, mineru, agent-stack, notes]
timestamp: 2026-08-12T00:00:00Z
---

# Parser Service — NOTES

## Integration (verified 2026)
* **Docling** — Python API + CLI; outputs **Markdown or DoclingDocument JSON**; IBM ships a Docling agent skill (parse/convert/chunk/analyze). ([docling-project.github.io](https://docling-project.github.io/docling/examples/agent_skill/docling-document-intelligence/SKILL/))
* **MinerU** — CLI `mineru -p <in> -o <out> -b pipeline`, API, WebUI; PDF/image/DOCX/PPTX/XLSX → Markdown. ([github.com/opendatalab/mineru](https://github.com/opendatalab/mineru))

## How it feeds the stack
```
docs/PDF ──► parser-service (Docling | MinerU) ──► ./parsed (markdown/json)
                │
                ▼
        ingest step: embed via Ollama (nomic-embed-text)
                │
                ├─► Weaviate (search backend)
                └─► Graphiti episodes (memory)
```
Hermes can call the parser over HTTP (`:5007`/`:5008`) or via the Docling agent skill directly.

## Division of labor
* **Docling** = primary (clean structured docs; JSON for graph episodes).
* **MinerU** = scan/OCR-heavy where Docling loses fidelity.

## Not deployed
CPU-capable; GPU optional (uncomment deploy block for MinerU OCR). Joins `agent-net` (external) so it reaches Ollama/Weaviate.

# Citations

[1] [Docling](https://github.com/docling-project/docling)
[2] [MinerU](https://github.com/opendatalab/mineru)
[3] [Integration map](../notes.md)
