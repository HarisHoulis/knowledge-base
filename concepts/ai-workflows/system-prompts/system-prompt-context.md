---
domain: ai-workflows
subdomain: system-prompts
concept: system-prompt-context
title: Quoting Claude Opus 5 System Prompt: Export Controls Notice
sources:
  - title: "Quoting Claude Opus 5 system prompt"
    url: "https://simonwillison.net/2026/Aug/9/claude-opus-5-system-prompt/#atom-everything"
    date: "2026-08-09T23:31:39+00:00"
---

# Quoting Claude Opus 5 System Prompt: Export Controls Notice

The article presents an excerpt from the Claude Opus 5 system prompt, which includes a factual notice about the temporary suspension of Claude Fable 5 and Mythos 5 in June 2026 due to U.S. Department of Commerce export controls. This notice is embedded because the event occurred after the model's training-data cutoff, ensuring the model has accurate context when questioned about the suspension. Without such context, the model might hallucinate or provide incorrect answers about the situation.

The prompt instructs Claude to acknowledge the suspension as fact, treat the export controls as a current political topic, provide a fair and accurate account without sharing personal opinions, and point users to Anthropic's official statement for further details. It also advises the model to check for newer information when search is available, and otherwise suggest visiting Anthropic's site. This example demonstrates how system prompts can be used to inject critical temporal context, thereby improving factual reliability and preventing misinformation about recent events.

- System prompts can include post-training-cutoff events to keep models factually accurate.
- Claude is instructed to confirm the suspension and treat export controls as a political topic without personal opinion.
- The prompt directs users to Anthropic's official statement for more details.
- This illustrates a practical use of system prompts to shape model behavior around current events.