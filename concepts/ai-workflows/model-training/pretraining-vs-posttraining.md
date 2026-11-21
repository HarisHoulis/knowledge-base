---
domain: ai-workflows
subdomain: model-training
concept: pretraining-vs-posttraining
title: Baking a Model: Pre-training and Post-training Explained
sources:
  - title: "Baking a Model"
    url: "https://newsletter.kentbeck.com/p/baking-a-model"
    author: "Kent Beck"
    date: "2026-08-14"
---

# Baking a Model: Pre-training and Post-training Explained

Kent Beck uses a baking analogy to explain how AI models are constructed, distinguishing the model proper (a "bag of numbers" produced by training) from the conventional user interface that handles formatting, sequencing, and authentication. Unlike programming, where you write statements that produce a program, models result from training—iteratively tweaking approximately correct numbers rather than guessing them correctly in one go.

Pre-training is a big batch: the team sets up initial conditions (data and a blank model), runs the data through the model a huge number of times, takes crash-recovery snapshots, and watches for signs the run has gone off the weeds. It is a big bet costing hundreds of millions of dollars and months of delay. Beck likens it to cold proofing bread—mix ingredients, put it somewhere you can't interfere, and let it play out; the result isn't usable but is the precursor to what follows.

Post-training consists of many small batches: researchers (whom Beck would bluntly call "model engineers") identify particular problems the raw model handles poorly and explore tweaks, yielding surviving chunks of code and data that supplement the model. Apply enough supplements and, paired with a UI, user, and compute, you get a model that can answer prompts. Beck notes the analogy breaks down because post-training is collaborative, iterative, and reversible.

He flags that "training" is really the composition of pre-, mid-, and post-training, and plans a followup on the divergent incentives, tools, rhythms, and cultures of the teams involved.

- A model is split into a conventionally programmed user interface and the model proper, which is a "bag of numbers" produced by training rather than written statements.
- Pre-training is a large, expensive, months-long batch process analogous to cold proofing: set initial conditions, let it run, and monitor for divergence.
- Post-training is many small, iterative, reversible experiments that supplement the pre-trained model to fix specific weaknesses.
- "Training" is really the composition of pre-, mid-, and post-training; Beck invites corrections on his understanding.