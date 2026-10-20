---
domain: ai-workflows
subdomain: agentic-software-creation
concept: invisible-software
title: The Future of Software is Invisible
sources:
  - title: "The Future of Software is Invisible"
    url: "https://www.youtube.com/watch?v=P00lzZaxv8U"
    author: "Kent C. Dodds"
    date: "2026-10-20"
---

# The Future of Software is Invisible

Kent C. Dodds argues that SaaS products face serious disruption not from hobbyist rewrites of major software, but from a shift toward what he calls "invisible software": a future where software is created by billions of people rather than millions. He stresses that this does not mean everyone becomes a programmer; a supermarket employee or a hairdresser simply wants their problems solved and their lives made easier, not to hand-write applications.

The mechanism is agents. Dodds cites agent benchmarks (bug fixing, terminal work, computer control) that started around one task in seven in 2024 and now see agents completing more than four out of five tasks, with every benchmark trending up and to the right. As agents become more capable, AI will create software to solve users' problems even when those users neither know nor care that custom code is behind the solution.

His concrete illustration is his hairdresser Victoria: a proactive bot notices four free windows on Thursday and offers to message regular customers due for a haircut. She says yes, and the agent writes, commits, and deploys an app that finds those customers, connects to her iMessage and Stripe, and lets her review and send messages in real time. She never thought of creating such an app, and her agent created it for her.

A practical corollary is that agent-driven development multiplies PRs and deployments, making CI speed and concurrency critical. Dodds notes his validation pipeline takes nearly 12 minutes and that agent PRs hit concurrency limits, which is why he adopted a faster CI provider to release at "the speed of AI."

- SaaS is threatened by a shift to "invisible software" created by billions of people via agents, not by mass manual programming.
- Agent benchmarks show rapid improvement, from roughly one in seven tasks in 2024 to more than four in five now.
- Users want problems solved, not to write code; agents will write, commit, and deploy custom apps on their behalf.
- The hairdresser example shows an agent building and deploying a personalized app integrated with iMessage and Stripe.
- Agent-driven development increases PR volume, making CI speed and unlimited concurrency essential.