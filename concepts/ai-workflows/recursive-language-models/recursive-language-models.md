---
domain: ai-workflows
subdomain: recursive-language-models
concept: recursive-language-models
title: It's Tokens All The Way Down: How RLMs are Different
sources:
  - title: "It's Tokens All The Way Down: How RLMs are Different — Kevin Madura, AlixPartners"
    url: "https://www.youtube.com/watch?v=xo68uCibfm8"
    author: "Kevin Madura (AlixPartners)"
    date: "2026-09-09"
---

# It's Tokens All The Way Down: How RLMs are Different

Kevin Madura introduces Recursive Language Models (RLMs), a paradigm where the model treats context as an interactive symbolic environment—typically a Python REPL—rather than sending tool calls as external JSON strings. This allows the model to write and execute its own code, inspect results, and iteratively reason within the environment. A second key capability is delegation: the RLM can spawn sub-LLM calls, recursively decomposing problems and letting each subordinate model interpret its subtask in the same REPL context. This shifts control from rigid orchestration to model-driven decision-making, aligned with the 'bitter lesson' that as models improve, they should rely more on the model itself to determine what it needs to do.

- RLMs interact with a symbolic environment like a REPL, unlike conventional tool calls that return strings to external programs.
- RLMs can delegate subtasks to other language models, enabling recursive problem decomposition and application of logic.
- This design lets models decide their own actions and code, reducing the need to manually manage context windows.
- RLM approaches show strong performance on long-context benchmarks such as ULong and Browse Comp, even outperforming more expensive tool-call baselines.
- RLMs fit a DSPy-inspired philosophy: define clear inputs and outputs, then let the model handle the internal implementation.