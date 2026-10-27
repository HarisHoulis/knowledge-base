---
domain: ai-workflows
subdomain: llm-model-releases
concept: midrange-model-positioning
title: GPT-6.1 Terra: OpenAI's Midrange Visual Reasoning and Computer Use Model
sources:
  - title: "GPT-6.1 Terra"
    url: "https://simonwillison.net/2026/Oct/26/gpt-61-terra/"
    author: "Simon Willison"
    date: "2026-10-26"
---

# GPT-6.1 Terra: OpenAI's Midrange Visual Reasoning and Computer Use Model

Simon Willison covers OpenAI's release of GPT-6.1 Terra, a fast, efficient model positioned around detailed visual reasoning, precise computer use, and clearer, more natural writing. OpenAI describes it as a significant step up from GPT-5.6 Terra, excelling at everyday work tasks like drafting proposals, interpreting technical drawings, filling out forms, and editing videos.

Terra occupies the same tier as Anthropic's Sonnet: neither the cheapest nor the most expensive option, which makes choosing when to use it harder. Willison notes that computer use is a good fit for a cheaper model, since it often runs automated, repetitive tasks. OpenAI's Ted Sanders, quoted from a Hacker News comment, says Terra is probably better than Astra and Sol at technical communication, similar on vision and computer use but much faster, and a bit worse on most other things—a nice midrange API option between Sol and Luna, though not a bombshell for subscribers.

Pricing is $1 per million input tokens and $5 per million output, roughly half the price of GPT-5.6 Terra and GPT-6.1 Sol, and about 10x the price of GPT-6 Luna. Willison benchmarks reasoning levels with his pelican-riding-a-bicycle test; the "max" reasoning pelican cost 11.3161 cents and took 4 minutes 11 seconds, and he published a comparison grid across OpenAI's current frontier lineup (GPT-6 Astra, GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Luna).

- GPT-6.1 Terra targets visual reasoning, computer use, and clearer writing, positioned as a step up from GPT-5.6 Terra
- It sits in the midrange tier like Anthropic's Sonnet, making model selection less obvious
- Priced at $1/M input and $5/M output tokens—about half of Sol and 10x Luna
- OpenAI's Ted Sanders: better than Astra/Sol at technical communication, similar on vision/computer use but much faster, weaker elsewhere
- The max-reasoning pelican benchmark cost 11.3161 cents and took 4m11s