---
domain: ai-workflows
subdomain: llm-evaluation
concept: comparison-grids-for-llm-outputs
title: Comparing GPT-6 Astra and GPT-5.6 Models with Pelican SVGs
sources:
  - title: "The Pelican comparison grid for Astra is pretty interesting"
    url: "https://simonwillison.net/2026/Sep/4/astra-pelicans/"
    date: "2026-09-04"
---

# Comparing GPT-6 Astra and GPT-5.6 Models with Pelican SVGs

Simon Willison used a prompt to generate SVGs of pelicans riding bicycles across GPT-6 Astra at different reasoning levels and compared them visually against GPT-5.6 Sol, Terra, and Luna in a grid. The grid was both fun and surprisingly useful for identifying qualitative differences in output quality and cost efficiency.

- GPT-6 Astra pelicans were significantly better than GPT-5.6 Sol pelicans, even at lower reasoning levels; every Astra pelican from low to xhigh looked better than the best Sol pelican.
- Astra below max still did not reliably depict pelican legs on both sides of the frame, indicating a persistent image generation limitation.
- Astra is about twice the price of Sol per token, but uses fewer tokens at each reasoning level, narrowing the actual cost difference.
- Astra low produced a better pelican than any GPT-5.6 Sol level for 9.55 cents, making it more cost-effective than spending more on other models.
- Input token counts differed: Astra and Luna used 16 input tokens while Sol and Terra used 26, suggesting a possible closer relationship between Astra and Luna.