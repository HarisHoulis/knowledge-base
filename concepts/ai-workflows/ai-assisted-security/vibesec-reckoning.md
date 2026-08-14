---
domain: ai-workflows
subdomain: ai-assisted-security
concept: vibesec-reckoning
title: The VibeSec Reckoning
sources:
  - title: "The VibeSec Reckoning"
    url: "https://martinfowler.com/articles/vibesec-reckoning.html"
    author: "Martin Fowler"
---

# The VibeSec Reckoning

Vibe coding has significantly accelerated software prototyping, but AI agents frequently recommend insecure configurations, creating security problems. This issue was observed in practice by Gautam Koul, Lucian Moss, Neil Drew-Lopez, and Daberechi Ruth Edeokoh while building applications for Thoughtworks's global marketing team. They found that the speed of AI-assisted development can inadvertently introduce vulnerabilities if not carefully managed.

To combat these risks, the team learned several key practices. First, they emphasize writing a security context file to guide AI agents toward secure decisions. Second, they advise being cautious with AI permission requests, as over-permissioning can lead to security gaps. Third, they recommend creating a daily security intelligence feed to keep builders informed of emerging threats. Finally, they advocate providing builders with secure-by-default harnesses and templates to reduce the likelihood of insecure configurations.

These measures help maintain a balance between the rapid prototyping benefits of vibe coding and the need for robust security. By embedding security guidance into the AI workflow and equipping developers with safe defaults, teams can leverage AI's speed without compromising on safety.

- Vibe coding accelerates prototyping but AI agents often recommend insecure configurations.
- Write a security context file to guide AI toward secure choices.
- Be cautious with AI permission requests to avoid unnecessary access.
- Maintain a daily security intelligence feed for builders.
- Provide secure-by-default harnesses and templates to reduce risk.