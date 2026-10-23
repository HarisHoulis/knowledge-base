---
domain: ai-workflows
subdomain: domain-specific-foundation-models
concept: transaction-foundation-model
title: A Bank Trained Its Own Foundation Model to Catch Fraud
sources:
  - title: "A Bank Trained Its Own Foundation Model to Catch Fraud — Freddy Lecue, Wells Fargo"
    url: "https://www.youtube.com/watch?v=UB6hoWyh3B0"
    author: "AI Engineer"
    date: "2026-10-23"
---

# A Bank Trained Its Own Foundation Model to Catch Fraud

Wells Fargo built its own foundation model trained from scratch on transaction data rather than language, arguing that in financial services the most valuable data is structured and tabular rather than linguistic. The speaker notes that while language models like Claude and ChatGPT are useful, simply loading banking data into them is not necessarily the best approach; instead the bank wanted a single backbone model that could be reused across divisions for tasks like credit scoring, fraud detection, anti-money laundering, and marketing.

- Wells Fargo pre-trained transformer blocks from scratch on its own transaction data, using only the architecture and no open-source weights, on its GPU cluster for days to weeks.
- The model predicts the next transaction or next token in a transaction, analogous to next-token prediction in language models, with the representation then adapted for downstream tasks.
- The transaction model reportedly outperforms XGBoost, including on latency, with better false-positive reduction and higher detection rates in fraud detection.
- Scale is large: billions of transactions and millions of accounts per month, with hundreds of transactions per customer across debit, credit, and check channels.
- The approach aims to replace many division-specific models with one reusable backbone that learns customer transaction representations at scale.