---
domain: ai-workflows
subdomain: agentic search / RL training
concept: reinforcement-learning-search-agents
title: Where RL Will Take Search
sources:
  - title: "Where RL Will Take Search — Maximilian-David Rumpf, SID.ai"
    url: "https://www.youtube.com/watch?v=iJVxxxHM_Oc"
    author: "Maximilian-David Rumpf (AI Engineer)"
    date: "2026-09-16"
---

# Where RL Will Take Search

Maximilian-David Rumpf, founder and CEO of SID.ai (a stealth-ish AI lab for search), argues that agents are a new paradigm for search: they deliver vastly higher quality results, roughly twice as likely to find the right documents, but at 100–1,000x the cost of a classical search query and in minutes rather than milliseconds. Because agents spend 30–50% of their tokens on searching, usually early in a task to gather context, the target is to make that search step much cheaper and faster (https://www.youtube.com/watch?v=iJVxxxHM_Oc).

His proposed structure is to move searching out of the main agent into a sub-agent, and to train that sub-agent with reinforcement learning. Classical search is a pipeline of chained, locally optimized models (query rewrite, search backend, reranker) where decisions are baked in at design time and compute per question is fixed. Crucially, a reranker may know the results are insufficient but can only return them anyway, which accrues a long tail of failures that designers patch with edge cases (https://www.youtube.com/watch?v=iJVxxxHM_Oc).

The historical pattern Rumpf invokes is that machine design outperforms human design: computer vision moved from primitive edge detection to narrow, locally optimized models to VLMs that handle all parts of the pipeline; chess moved from Deep Blue's human-written rules to Stockfish to AlphaZero and MuZero, which put everything inside the model. He expects search to follow the same arc from BM25 and PageRank, through vectors and rerankers, to pure RL in which no design decisions are baked into the model (https://www.youtube.com/watch?v=iJVxxxHM_Oc).

In practice this looks like one model that goes back and forth with the database: searching, reading results, iterating, setting metadata filters on the fly, constraining its search as much as it wants, and finally producing a ranked list of results — adapting compute to question difficulty. Search suits this because it is verifiable: for a given question you can tell whether the correct document was found, and the environment lets the model attempt the question thousands of times per second during training. He also notes that most of a language model's parts don't need to be extremely performant for this specialization (https://www.youtube.com/watch?v=iJVxxxHM_Oc).

- Agentic search is much better and much worse: ~2x more likely to find the right document, but 100–1,000x more expensive and minutes instead of milliseconds; agents spend 30–50% of tokens on search.
- Classical search is a fixed-compute pipeline of locally optimized models with design-time decisions, whose reranker can recognize bad results but cannot act, producing a long tail of failures patched by edge cases.
- The proposed fix is to hand search to a sub-agent trained with RL, so one model searches, reads, iterates, sets metadata filters on the fly and returns a ranked list, adapting compute to question difficulty.
- Search is a good RL target because it is verifiable (did you find the correct document?) and the environment allows thousands of attempts per second during training.
- The trajectory mirrors computer vision and chess: human-designed rules and narrow models give way to models that absorb the whole pipeline.