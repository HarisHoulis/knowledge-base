---
domain: ai-workflows
subdomain: ai-in-software-development
concept: ai-agents-and-pipelines
title: Fragments: September 1
sources:
  - title: "Fragments: September 1"
    url: "https://martinfowler.com/fragments/2026-09-01.html"
    author: "Martin Fowler"
    date: "2026-09-01"
---

# Fragments: September 1

Martin Fowler opens by noting his wariness of AI-generated prose and his uncertainty about his own detection ability. He cites Simon Willison's [LLM cliché highlighter](https://tools.simonwillison.net/llm-cliche-highlighter) and the Wikipedia [signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) page, which notes that humans are bad at distinguishing human from LLM text — a 2025 study found detection no better than random chance, and a study of German theses found a 57% recognition rate for AI texts and 64% for human texts.

On long-horizon agents, Fowler points to NVIDIA's [Architecture for Long-Horizon Autonomous Agents](https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/). Their AVO harness combined with Claude Opus 5 was first used for GPU kernel optimization — running for seven days — and then on the ARC-AGI-3 reasoning benchmark. AVO relies on persistent memory (carrying forward prior implementations, evaluation results, compiler/profiler outputs, and accumulated reasoning) and a supervisor that monitors the trajectory for stagnation and redirects toward alternative strategies when the search plateaus, while the main agent decides what to inspect, change, test, and evaluate.

Paul Stack argues in [AI Broke the Assumptions Behind CI](https://stack72.dev/ai-broke-the-assumptions-behind-ci/) that agents iterating across the PR boundary put the feedback loop in the wrong place, regardless of CI speed, and advocates verifying before pushing. Fowler counters that this was always how Continuous Integration works: pull, build and test locally, then push, with slower tests downstream in the deployment pipeline. He agrees it's right to question how pipelines should work with agents, and that CI with humans relies on discipline to run commit tests locally — something we can and should automate for agents. CI is a practice, not just the server, and its conflation of verification and merge coordination is the point, since verification is a necessary part of merging to retain a healthy mainline.

On AI risk, Fowler contrasts Noah Smith's worry about an AI-generated super-virus with Claus Wilke's [skepticism](https://blog.genesmindsmachines.com/p/im-sorry-youre-not-going-to-die-from), who argues computational design of biological systems is unfathomably difficult and that today's AI-assisted researchers routinely fail at far simpler tasks like designing peptide binders. Fowler also notes correlated LLM hallucination — fabricated experts such as Elena Vasquez and Marcus Chen appearing as volcano experts, astronauts, and co-authors across hundreds of AI-generated documents in [non-random pairs and trios](https://arxiv.org/pdf/2606.02184).

- Humans detect LLM-generated text poorly — roughly random chance in one 2025 study, 57%/64% rates for AI/human texts in another.
- NVIDIA's AVO harness (with Claude Opus 5) uses persistent memory and a supervisor to sustain long-horizon tasks, running a GPU kernel optimization for seven days.
- Agents pushing fixes to CI create feedback in the wrong place; Fowler argues local verification before push was always part of Continuous Integration, and CI is a practice, not just a server.
- LLMs produce correlated fake expert ensembles (e.g., recurring co-occurring names) rather than random individual names.
- Fowler cites skepticism that AI can realistically design a super-virus, given how hard computational biology remains.