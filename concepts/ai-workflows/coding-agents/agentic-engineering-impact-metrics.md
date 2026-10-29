---
domain: ai-workflows
subdomain: coding-agents
concept: agentic-engineering-impact-metrics
title: GitHub Octoverse 2026: Agentic Engineering Triples Output Metrics
sources:
  - title: "GitHub Octoverse 2026"
    url: "https://simonwillison.net/2026/Oct/28/github-octoverse-2026/"
    author: "Simon Willison"
    date: "2026-10-28"
---

# GitHub Octoverse 2026: Agentic Engineering Triples Output Metrics

Simon Willison highlights GitHub's Octoverse 2026 report as a stark representation of agentic engineering's impact on the platform. Merged pull requests tripled in under a year to 220 million per month, commits more than tripled to 7.38 billion per month (with most growth in the second half of the year), and new repository creation doubled to 30.3 million per month.

The report adds new breakdowns by industry and for repositories involving interoperability or reverse engineering. Methodology notes describe how GitHub classified data: pushes by country were summed and adjusted for VPN bias using LLM classification to extract ISO country codes from user profiles; public repositories created 2022–2026 were sorted into NAICS sectors via a fine-tuned multilingual embedding model using name, description, topics, and README from random samples per year.

Interoperability counts cover public repositories whose name, description, topics, or README mention interoperability or reverse engineering or related terms such as clean room implementation, drop-in replacement, or protocol re-implementation.

- Merged PRs tripled to 220M/month in 2026, commits more than tripled to 7.38B/month, and new repos doubled to 30.3M/month
- GitHub attributes the surge to agentic engineering, with most commit growth in the second half of the year
- Country-level push stats were adjusted for VPN bias using LLM classification of profile locations
- Industry classification used a fine-tuned multilingual embedding model over repo name, description, topics, and README
- A new interoperability/reverse-engineering category tracks terms like clean room implementation and drop-in replacement