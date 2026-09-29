---
domain: ai-workflows
subdomain: decision models
concept: decision-models
title: Jev introduces a new shape of LLM: System One / decision models
sources:
  - title: "Jev introduces a new shape of LLM - System One, aka Decision Models"
    url: "https://simonwillison.net/2026/Sep/21/jev/"
    author: "Simon Willison"
    date: "2026-09-21"
  - title: "Introducing System One models and Jev"
    url: "https://typesafe.ai/blog/introducing-system-one-models-and-jev"
    author: "TypeSafe AI"
  - title: "Kev"
    url: "https://github.com/jaredpalmer/kev"
    author: "Jared Palmer"
---

# Jev introduces a new shape of LLM: System One / decision models

TypeSafe AI unveiled Jev, described as the first example of a new category of model they call "System One models" (a name Simon Willison prefers to replace with "decision models", agreeing with Maggie Appleton). Jev still accepts text input, but instead of text output it returns floating point numbers corresponding to categories, yes/no questions, ratings, and associated confidence scores — "unstructured state in, typed probabilistic decisions out." (simonwillison.net)

Jev is fast and cheap: it charges only for input (output is free) at $0.042 per million tokens, cheaper than OpenAI's GPT-5 Nano at $0.05/million. You compose a "state" object — a string, array of strings, or set of name-value pairs describing an article, a customer, or any record — send it with one or more questions, and get a reply for each. A single state can carry as many questions as fit in the context window, and questions are evaluated in parallel, so many questions take roughly the same time as one. (simonwillison.net)

The decision-model framing makes clear where Jev fits: anything expressible as a classification task, such as spam detection, label suggestion, prioritization, and ranking. Willison also experimented with search reranking — fetching 100 likely matches with an inexpensive algorithm like BM25, then having Jev score those candidates for relevance against the original query. (simonwillison.net)

Willison finds Jev uncomfortable as a further regression toward black-box machine learning. LLMs already are black boxes, but you can at least ask them to justify decisions (without guarantees of accuracy); Jev returns only a floating point number, leaving no way to know which content signals tipped it off. Bias concerns become central — he hopes nobody uses Jev to rank job applicants, since the number could conceal unseen bias that is tricky to pick apart experimentally (in one experiment scoring Bay Area cities on whether they were a "Good city?", Jev rated Cupertino top and East Palo Alto bottom). Evals and structured experiments matter more than with regular LLM projects, but Jev is cheap enough that hundreds or thousands of experimental prompts cost only cents. Community activity around Jev has been intense, including open-weight recreations like Kev (built on Qwen 3.5, producing 0.8B, 4B, and 9B models) and an already-emerging JevBench benchmark for comparing "Jev-class decision models". (simonwillison.net)

- Jev, from TypeSafe AI, is the first "System One model" (aka decision model): text in, floating point numbers for categories, yes/no answers, ratings, and confidence scores out.
- Pricing is input-only at $0.042/million tokens with free output, undercutting GPT-5 Nano; questions are evaluated in parallel, so many questions cost about the same time as one.
- Best fit is classification-shaped work: spam detection, label suggestion, prioritization, ranking, and search reranking over candidates fetched by cheap algorithms like BM25.
- Jev removes even the illusion of explanation — only a number comes back — raising bias concerns and making evals and structured experiments more important.
- Within a week of release, the community produced open-weight alternatives like Kev and a JevBench benchmark for decision models.