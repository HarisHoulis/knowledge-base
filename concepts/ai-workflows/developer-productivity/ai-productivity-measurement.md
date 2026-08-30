---
domain: ai-workflows
subdomain: developer-productivity
concept: ai-productivity-measurement
title: Fragments: June 2 — AI Productivity, Metrics, and the Changing Developer Role
sources:
  - title: "Fragments: June  2"
    url: "https://martinfowler.com/fragments/2026-06-02.html"
    author: "Martin Fowler"
    date: "2026-06-02"
  - title: "Twelve ways to be wrong"
    url: "https://third-bit.com/2026/05/20/twelve-ways-to-be-wrong/"
    author: "Greg Wilson"
    date: "2026-05-20"
  - title: "AI job exposure"
    url: "https://www.ben-evans.com/benedictevans/2026/5/24/ai-job-exposure"
    author: "Benedict Evans"
    date: "2026-05-24"
  - title: "Behind the scenes hardening Firefox"
    url: "https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/"
    author: "Mozilla"
    date: "2026-05"
  - title: "Technical debt is a prompt now"
    url: "https://pavelvoronin.com/technical-debt-is-a-prompt-now/"
    author: "Pavel Voronin"
    date: "2026"
  - title: "AI sustainable"
    url: "https://jamiehurst.co.uk/2026-05-24_ai-sustainable"
    author: "Jamie Hurst"
    date: "2026-05-24"
---

# Fragments: June 2 — AI Productivity, Metrics, and the Changing Developer Role

Martin Fowler's June 2 fragment collection surveys recent posts about AI in software development. He opens with Greg Wilson's critique of common AI productivity metrics—lines of code, tickets closed, or dev surveys—and acknowledges each has flaws. Fowler himself defends self-reported productivity as weak but useful evidence when better measures are unavailable, framing it as a dim light in an environment where true measurement is impossible (Fowler, 2026; Wilson, 2026).

- Common AI productivity metrics such as lines of code, tickets closed, or self-reported productivity are flawed, but qualitative self-reports may still offer useful signal when quantitative measures are lacking.
- Historical automation of accounting did not eliminate accountants; Jevons paradox and changing job definitions make AI job-impact forecasts unreliable.
- LLMs treat existing code as precedent, so technical debt becomes 'generative debt' that models reproduce, compounding maintenance issues.
- AI can be used for defense: Mozilla's improved LLM tooling helped fix 423 security bugs in April 2026, up from 17–31 per month in 2025.
- Developer attention is the bottleneck for AI agent workflows, analogous to Python's GIL; agent orchestration must be designed around this single serial resource.