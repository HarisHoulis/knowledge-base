---
domain: ai-workflows
subdomain: ai-roi-measurement
concept: live-ab-testing-ai-workflows
title: Proving Alpha: Measuring AI's ROI in a Hedge Fund
sources:
  - title: "Proving Alpha: How a Hedge Fund Measures AI's ROI - Hari Kumar, Contour Asset Management"
    url: "https://www.youtube.com/watch?v=ZMZlAn6Pyfg"
    author: "AI Engineer"
    date: "2026-10-24"
---

# Proving Alpha: Measuring AI's ROI in a Hedge Fund

Hari Kumar, head of AI at Contour Asset Management (a ~15-20 person, $6B AUM long/short hedge fund focused on TMT), describes the challenge of demonstrating the return on the firm's AI investment. The core difficulty is that much of the firm's value comes from idea generation and research, where impact on P&L may take six months to a year to materialize, making immediate ROI hard to show. Rather than chasing direct profit attribution, the firm focuses on measuring process improvement step by step.

The central method is running live A/B tests on analysts' research workflows. The firm has about 10 analysts, each covering many companies with long-established processes for forming theses, generating ideas, and validating them. Kumar's team documents an analyst's entire pre-AI process—what data sources they use and what conclusions they reach—then runs the same process with AI tools layered in one at a time, such as agent-assisted expert interviews or agent-conducted consumer surveys.

A concrete example is a three-month cycle between earnings reports for a particular stock: results are tracked first without any LLM tools, then with tools added incrementally. The comparison asks whether the analyst would reach the same conclusion with or without AI, and how long information takes to find manually versus via an agent-based approach—for instance, whether an agent summarizing expert-call notes before the analyst draws conclusions changes the outcome.

Because direct ROI is hard to capture, the firm treats this as a process-oriented measurement: are consumer surveys conducted better, are models updated more efficiently? The goal is to progressively introduce more ROI measurements across research and eventually trading, operations, compliance, and finance.

- Run live A/B tests: document an analyst's pre-AI research process, then repeat it with AI tools added incrementally and compare conclusions.
- Use a defined window (e.g., the three-month cycle between earnings reports) to compare outcomes with and without LLMs.
- Direct P&L attribution is hard because idea-generation impact can take 6-12 months; measure process improvement instead.
- Layer tools one at a time (agent-assisted expert interviews, agent-run consumer surveys) to isolate each tool's effect.