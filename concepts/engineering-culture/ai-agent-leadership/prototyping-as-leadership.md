---
domain: engineering-culture
subdomain: ai-agent-leadership
concept: prototyping-as-leadership
title: Prototyping as Leadership: How a CTO Ships with AI Agents
sources:
  - title: "Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company"
    url: "https://www.youtube.com/watch?v=bdHaOXZOhcM"
    author: "AI Engineer"
    date: "2026-08-20T14:00:21+00:00"
---

# Prototyping as Leadership: How a CTO Ships with AI Agents

Hursh Agrawal, CTO at The Browser Company, argues that AI agents have made the manager schedule usable as building time, allowing leaders to ship between two and ten pull requests weekly despite fifteen recurring meetings and seven direct reports. This shift changes building from a hobby to core leadership work, because frontier models change rapidly and hands-on experience is needed to calibrate judgment rather than relaying opinions from Twitter (Agrawal, 2026).

Building also improves communication: a working prototype is more persuasive than quarterly arguments about model capability, and leaders are well-suited because they hold business context, making their steering more valuable per token. The practical workflow is an overnight loop: a coworker agent gathers context from Slack and the issue tracker for twenty minutes, hands a prompt to a coding agent at 5pm, and the leader reviews results in the morning. This is used for features, prompt hill-climbing against eval sets from feedback dumps, and training small classifiers end to end (Agrawal, 2026).

Caveats are significant: the approach relies on trustworthy CI, feature flags, and prototype branches, and Agrawal acknowledges his own code has caused incidents. He also advises leaders to avoid certain tasks and never add reviewers to code they have not read, preserving accountability and quality (Agrawal, 2026).

- AI agents turn a CTO's manager schedule into building time, enabling 2-10 PRs per week.
- Hands-on prototyping lets leaders calibrate model capabilities and persuade engineers with working examples instead of arguments.
- The core loop is overnight: context assembly, 5pm agent execution, morning review.
- It works only with strong CI, feature flags, prototype branches, and personal review of AI-written code.
- Leaders' business context makes their AI-assisted steering especially high-leverage.