---
domain: ai-workflows
subdomain: llm-pretraining-synthetic-data
concept: synthetic-data-at-scale
title: Lessons from Generating 12 Trillion Synthetic Tokens
sources:
  - title: "Lessons from Generating 12 Trillion Synthetic Tokens — Bogdan Gaza, DatologyAI"
    url: "https://www.youtube.com/watch?v=FQwTqUmcbRg"
    author: "Bogdan Gaza (AI Engineer)"
    date: "2026-10-02"
---

# Lessons from Generating 12 Trillion Synthetic Tokens

Bogdan Gaza, co-founder and CTO of DatologyAI (rendered as "Duality" in the transcript), describes the engineering lessons from scaling synthetic data for LLM pre-training at the trillion-token level. He frames the motivation around a "data wall": due to scaling laws, exponentially more compute and data are needed to get only linear model improvements, the internet holds a limited amount of usable data, and high-quality synthetic data is needed to supplement it (AI Engineer, 2026).

DatologyAI is presented as a data curation service—an "oil refinery" for pre-training datasets—that identifies the highest-quality data points in a client's corpus and runs them through its synthetic data recipe, "Beyond Web." The core technique is paraphrasing/rewording existing high-quality documents rather than asking a model to generate data points from scratch, because the latter simply learns the modes of the distribution the model was originally trained on. Prompts are added as prefixes to source documents, and many GPUs and different models are used to generate the synthetic data (AI Engineer, 2026).

Reported results (published in late summer 2025, and described as somewhat outdated by the time of the talk) show models trained at 1B, 3B and 8B parameters on the Beyond Web recipe. A 3B model matched the accuracy of an 8B model trained on Nemo Trans Sent, and Beyond Web reached the performance of Nemo Trans Sent and Cosmopedia using 2.7x and 5.3x fewer tokens respectively—meaning the same performance with less data and less compute (AI Engineer, 2026).

The most recent large-scale run completed roughly 12 trillion synthetic tokens spanning web, math and code. On infrastructure, Gaza notes that while there are expectations about how long generation will take, in practice throughput is much less stable and it is very difficult to reach the ideal GPU utilization. The team began this work for research purposes on a Slurm cluster before integrating synthetic data into their product (AI Engineer, 2026).

- Scaling laws create a "data wall": exponentially more compute and data yield only linear capability gains, and the internet alone cannot supply enough data for frontier pre-training.
- The Beyond Web recipe paraphrases/reworks high-quality documents from a client's dataset instead of prompting a model to invent data from scratch, which would only reproduce the source distribution's modes.
- Reported gains: a 3B model trained with Beyond Web matched an 8B model on Nemo Trans Sent, and compared against Cosmopedia and Nemo Trans Sent it reached comparable accuracy with 2.7x and 5.3x fewer tokens.
- A ~12 trillion token synthetic run was completed across web, math and code domains.
- Engineering reality: achieved GPU throughput during synthetic generation is far less stable than expected, and the work started on a research Slurm cluster before product integration.