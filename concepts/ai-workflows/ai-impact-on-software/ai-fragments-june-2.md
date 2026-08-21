---
domain: ai-workflows
subdomain: ai-impact-on-software
concept: ai-fragments-june-2
title: Fragments: June 2
sources:
  - title: "Fragments: June 2"
    url: "https://martinfowler.com/fragments/2026-06-02.html"
    author: "Martin Fowler"
    date: "2026-06-02"
---

# Fragments: June 2

Martin Fowler's June 2 fragments survey a range of AI-related issues in software engineering and society. He begins with Greg Wilson's critique of dodgy metrics for assessing AI developer productivity, noting that while qualitative measures like asking developers if they feel more productive are flawed, they remain among the best available evidence given the inherent difficulty of measuring productivity. Fowler also references Benedict Evans' historical observation that a century of automating accounting did not reduce the number of accountants, suggesting that forecasts of AI's impact on jobs are unreliable due to effects like Jevons paradox and the changing nature of work.

On AI models, Fowler discusses Stephen O'Grady's analysis showing closed models lead on benchmarks but open models are catching up faster over time (e.g., 13-18 months to match GPT-4, but only 2-7 months for GPT-4o). He highlights GPTZero's investigation of an Ernst & Young Canada report where over half of the references were hallucinated, warning that AI-generated misinformation can poison the internet's knowledge pool. Conversely, Mozilla's use of AI to identify latent security bugs in Firefox demonstrates defensive potential, with monthly fixed bugs jumping from 17-31 to 423 in April 2026.

Fowler also covers Pavel Voronin's concept of "generative debt," where LLMs treat technical debt as precedent, amplifying both good and bad code patterns. He notes Andy Osmani's analogy of the developer as the GIL (Global Interpreter Lock) for AI agents, emphasizing that human attention is the bottleneck in orchestrating many agents. Finally, Jamie Hurst's reflection from Booking.com highlights that while the cost of building software has collapsed, the cost of organizational alignment has risen, and productivity gains are often captured as output volume rather than quality, squeezing out thinking and mentoring time.

- Measuring AI developer productivity is fundamentally hard; qualitative metrics like self-reported productivity are weak but still useful.
- Historical automation in accounting did not eliminate jobs, so forecasts of AI's impact on work are unreliable.
- Open AI models are closing the capability gap with closed models at an accelerating pace.
- Hallucinated citations in AI-generated reports (e.g., EY Canada) can poison the internet's knowledge base, while AI also enables security bug finding at scale.
- Technical debt becomes 'generative debt' when LLMs imitate existing code patterns, and human attention becomes the limiting factor when orchestrating many AI agents.