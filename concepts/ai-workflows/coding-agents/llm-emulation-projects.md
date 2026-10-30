---
domain: ai-workflows
subdomain: coding-agents
concept: llm-emulation-projects
title: Building an NES Emulator as a Neural Network with Opus 5.5
sources:
  - title: "dbreunig/nesformer"
    url: "https://simonwillison.net/2026/Oct/30/nesformer/"
    author: "Simon Willison"
    date: "2026-10-30"
---

# Building an NES Emulator as a Neural Network with Opus 5.5

Drew Breunig used prompts with Opus 5.5 to explore whether a Nintendo Entertainment System's chip and RAM could be emulated with a neural network model rather than FPGAs, as done in MISTRs. The initial prompt asked the model to read a blog post on a similar technique and assess feasibility, including what model size would be needed and whether smaller, faster models could hit standard clockspeed.

A follow-up prompt committed to building it "just for fun," accepting slower performance, with the goal of having the weights and a CLI that can be pointed at a ROM. The model reportedly located and used Christopher Pow's NES CPU conformance tests (nestest.txt), a collection released 15 years ago, to guide the work.

- Opus 5.5 was prompted to assess emulating NES chip and RAM with a neural network instead of FPGAs
- The project was pursued for fun, prioritizing having weights and a ROM-running CLI over speed
- The model found and used Christopher Pow's 15-year-old NES CPU conformance tests