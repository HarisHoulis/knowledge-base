---
domain: ai-workflows
subdomain: multi-agent-systems
concept: batch-multi-agent-llm-workflows
title: Batch Intelligence at Scale: Cost-Efficient Multi-Agent LLM Workflows with Built-In Resilience
sources:
  - title: "Presentation: Batch Intelligence at Scale: Cost-Efficient Multi-Agent LLM Workflows with Built-In Resilience"
    url: "https://www.infoq.com/presentations/scaling-multi-agent-llm-batch/"
    author: "Aditya Mulik"
    date: "2026-11-10"
---

# Batch Intelligence at Scale: Cost-Efficient Multi-Agent LLM Workflows with Built-In Resilience

Aditya Mulik describes how Walmart Global Tech deployed multi-agent LLM workflows across 4,700 stores for nightly batch inventory forecasting. The system runs as a batch workload rather than an interactive one, and the presentation focuses on the production hurdles encountered at that scale: schema violations, cross-department data mismatches, and network drops.

To address these failures, the team used MCP grounding and loop agents, giving the workflows built-in resilience against malformed outputs and inconsistent data across departments. These mechanisms let the batch pipeline recover from errors rather than aborting on the first problem.

On cost, Mulik reports cutting cloud inference spend from over $100k per month to roughly $10k per month by shifting from provisioned throughput units (PTUs) to pay-as-you-go pricing. The talk frames this as a key lesson for running LLM workloads economically at scale.

- Multi-agent LLM workflows can run as nightly batch jobs across thousands of locations (4,700 stores at Walmart).
- Production failures included schema violations, cross-department data mismatches, and network drops.
- MCP grounding and loop agents were used to build resilience into the workflows.
- Switching from PTUs to pay-as-you-go cut inference costs from $100k+ to ~$10k per month.