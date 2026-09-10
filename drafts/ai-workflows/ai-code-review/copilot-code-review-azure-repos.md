---
domain: ai-workflows
subdomain: ai-code-review
concept: copilot-code-review-azure-repos
title: Copilot Code Review Reaches Azure Repos, Billed Per Review with Reporting Two Days behind
sources:
  - title: "Copilot Code Review Reaches Azure Repos, Billed Per Review with Reporting Two Days behind"
    url: "https://www.infoq.com/news/2026/09/copilot-code-review-azure-repos/"
    author: "Steef-Jan Wiggers"
    date: "2026-09-04"
---

# Copilot Code Review Reaches Azure Repos, Billed Per Review with Reporting Two Days behind

Microsoft has opened GitHub Copilot code review to all Azure DevOps customers for use on Azure Repos, after acknowledging that many customers are not ready to migrate to GitHub [1]. The capability is aimed at organizations remaining on Azure Repos rather than moving their repositories to GitHub.

Billing is usage-based: each review is billed through the Azure subscription linked to the organization, and the resulting charges surface in Azure Cost Management roughly 48 hours after the fact [1]. Organizations can set budgets, but those budgets only notify — they do not halt reviews [1]. Concurrency is limited to five reviews per organization at a time [1].

- Copilot code review in Azure Repos is now available to all Azure DevOps customers, offered in part because many customers are not ready to migrate to GitHub.
- Reviews are billed per use through the organization's linked Azure subscription.
- Cost data appears in Cost Management 48 hours after reviews occur; budgets alert but cannot stop reviews.
- Concurrency is capped at five reviews per organization.