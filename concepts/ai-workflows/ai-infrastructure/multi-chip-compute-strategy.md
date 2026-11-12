---
domain: ai-workflows
subdomain: ai-infrastructure
concept: multi-chip-compute-strategy
title: Anthropic's Multi-Chip Compute Strategy and Compute Multipliers
sources:
  - title: "Anthropic's IPO roadshow video"
    url: "https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/"
    author: "Simon Willison"
    date: "2026-11-11"
---

# Anthropic's Multi-Chip Compute Strategy and Compute Multipliers

In Anthropic's IPO roadshow video, co-founder Tom Brown describes how Anthropic trains and serves Claude across all four major chip families: AWS Trainium, Google TPUs, NVIDIA GPUs, and AMD GPUs. This was an early, unconventional bet on a multi-chip strategy, since each chip requires its own tailored software and inference stack, which is expensive and difficult to build. Anthropic has been doing this for years and claims to have become very good at it.

A concrete example is the company's 2026 work with AMD GPUs. Historically, onboarding a new chip platform took dozens of engineers months of work; this time an AI system (referred to as Mythos) got Claude running on AMD in just three days with basically no human intervention, porting or writing almost 100% of the kernels.

The second driver of compute advantage is the rate of discovery of compute multipliers. Anthropic focuses on total effective compute, the multiplicative product of physical capacity times discovered multipliers. A 4x multiplier means a model can be trained with 25 units instead of 100, or the same 100 units can train a model that would previously have required 400. These multipliers stack and compound, creating a competitive advantage that is hard to replicate. Brown suggests this could accelerate toward recursive self-improvement, with Claude discovering compute multipliers entirely by itself.

Simon Willison notes that Anthropic's multi-chip strategy was hinted at in their September postmortem of three recent issues, which described bugs affecting only their TPU deployments. He also extracted a transcript of the video using MacWhisper since no official transcript was provided.

- Anthropic trains and serves Claude across AWS Trainium, Google TPUs, NVIDIA GPUs, and AMD GPUs, an early bet on a multi-chip strategy requiring tailored software stacks per chip.
- An AI system got Claude running on AMD GPUs in three days with minimal human intervention, porting nearly all kernels, versus months of engineering work previously.
- Anthropic optimizes total effective compute as physical capacity multiplied by discovered compute multipliers, which stack and compound as a durable competitive advantage.
- Brown expects compute multiplier discovery to accelerate toward recursive self-improvement, with Claude finding multipliers autonomously.