---
domain: ai-workflows
subdomain: retrieval-augmented-generation
concept: query-dependent-chunking
title: Stop Chunking Like It's 2022 — Yuval Belfer, AI21 Labs
sources:
  - title: "Stop Chunking Like It's 2022 — Yuval Belfer, AI21 Labs"
    url: "https://www.youtube.com/watch?v=r9OwPx_HoV0"
    author: "AI Engineer"
    date: "2026-09-16T17:00:06+00:00"
---

# Stop Chunking Like It's 2022 — Yuval Belfer, AI21 Labs

Yuval Belfer of AI21 Labs argues that chunking is not dead, despite claims that agentic search makes it obsolete (Yuval Belfer, AI21 Labs). He says tools like grep, ls, and find are useful, but are still not enough when there is a lot of data and many queries, and they cost money/tokens at scale. He claims that if something has been killed, it is more likely retrieval tuning, not chunking. The talk frames chunking as the unglamorous preprocessing stage: pick a chunk size, add 10–20% overlap, index everything, and forget it.

Belfer characterizes fixed chunking as lossy compression: chunks that are too large preserve the whole picture but lose nuance and produce less meaningful embeddings; chunks that are too small lose the big picture and are less efficient (Yuval Belfer, AI21 Labs). He argues there is no single right chunk size per dataset, and that chunking is query-dependent. A FIFA World Cup example illustrates the issue: if data is organized in directories by tournament year, a query such as “which team won the most World Cups” requires visiting every folder and aggregating, which is inefficient.

He says his team tested this by duplicating a dataset several times—six times in the example—instead of only finding the best chunk size per dataset. The transcript cuts off during the explanation of that experiment.

- Agentic search tools such as grep, ls, and find help but do not eliminate the need for chunking at scale with many queries and large data.
- Fixed chunking is a lossy tradeoff: large chunks lose nuance and embedding specificity, while small chunks lose the big picture and efficiency.
- There is no single best chunk size per dataset; chunking is query-dependent.
- The FIFA World Cup example shows that directory-level organization fails aggregate queries like “which team won the most World Cups” without cross-folder aggregation.
- The speaker’s team tested chunking by duplicating a dataset several times—six times in the example—rather than only optimizing chunk size per dataset.