---
domain: ai-workflows
subdomain: autonomous-ai-research
concept: ai-research-agent
title: ARIA: An AI Research Agent That Runs Your Experiments
sources:
  - title: "An AI Research Agent That Runs Your Experiments — Tim Sweeney, Weights & Biases"
    url: "https://www.youtube.com/watch?v=hd7TOvmyAxU"
    author: "AI Engineer"
    date: "2026-09-26T14:30:38+00:00"
---

# ARIA: An AI Research Agent That Runs Your Experiments

Tim Sweeney, a lead engineer at Weights & Biases and CoreWeave, introduces ARIA, an agent for AI research and iteration. He describes Weights & Biases as an AI development platform that joined CoreWeave about a year ago and offers products for models, training, inference, and the Weave stack. ARIA is presented as a chat-based agent inside the Weights & Biases workspace, accessed via a button in the project UI.

In the live demo, Sweeney uses the Karpathy Auto Research project as a simple LLM learning codebase suitable for auto-research demonstrations. ARIA helps download the code, set up the task to run, prepare the GPU, and autonomously iterate on code and hyperparameters. The demo chat shows over 200 experiments already run through the auto-research loop. When asked to do another series of experiments, ARIA reasons that a large architecture shift is risky and instead chooses hyperparameter modifications, then launches a shell call to execute the experiment cycle.

The talk agenda covers ARIA and automated research, a behind-the-scenes look at how Weights & Biases and CoreWeave were used to create ARIA, and key tips for implementing such systems into production.

- ARIA is a Weights & Biases agent for AI research and iteration, integrated into the W&B workspace as a chat interface.
- The agent automates experiment loops by helping download code, set up tasks, prepare GPUs, and iterate on code and hyperparameters.
- The demo uses the Karpathy Auto Research project and reports over 200 experiments run through the auto-research loop.
- ARIA makes risk-aware decisions during experimentation, such as preferring hyperparameter changes over large architecture shifts.
- The talk also covers building ARIA with Weights & Biases and CoreWeave and gives tips for productionizing agent systems.