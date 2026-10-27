---
domain: ai-workflows
subdomain: enterprise-ai-platforms
concept: fast-feedback-ai-platform
title: How a Trading Firm Ships New AI Models the Same Day
sources:
  - title: "How a Trading Firm Ships New AI Models the Same Day - Noyan Tokgozoglu, Optiver"
    url: "https://www.youtube.com/watch?v=aGIUg8zKI8A"
    author: "AI Engineer"
    date: "2026-10-27"
---

# How a Trading Firm Ships New AI Models the Same Day

Noyan Tokgozoglu, who leads the AI development team at market maker Optiver, describes how the firm scales AI when profits and losses are at stake. Optiver trades its own money with no customers, executing over 10 million trades per day, evaluating millions of instruments, and processing petabytes of data daily across more than 10 global offices. Technically, the firm takes in large amounts of data, builds models, and makes decisions from them as efficiently as possible.

The key difference from a traditional tech company is the feedback loop. Where consumer companies measure engagement over days and revenue over months or years, Optiver resets its balance to zero each day and sees the P&L impact of a change within hours. That speed cuts both ways: missing an opportunity during a special market event can be very expensive, so decisions must be made quickly, measured effectively, and acted on readily.

To operate this way, Optiver built its own AI platform around a few principles. It must be modular, since new models and paradigms (cycles, swarms, graphs) appear constantly and any valuable one needs to be measured and then implemented. Measurement must exist at every level: external benchmarks are not enough because internal data distributions differ, so internal benchmarks matter. Because traders are smart and high-initiative, the platform is self-service, but with good defaults to prevent chaos, and AI engineers are embedded next to traders to learn how they work and feed that knowledge back into the platform. Safety matters too, since agents going out of control could harm the stack, and the company is broadly AI-native, with everyone using AI in somewhat different ways.

- Daily P&L resets give Optiver an hours-long feedback loop on AI changes, versus months or years for consumer tech companies
- The platform is modular so new models and paradigms can be measured against internal benchmarks and adopted quickly if valuable
- Traders are high-initiative users, so the platform is self-service but ships with good defaults to avoid chaos
- AI engineers are embedded alongside traders to translate trading needs into platform capabilities
- Agent safety is a first-class concern given the potential to damage the stack