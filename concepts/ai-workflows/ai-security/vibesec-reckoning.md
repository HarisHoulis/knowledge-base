---
domain: ai-workflows
subdomain: ai-security
concept: vibesec-reckoning
title: The VibeSec Reckoning
sources:
  - title: "The VibeSec Reckoning"
    url: "https://martinfowler.com/articles/vibesec-reckoning.html"
    author: "Martin Fowler"
---

# The VibeSec Reckoning

Vibe coding accelerates prototyping, but AI agents often recommend insecure configurations, introducing security risks. The authors—Gautam Koul, Lucian Moss, Neil Drew-Lopez, and Daberechi Ruth Edeokoh—describe their experience building applications for Thoughtworks's global marketing. They found that standard AI-assisted workflows lack security guardrails, so they developed practices to mitigate these vulnerabilities. Key mitigations include writing a security context file to guide AI behavior, cautiously reviewing AI permission requests, maintaining a daily security intelligence feed, and equipping builders with secure-by-default harnesses and templates.

- AI code generation can produce insecure configurations if not explicitly guided.
- A security context file helps align AI recommendations with organizational security policies.
- Always scrutinize AI permission requests to prevent unintended access or changes.
- A daily security intelligence feed keeps builders informed of emerging threats.
- Secure-by-default harnesses and templates reduce the risk of insecure foundational choices.