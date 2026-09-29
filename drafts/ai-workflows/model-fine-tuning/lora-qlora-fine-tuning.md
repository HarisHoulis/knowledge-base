---
domain: ai-workflows
subdomain: model-fine-tuning
concept: lora-qlora-fine-tuning
title: How to Customize a Model to Learn New Tricks
sources:
  - title: "How to Customize a Model to Learn New Tricks"
    url: "https://blog.bytebytego.com/p/how-to-customize-a-model-to-learn"
    author: "ByteByteGo"
    date: "2026-09-23"
---

# How to Customize a Model to Learn New Tricks

Prompting and retrieval-augmented generation (RAG) both work by supplying information at request time and do not change a model's learned parameters; prompting can't supply missing information, which is what RAG addresses by pulling relevant external material into the model's input. When recurring weaknesses remain—struggles with specialized document categories or summaries that highlight the wrong details—fine-tuning becomes a different option, training the model so desired behavior becomes part of its default behavior, rather than something re-supplied in every request (ByteByteGo).

Supervised fine-tuning (SFT) continues training from an existing model using a focused dataset of input/response pairs; the model predicts the desired response tokens, loss measures how well predictions match targets, and backpropagation plus an optimizer adjust trainable parameters. RLHF adds refinement by having humans rank multiple model responses, training a separate reward model that predicts scores human raters would assign. SFT and RLHF describe how examples teach the model; LoRA and QLoRA describe how that training is carried out efficiently, and the same instruction-response dataset can be used with either (ByteByteGo).

LoRA (Low-Rank Adaptation) is parameter-efficient fine-tuning: the original model weights stay frozen and small trainable adapters—two compact matrices—are attached to selected calculations, producing adjustments added to the original results. Because changes often share patterns, the adapter doesn't need to relearn grammar or domain knowledge already in the base model. A rank setting (e.g. 8, 16, 32, 64) controls adapter capacity, and higher rank is not automatically better. QLoRA combines LoRA with quantization, commonly storing frozen base weights in 4-bit while keeping adapters at higher precision (16- or 32-bit), letting a fixed memory budget customize a larger model. Adapters adapt to the quantized combination and can help recover task performance affected by compression, though they cannot be assumed to fix every quantization error (ByteByteGo).

A practical process starts by choosing a base model that already performs reasonably well in the required language and task, then establishing a baseline with a carefully developed prompt to expose remaining problems. Next, prepare examples demonstrating desired behavior—with correctness mattering because training rewards agreement with supplied answers—and split them into training, validation, and test sets that respectively drive parameter updates, guide setting comparison and checkpoint choice, and provide a final assessment (ByteByteGo).

- Prompting and RAG guide behavior through request-time information without changing model parameters; fine-tuning makes desired behavior part of the model's default behavior.
- SFT trains on input/response pairs using loss, backpropagation, and an optimizer; RLHF adds a reward model trained on human rankings of model responses.
- LoRA freezes base weights and trains small adapter matrices attached to selected calculations, with a rank setting trading adapter capacity against size and training overhead.
- QLoRA quantizes frozen base weights (commonly 4-bit) while keeping adapters at higher precision, enabling customization of larger models under a fixed memory budget.
- A sound process requires a capable base model, a prompt-established baseline, correct and consistent training examples, and separate training/validation/test splits.