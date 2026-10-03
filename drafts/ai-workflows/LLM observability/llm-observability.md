---
domain: ai-workflows
subdomain: LLM observability
concept: llm-observability
title: Your LLM App Returned 200 OK. It Was Still Wrong.
sources:
  - title: "Your LLM App Returned 200 OK. It Was Still Wrong. — Marina Petzel, Datadog"
    url: "https://www.youtube.com/watch?v=rTojoVotlD8"
    author: "Marina Petzel, Datadog (AI Engineer channel)"
    date: "2026-10-03"
---

# Your LLM App Returned 200 OK. It Was Still Wrong.

Traditional monitoring relies on golden signals—latency, errors, traffic, and saturation—but these are no longer sufficient for generative AI applications. Unlike traditional programs, the same input to an LLM can produce different outputs, so teams cannot rely only on standard regression testing and must continuously evaluate quality in real-world environments [1].

GenAI also introduces a dynamic cost structure: costs vary by token count, model choice, and context window size, so real-time cost tracking is needed to prevent uncontrolled spending. The talk highlights three main cost risks: token shifting, where context windows are enlarged without financial review and can cause an eightfold cost increase; model drift, where moving from a cheaper model like Haiku 4.5 to a more powerful model like Opus 4.8 can be 15 times more expensive; and uncached value, where repeated API calls without an effective caching layer can make 70% of costs unnecessary, according to Datadog research [1].

Security is another new concern. Instead of only SQL injection or cross-site scripting, LLM apps must defend against operational injections, jailbreaking, and PII leaks in outputs—issues that may not surface as a simple 500 error and require new forms of security monitoring. Quality is also subjective and measured on a spectrum: relevance, accuracy, and completeness. A 200 OK response does not mean the answer was useful or correct, so continuous quality assessment must be integrated directly into the monitoring stack [1].

- Golden signals remain important but are insufficient for GenAI because nondeterministic outputs require continuous quality evaluation.
- LLM costs are dynamic and unpredictable; monitor token shifting, model drift, and uncached/repeated calls to avoid runaway spend.
- New security monitoring is needed for prompt-based attacks, jailbreaking, and PII leakage in outputs.
- HTTP 200 OK is not a quality signal; teams should monitor relevance, accuracy, and completeness of responses.
- Continuous quality assessment should be integrated directly into the monitoring stack.