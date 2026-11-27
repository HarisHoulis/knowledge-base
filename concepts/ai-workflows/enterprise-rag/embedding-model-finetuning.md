---
domain: ai-workflows
subdomain: enterprise-rag
concept: embedding-model-finetuning
title: Finetuning Your Embedding Model for Better Search: Learning from Agentic Search at Dell
sources:
  - title: "Presentation: Finetuning Your Embedding Model for Better Search: Learning from Agentic Search at Dell"
    url: "https://www.infoq.com/presentations/fine-tune-enterprise-rag-embeddings/"
    author: "Rachel Shalom"
    date: "2026-11-26"
---

# Finetuning Your Embedding Model for Better Search: Learning from Agentic Search at Dell

Rachel Shalom describes how Dell addressed retrieval failures in its enterprise RAG system when queries involved internal terminology. Rather than relying on off-the-shelf embeddings, the team fine-tuned open-source embedding models to better match their domain vocabulary.

The approach centers on careful data preparation using hard negatives, so the model learns to distinguish closely related but incorrect passages. Training uses a distributed InfoNCE loss across H100 GPUs, with automated hyperparameter tuning to manage the search space efficiently.

Production quality is assessed with LLM-as-a-judge evaluation, giving the team a scalable way to measure retrieval improvements after fine-tuning. The talk frames this as a practical playbook for improving agentic search in enterprise settings.

- Fine-tuning open-source embedding models fixes retrieval failures on internal/enterprise terminology
- Hard-negative data preparation is key to training discriminative embeddings
- Training uses distributed InfoNCE loss on H100 GPUs with automated hyperparameter tuning
- LLM-as-a-judge provides scalable production evaluation of retrieval quality