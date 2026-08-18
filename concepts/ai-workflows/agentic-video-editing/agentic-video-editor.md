---
domain: ai-workflows
subdomain: agentic-video-editing
concept: agentic-video-editor
title: Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful
sources:
  - title: "Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful"
    url: "https://www.youtube.com/watch?v=pPj_tjlvYjA"
    author: "AI Engineer"
    date: "2026-08-18T14:30:38+00:00"
---

# Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful

Ekaterina Deyneka identifies a common gap between recording video and actually posting it, and Reelful is her attempt to close that gap: a user drops in raw footage with a line of direction, and an agent selects usable moments, cuts them together, and generates captions, music, voiceover, and b-roll. She frames this for an AI engineering audience by noting that an agentic video editor is structurally identical to an agentic app builder: a prompt goes in, a sandbox spins up, the agent works inside it with tools and skills, and something renders out the other end (source: Reelful talk). The key difference is that editing real footage is harder than generating from a blank canvas because the agent must judge which take is best, what to drop, and how to produce something polished from noisy or incomplete source material (source: Reelful talk).

The composition layer is built on Remotion, which expresses video as React code, chosen deliberately because agents write code well. Skills carry the editing taste—cut rules, font pairings, when a cutaway actually helps—and a verification pass catches compositions that will not render and sends the agent back for another iteration. All of this is hidden behind mobile templates, so the consumer never sees the pipeline at all (source: Reelful talk). Deyneka emphasizes that the mass-consumer requirement means the entire complexity of the agentic workflow must remain invisible, with the user only seeing the prompt and the final video (source: Reelful talk).

The talk presents a concrete example of applying agentic workflows to a creative, subjective domain. By encoding taste in skills and using a code-based rendering layer, the system turns unstructured footage into a polished product while maintaining a fully automated loop. This design parallels other agentic systems where capabilities are split between a flexible agent and deterministic, verifiable tools (source: Reelful talk).

- Agentic video editing shares the same architecture as agentic app builders: prompt, sandbox, tool-using agent, and rendered output.
- Editing real footage is fundamentally harder than generating video because the agent must judge and discard material, not just create freely.
- Remotion (video as React code) is used because agents are better at writing code than directly manipulating timeline UIs.
- Skills encode editing taste (cut rules, font pairings, b-roll decisions), and a verification pass prevents broken renders before the final output.
- The entire pipeline is hidden behind mobile templates to make the agentic system accessible to mass consumers.