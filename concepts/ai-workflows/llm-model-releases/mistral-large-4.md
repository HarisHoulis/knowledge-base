---
domain: ai-workflows
subdomain: llm-model-releases
concept: mistral-large-4
title: Mistral Large 4 ("Le chonk") preview
sources:
  - title: "Introducing Mistral Large 4: Le chonk"
    url: "https://simonwillison.net/2026/Oct/6/le-chonk/"
    author: "Simon Willison"
    date: "2026-10-06"
  - title: "Introducing Mistral Large 4: Le chonk"
    url: "https://mistral.ai/news/mistral-large-4/"
    author: "Mistral AI"
  - title: "Mistral Large 4 model page"
    url: "https://artificialanalysis.ai/models/mistral-large-4"
    author: "Artificial Analysis"
---

# Mistral Large 4 ("Le chonk") preview

Mistral announced Mistral Large 4, nicknamed "Le chonk", with a preview available via their API and a promise to release the open weights model at the end of the month (https://mistral.ai/news/mistral-large-4/). The model supports only two reasoning levels, "none" and "high", via the Mistral API.

Simon Willison compared the two reasoning levels using the pelican-riding-a-bicycle test: the "high" output looked better, though it surprisingly used only 2,717 output tokens versus 3,275 for "none" (https://simonwillison.net/2026/Oct/6/le-chonk/). On Artificial Analysis it scores 38, just behind DeepSeek 4.1 Flash, which is a 552B model (https://artificialanalysis.ai/models/mistral-large-4).

That score is a huge improvement on last December's Mistral Large 3, which produced a terrible pelican and scored 9 on Artificial Analysis. The verdict: not a Fable-class model, but Mistral is back to being roughly six months behind the frontier.

- Mistral Large 4 preview is API-only; open weights are promised for the end of the month.
- Only two reasoning levels are exposed via the Mistral API: "none" and "high".
- The "high" reasoning setting produced the better pelican while using fewer output tokens (2,717 vs 3,275).
- It scores 38 on Artificial Analysis, a large jump from Mistral Large 3's 9, but still behind DeepSeek 4.1 Flash.
- Overall it puts Mistral roughly six months behind the frontier, not Fable-class.