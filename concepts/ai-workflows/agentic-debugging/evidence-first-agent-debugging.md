---
domain: ai-workflows
subdomain: agentic-debugging
concept: evidence-first-agent-debugging
title: Debugging with Agents: Facts, Hypotheses, and Controls
sources:
  - title: "Fragments: October 21"
    url: "https://martinfowler.com/fragments/2026-10-21.html"
    author: "Martin Fowler"
---

# Debugging with Agents: Facts, Hypotheses, and Controls

Martin Fowler's fragments post highlights Gergely Orosz's frustration that entrants to his explicitly "No AI" essay competition used AI, and Orosz's point that when it takes effort to determine how much of a piece is AI versus human, readers will simply assume it is all AI and disengage (Fowler agrees, saying he "flips the bozo bit" once he hears LLM voice). Fowler adds caveats: his own AI-detection may be inaccurate, humans may adopt AI-ish styles, and there are valid uses such as Jim Highsmith's second-brain tool for Parkinson's or translation help for non-native English speakers. He also notes the cancellation of the Grace Hopper Celebration, attributing it to the impact of anti-diversity crusades on funding.

The bulk of the post summarizes Cindy Sridharan's long article on debugging code you no longer understand. Sridharan argues agents are not humans and should be leaned on for their strengths rather than made to replicate human problem-solving. A key anti-pattern: having an agent start by reading the code. Instead, an agent should first collect all available evidence about the bug, then formulate hypotheses from the code that best explain the observations.

She separates a bottom tier of facts (raw behavioral data) from an upper tier of hypotheses (inferences), framing diagnosis as finding the hypothesis that satisfies every fact. Her three-step process: identify the most important signals, best done by giving the agent a high-quality control (a behavior that does not exhibit the bug, such as triggering vs. non-triggering requests, different builds, or environments); focus on hypotheses that fit the signals, where the most valuable signals are those satisfied by only a few hypotheses (a hypotheses-by-signals table helps); then validate promising hypotheses against every fact as a constraint.

Fowler observes that his own most valuable contributions across the three bugs were not code knowledge but picking a control, choosing a constraint, and rejecting an unvalidated hypothesis, and that engineers who thrive in an agent-native world will be good at designing verification loops. Because agents process huge volumes of raw data, aggregation that helps humans can destroy signal for agents, and more logging gives agents more to work with. Yet the human is still needed to direct the agent: in each case the agent could reach the root cause but did not set up a control until asked.

- Readers who suspect AI involvement will often assume a piece is entirely AI and disengage, so even light AI use risks losing the audience.
- Sridharan's anti-pattern: agents should not start by reading code; they should first gather evidence, then form hypotheses.
- Diagnosis is framed as finding the hypothesis that satisfies every fact, with a control (a non-buggy behavior) used to isolate the most valuable signals.
- Agents benefit from raw data rather than human-oriented aggregation, so more logging helps them; humans remain necessary to direct controls and validation.
- Fowler notes the cancellation of the Grace Hopper Celebration and its impact on gender diversity efforts in tech.