---
domain: ai-workflows
subdomain: document-ai-ocr
concept: state-space-vision-model
title: Sarvam Vision: Training a 3B State-Space Document AI Model from Scratch
sources:
  - title: "From Scratch to SOTA: Training a 3B State-Space Vision Model — Krishna Prasad Srinivasan, Sarvam"
    url: "https://www.youtube.com/watch?v=T72nqdC92PM"
    author: "Krishna Prasad Srinivasan"
    date: "2026-09-23"
---

# Sarvam Vision: Training a 3B State-Space Document AI Model from Scratch

Krishna Prasad Srinivasan, general manager at Sarvam, describes Sarvam Vision, a 3-billion-parameter vision-language model for document AI that runs on a single GPU yet outperforms models 100x larger. The model is unusual in two ways: its language backbone is not a standard transformer but a state-space model (SSM), and its data, compute, and training were done entirely in India, covering English and the 22 official Indian languages (Srinivasan, Sarvam talk).

The motivation is that India is largely absent from the machine-readable world: less than 1% of the Common Crawl corpus is Indic languages, which the speaker attributes not to a lack of data or knowledge but to that data never having been digitized (Srinivasan, Sarvam talk). Indian document processing is hard because the goal is to extract knowledge rather than plain text, Indian scripts have complex Unicode character combinations where what the reader sees differs from what the machine sees, and most Indian languages are resource-poor (Srinivasan, Sarvam talk).

Architecturally, Sarvam bet early on block-by-block OCR plus a document complexity assessment system, with two complexity modules (layout and reading) wrapped around a state-space VLM doing the per-block OCR. The SSM choice is justified by cost: transformers force L×L token interactions with quadratic compute and growing memory, while SSMs keep a single state updated step by step, giving linear compute and constant memory — important when a page can contain 5,000–10,000 visual tokens. The speaker accepts some recall loss in exchange for avoiding transformer costs (Srinivasan, Sarvam talk).

Training follows a four-stage phased program. Stage one is text-only pretraining on 13 trillion tokens of English, Indian languages, math formulas, and code, producing the 3B-parameter language base so the model can resolve blurred or ambiguous text from images much as a human reads a half-erased word. Stage two is continued pretraining on 300 million image-text pairs to teach general visual capability; stage three begins supervised training, though the transcript cuts off before that stage completes (Srinivasan, Sarvam talk).

- Sarvam Vision is a 3B-parameter, single-GPU-runnable document AI model that claims SOTA results, beating models 100x larger, with all data, compute, and training done in India (Srinivasan, Sarvam talk).
- It uses a state-space model instead of a transformer: linear compute and constant memory versus the quadratic L×L attention cost, which matters for pages with 5,000–10,000 visual tokens (Srinivasan, Sarvam talk).
- The pipeline is block-by-block OCR wrapped in two document-complexity modules (layout and reading) — an early bet that later 2026 models converged on (Srinivasan, Sarvam talk).
- Training is a four-stage phased program: 13T text tokens first for a strong language base, then 300M image-text pairs for visual grounding, then supervised training (Srinivasan, Sarvam talk).
- Motivation: under 1% of Common Crawl is Indic, and the gap is caused by undigitized data rather than missing knowledge or data (Srinivasan, Sarvam talk).