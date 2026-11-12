---
type: Concept
title: Embeddings
description: Text and multimodal embeddings — what they are, dense versus sparse and late-interaction vectors, choosing and serving embedding models locally or via APIs, dimensions and quantization, rerankers, and why the embedding choice is hard to change later.
resource: https://huggingface.co/spaces/mteb/leaderboard
tags: [concept, embeddings, vectors, rerankers, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: mteb
    resource: "https://huggingface.co/spaces/mteb/leaderboard"
    title: "MTEB leaderboard"
    author: "Hugging Face"
---

# Embeddings

An **embedding** maps text (or images, audio, code) to a vector so that similar meanings land close together. Embeddings power semantic search in [RAG](rag.md), [agent memory](agent-memory.md), deduplication, clustering and classification.

## Kinds

| Kind | Notes |
|---|---|
| Dense | One vector per text (e.g. 384–4096 dims); the default |
| Sparse | Weighted vocabulary terms (BM25, SPLADE); great for exact terms — combine with dense for hybrid search |
| Late interaction | One vector per token (ColBERT, ColPali for page images); highest accuracy, more storage |

[Qdrant](../databases/qdrant/overview.md) supports all three; [pgvector](../databases/pgvector/overview.md) supports dense, binary and sparse.

## Choosing a model

* Check the MTEB leaderboard for your language and task, then test on your own data.
* Popular open models: `nomic-embed-text`, `bge-m3` (multilingual, dense+sparse), Qwen3 embedding models, `mxbai-embed-large`; hosted: OpenAI, Cohere, Voyage, Gemini.
* Serve locally with [Ollama](../runtime/ollama/snippets.md), [vLLM](../runtime/vllm/overview.md), [llama.cpp](../runtime/llamacpp/ai-integration.md), Hugging Face TEI or FastEmbed.

## Practical rules

* **Pick once.** Vectors from different models are incompatible; switching means re-embedding everything ([LightRAG](../memory/lightrag/configuration.md) and [AnythingLLM](../apps/anythingllm/rag-embeddings.md) warn about this).
* **Match dimensions** in the vector store config.
* **Quantize** (half precision, int8, binary) to save memory with small recall loss.
* **Rerank** the top results with a cross-encoder for a large quality gain at low cost.

## Related

[Vector databases](vector-databases.md) · [RAG](rag.md) · [Local inference](local-inference.md) · [Concepts index](index.md)
