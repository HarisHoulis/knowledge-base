---
domain: ai-workflows
subdomain: self-improving-agents
concept: agent-skills
title: From 36% to 100%: How Self-Improving Agents Write Their Own Skills
sources:
  - title: "From 36% to 100%: How Self-Improving Agents Write Their Own Skills — Rafal Wilinski, Runlayer"
    url: "https://www.youtube.com/watch?v=u-o0sW9nwmk"
    author: "AI Engineer"
    date: "2026-10-07"
---

# From 36% to 100%: How Self-Improving Agents Write Their Own Skills

Rafal Wilinski, a founding engineer at Runlayer, argues that agents can become self-improving by capturing the knowledge they gain while solving hard problems and turning it into reusable "skills" (https://www.youtube.com/watch?v=u-o0sW9nwmk). He defines a skill as an instruction an agent can read when it senses the knowledge is relevant, enabled by progressive disclosure: the agent initially sees only a brief description, then loads the full skill into context when useful, changing its action trajectory (https://www.youtube.com/watch?v=u-o0sW9nwmk).

He frames skills as critical because models are increasingly capable of long-horizon, multi-step work, as shown by the METR benchmark, but with longer reasoning comes the risk of agents going down deep rabbit holes, defending false theses across hundreds of tool calls, and wasting time, tokens, and money (https://www.youtube.com/watch?v=u-o0sW9nwmk). Skills steer the agent toward the right goal from the start. Valuable skills are the rituals nobody wants to rediscover—script sequences, function switches, or the exact wording needed to handle a picky corporate client—and without them agents would likely fail, often expensively (https://www.youtube.com/watch?v=u-o0sW9nwmk).

Wilinski identifies three major problems with skills. The first is that they are local and developer-centric: the ecosystem consists of markdown files, JSON files, CLI commands, and Git repositories, which works for developers but not for AI implementation leads who must roll out strategy across non-technical staff (https://www.youtube.com/watch?v=u-o0sW9nwmk). The central challenge he raises is how non-technical people can create and share skills, which the transcript cuts off before fully addressing (https://www.youtube.com/watch?v=u-o0sW9nwmk).

- Skills are instructions agents load on demand via progressive disclosure, letting them change course when relevant knowledge is detected.
- Longer-horizon agent reasoning raises the cost of a bad initial trajectory, making skills essential for steering agents toward correct goals.
- Valuable skills encode hard-won, non-obvious company rituals that agents would otherwise have to rediscover from scratch and likely fail at.
- The current skills ecosystem is developer-centric (markdown, JSON, CLI, Git), creating a barrier for non-technical employees to create and share skills.