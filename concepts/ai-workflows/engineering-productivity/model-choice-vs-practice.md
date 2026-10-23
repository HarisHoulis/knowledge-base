---
domain: ai-workflows
subdomain: engineering-productivity
concept: model-choice-vs-practice
title: Better AI Models Won't Fix Your Engineering Team
sources:
  - title: "Better AI Models Won't Fix Your Engineering Team — Nicholas Arcolano, Jellyfish"
    url: "https://www.youtube.com/watch?v=Ve2bAarPA2I"
    author: "AI Engineer"
    date: "2026-10-22"
---

# Better AI Models Won't Fix Your Engineering Team

Nicholas Arcolano, head of AI and research at Jellyfish, argues that when teams fail to get results from AI, the problem is usually not the model but how the team uses it. He draws a golf analogy: clubs (models) have genuinely improved over time, just as model benchmarks keep climbing, but an instructor would still tell a bad golfer that the basics matter more than new equipment. Jellyfish combines AI coding-tool and agent telemetry with engineering workflow and outcome data across hundreds of thousands of developers at roughly 1,300 companies.

A natural experiment tested whether model choice drives output. When Cursor pushed Grok to the top of its UI and changed auto-mode behavior, Jellyfish saw a huge spike in Grok usage and the biggest model-switch it had recorded. Plotting each engineer's change in Grok share against their relative change in merged-PR throughput versus peers showed a cloud centered on zero — no statistical correlation. Switching everyone to Grok didn't change results.

Arcolano then narrows to a curated dataset of about 50,000 engineers across 447 companies using Cursor and Claude, measuring merged PRs per engineer per week. He stresses that the tool and the model are interconnected, and that what matters is how well engineers use them — skills, Cursor rules, system tuning, and the tricks AI engineers learn to improve their workflows. The golfing equivalent is knowing how to get out of a bad situation rather than buying new clubs.

- Model benchmarks keep improving, but model choice alone showed no correlation with engineer PR throughput in Jellyfish's data
- A UI-driven mass switch to Grok produced no measurable change in merged PRs per engineer relative to peers
- The tool and model are interconnected; how engineers use them (rules, tuning, skills) matters more than which model
- Analysis draws on a curated dataset of ~50,000 engineers across 447 companies using Cursor and Claude