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

Vibe coding accelerates software prototyping, but AI agents frequently recommend insecure configurations, creating security vulnerabilities. Drawing on experience building applications for Thoughtworks' global marketing, the authors identify a critical gap: AI assistants lack security context and often suggest default or permissive settings. To mitigate these risks, they propose a multi-layered approach: writing a security context file that explicitly guides AI behavior, carefully reviewing AI permission requests, establishing a daily security intelligence feed to keep models updated on emerging threats, and providing builders with secure-by-default harnesses and templates. These practices shift security from an afterthought to an integrated part of the AI-assisted development workflow.

- AI agents often recommend insecure configurations, leading to security problems in vibe-coded applications.
- A security context file can guide AI assistants to make safer choices during code generation.
- Developers should be cautious with AI permission requests to avoid excessive access or unintended actions.
- A daily security intelligence feed and secure-by-default templates help operationalize security in AI-driven development.