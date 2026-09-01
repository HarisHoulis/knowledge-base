---
domain: ai-workflows
subdomain: ai-coding-security
concept: vibesec-reckoning
title: The VibeSec Reckoning
sources:
  - title: "The VibeSec Reckoning"
    url: "https://martinfowler.com/articles/vibesec-reckoning.html"
    author: "Martin Fowler"
---

# The VibeSec Reckoning

Vibe coding accelerates software prototyping, but AI agents frequently recommend insecure configurations, creating security problems. Building applications for Thoughtworks's global marketing, Gautam Koul, Lucian Moss, Neil Drew-Lopez, and Daberechi Ruth Edeokoh learned that AI-generated code must be carefully guided and constrained to avoid introducing vulnerabilities (Fowler, "The VibeSec Reckoning").

To combat these risks, the team developed a set of practical safeguards. Writing a security context file to guide the AI helps align generated code with security requirements. Being cautious with AI permission requests limits the blast radius of autonomous actions. A daily security intelligence feed keeps builders aware of emerging threats. Providing builders with secure-by-default harnesses and templates reduces the likelihood of misconfiguration (Fowler, "The VibeSec Reckoning").

- AI agents frequently recommend insecure configurations, even when they accelerate prototyping.
- A security context file should be provided to guide the AI's code generation.
- Be cautious with AI permission requests to avoid granting excessive access.
- A daily security intelligence feed helps keep development aligned with current threats.
- Secure-by-default harnesses and templates enable safer vibe coding.