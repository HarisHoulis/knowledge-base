---
domain: ai-workflows
subdomain: domain-expert-agents
concept: planner-authored-skills
title: We Let Our Financial Planners Write the Agents
sources:
  - title: "We Let Our Financial Planners Write the Agents — Matthew Ragone, Range"
    url: "https://www.youtube.com/watch?v=gpmze-6ueGU"
    author: "AI Engineer"
    date: "2026-10-12"
---

# We Let Our Financial Planners Write the Agents

Matthew Ragone, a certified financial planner at Range, describes how non-engineer financial planners built the AI agents the firm uses daily. The starting point was chatbot-style assistance—pasting client messages in for rewording—which saved minutes but left all work manual. The real shift came from recognizing that the planner's constraint is not writing speed but presence: a planner can only be in one place at a time, so value comes from work done while they are elsewhere. Now an agent drafts a full cash-flow or insurance analysis for one client while the planner is on a call with another, and the planner reviews and corrects the draft before anything reaches the client.

The agent never sends anything on its own; the planner checks each recommendation before the client sees it. Two conditions made this possible: the agent must work where the work happens rather than in a separate chat window requiring copy-paste, and it must know how Range does planning, not how planning works in general. This firm-specific know-how is captured as a "skill"—the firm's way of doing a specific job written down so the agent can follow it.

Skills are created in five steps—select, train, package, test, release—none of which require writing code, but each of which requires deep understanding of the work, which is why they must be authored by the people who perform it. Selection favors recurring weekly work where quality is instantly recognizable and bad drafts are obvious, starting with low-complexity, high-manual-labor processes like cash-flow analysis and insurance checking. Training means walking the agent through real past client cases from start to finish while voicing judgments out loud—not just what is being opened but why, what is being looked for, and what would prompt a question.

Packaging a skill goes beyond a list of steps: the two most important elements are the questions the agent should ask before starting (what it needs to know, what it should confirm rather than guess) and the restrictions it must never violate. In Range's case the main rule is that the agent never sends anything directly to the client—it creates a draft and the planner decides whether to send it or adjust it. Writing only the steps yields something that merely works on its own; writing the questions and limits yields something that can be trusted.

- Financial planners at Range, none of whom write code, author the agents they use daily; the agent drafts analyses while the planner is occupied elsewhere, and the planner reviews every draft before it reaches a client.
- The planner's real constraint is being in one place at a time, not writing speed, so value comes from work done in parallel rather than faster manual work.
- Agents must operate where the work happens (not a separate chat window) and must encode how the firm does planning, not generic planning knowledge—captured as a firm-specific "skill."
- Skills are built in five no-code steps—select, train, package, test, release—and must be authored by the people who do the work because they require deep judgment about quality.
- Packaging must include the questions the agent should ask and the restrictions it must never violate (e.g., never send to clients directly); steps alone produce something that works, questions and limits produce something trustworthy.