---
domain: ai-workflows
subdomain: reasoning-models
concept: energy-based-reasoning-models
title: How to Build Models Without Language, with Logical Intelligence
sources:
  - title: "How to Build Models Without Language, with Logical Intelligence"
    url: "https://blog.bytebytego.com/p/how-to-build-models-without-language"
    author: "ByteByteGo"
    date: "2026-10-12"
---

# How to Build Models Without Language, with Logical Intelligence

Large language models struggle with constraint satisfaction problems like Sudoku because they generate tokens left-to-right and their outputs are discrete, making early mistakes expensive to revise and preventing incremental progress toward correctness [1][3]. In a public experiment, frontier LLMs including GPT-5.2, Claude Opus 4.5, Gemini 3 Pro, and DeepSeek V3.2 collectively solved only 2% of Sudoku puzzles at a cost of roughly $11,000 in API calls, while a model called Kona, about a thousand times smaller, solved 96.2% for only $4 in GPU time [1].

Logical Intelligence builds energy-based reasoning models (EBRMs) like Kona that work with latent variables instead of discrete tokens. An EBM learns a function E(x, y) that assigns an energy to a candidate answer y for a problem x, where lower energy means greater consistency with the problem [4]. Training uses a contrastive loss that lowers the energy of correct answers and raises it for wrong ones, producing a continuous landscape where correct answers sit in valleys. Inference starts from random noise and follows the descending energy gradient until the energy stops falling, allowing the model to spend more computation on harder problems [4].

Because the landscape is continuous, candidate answers are represented as vectors of scores rather than discrete tokens, enabling gradient-based search toward correctness. In the Sudoku demo, Kona settled in 313 milliseconds on average, while LLMs took up to 90 seconds per puzzle [1]. Logical Intelligence trained Kona on unfinished Sudoku solutions with half of every grid hidden and no reinforcement learning, yet it still learned the rules and produced complete, correct grids at test time [1]. The article argues that language is the interface to intelligence, not intelligence itself, and that many tasks require extrapolation, spatial reasoning, planning, and logic beyond language [2].

- LLMs fail on constraint satisfaction problems because of left-to-right generation and discrete outputs, which make early mistakes costly and prevent incremental correction [1][3].
- Energy-based reasoning models (EBRMs) learn an energy function E(x, y) that scores candidate answers, with lower energy indicating greater consistency with the problem [4].
- EBRM inference follows a descending energy gradient from random noise until energy stops falling, spending more computation on harder problems [4].
- Kona, a model about a thousand times smaller than frontier LLMs, solved 96.2% of Sudoku puzzles for $4 in GPU time versus 2% and $11,000 for LLMs [1].
- Language is the interface to intelligence, not intelligence itself; many tasks require non-linguistic reasoning such as logic, planning, and extrapolation [2].