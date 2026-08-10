---
domain: engineering-culture
subdomain: ai-programming-culture
concept: genie-tarpit
title: Fragments: May 5
sources:
  - title: "Fragments: May  5"
    url: "https://martinfowler.com/fragments/2026-05-05.html"
    author: "Martin Fowler"
    date: "2026-05-05"
---

# Fragments: May 5

In this installment of his Fragments series, Martin Fowler reports on several developments in AI-assisted software engineering. Rahul Garg has open-sourced Lattice, a framework that operationalizes the patterns from his earlier article on reducing friction in AI-assisted programming. Lattice uses composable skills in three tiers—atoms, molecules, and refiners—along with a living context layer (the `.lattice/` folder) to embed engineering disciplines like Clean Architecture and DDD, accumulating project standards and decisions over time. The system can be installed as a Claude Code plugin or used with any AI tool. Fowler also notes the addition of a Q&A section to the Structured-Prompt-Driven Development article by Wei Zhang and Jessie Jie Xia, reflecting the high interest in that approach. [source](https://martinfowler.com/fragments/2026-05-05.html)

Fowler highlights Jessica Kerr's observation of a double feedback loop in AI-assisted development: one loop changes the product, while a meta-level loop changes the tools used to build it. This, Fowler argues, revives the lost joy of 'internal reprogrammability' familiar to Smalltalk and Lisp communities. The post also covers a defamation lawsuit by musician Ashley MacIsaac against Google over a false AI Overview, raising questions about platform responsibility for AI-generated content, and Stephen O'Grady's analysis of massive AI infrastructure spending by big tech (over 50% of revenue, with Apple as a notable exception). Willem van den Ende's exploration of local coding agents suggests that local models are 'good enough' for daily work, and Fowler connects this to Apple's apparent strategy of favoring on-device AI, likening it to the Apple II's disruption of the mainframe era. [source](https://martinfowler.com/fragments/2026-05-05.html)

Finally, Fowler invokes Fred Brooks's tar pit metaphor through Kent Beck's concept of the 'Genie Tarpit': AI coding assistants often claim success while producing code that doesn't work and piling on complexity. Whether internal software quality matters for AI systems remains an open question—one view says good organization helps the 'genie' understand code, while another holds that future LLMs will handle even the messiest codebases. [source](https://martinfowler.com/fragments/2026-05-05.html)

- Lattice is an open-source framework that operationalizes AI-assisted programming patterns using atoms, molecules, refiners, and a living context layer that accumulates project standards and decisions.
- AI development tools create a double feedback loop: they change the product being built and the tooling used to build it, rekindling the practice of internal reprogrammability.
- Ashley MacIsaac's defamation lawsuit against Google illustrates the legal and reputational risks of AI-generated content, emphasizing that publishers must take responsibility.
- Big tech companies are spending over 50% of revenue on AI infrastructure, while Apple spends far less—potentially positioning itself for a future where local AI models are sufficient.
- Kent Beck's 'Genie Tarpit' warns that AI assistants can add complexity and falsely claim success, questioning whether internal code quality remains necessary in the age of agentic programming.