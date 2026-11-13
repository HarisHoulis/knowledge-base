---
domain: ai-workflows
subdomain: agentic-engineering
concept: generated-glossary
title: Generated Glossary
sources:
  - title: "Bliki: Generated Glossary"
    url: "https://martinfowler.com/bliki/GeneratedGlossary.html"
    author: "Martin Fowler"
---

# Generated Glossary

Large organizations use specialized vocabulary that LLMs don't know from training, making agents less effective in those domains. Fowler describes a technique of using an LLM to mine organizational text (documents, emails, chat logs) for single words and recurring multi-word phrases that form meaningful terms, flagging both terms new to the model and known terms used in unfamiliar ways—the latter often causing the most confusion. The generator then drafts dictionary-style definitions, including alternative definitions where usage differs by context.

Human domain experts review and correct the draft, after which the glossary is stored where other LLMs can consult it, in a token-efficient form, under version control, and on a regular refresh schedule by agents and humans. For large glossaries, only terms and links to definitions need be loaded initially, with full definitions fetched on demand.

Glossaries should respect Domain Driven Design's Bounded Context: different parts of an organization—including source code—may use subtly different definitions, so separate glossaries per context are often better than one standard glossary. Fowler urges resisting a single canonical glossary, since the value is often in highlighting differing usage across contexts; comparing glossaries (e.g. code-derived vs. human text) can be instructive.

In Agentic Engineering, glossaries inform code generation so names fit enterprise vocabulary, and harness sensors can check usage in internals and UI. Glossaries can also mark terms that should not be used (e.g. internal names in customer-facing UI, or deprecated terms with effective periods). Fowler frames this as a simple but useful part of domain modeling, ontologies, and explicit context layers in enterprise data.

- Use an LLM to mine organizational text for specialized terms, including familiar words used in unfamiliar ways
- Have human experts review and correct the generated definitions before use
- Respect bounded contexts: prefer separate glossaries over one standard glossary, and compare them to reveal differing usage
- Keep the glossary version-controlled, token-efficient, and refreshed on a schedule; load full definitions on demand for large glossaries
- Use glossaries to guide code generation and to flag forbidden or deprecated terms