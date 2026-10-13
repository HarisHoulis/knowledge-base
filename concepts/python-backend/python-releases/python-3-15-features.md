---
domain: python-backend
subdomain: python-releases
concept: python-3-15-features
title: Hello Python 3.15, Goodbye 3.10, and Now I Can Use 3.11
sources:
  - title: "Hello Python 3.15, goodbye 3.10, and now I can use 3.11"
    url: "https://simonwillison.net/2026/Oct/12/python-3-15/"
    author: "Simon Willison"
    date: "2026-10-12"
---

# Hello Python 3.15, Goodbye 3.10, and Now I Can Use 3.11

Simon Willison covers the release of Python 3.15, highlighting features most relevant to library and tool maintainers. The headline addition is explicit lazy imports from PEP 810, which let modules be imported only when their symbols are first used—directly addressing the startup cost that plugin systems like his LLM CLI tool incur when plugins pull in heavy dependencies such as sentence_transformers. He also notes the new unpacking-in-comprehensions syntax from PEP 798, which extends PEP 448's unpacking to comprehensions for lists, sets, and dicts.

Another major addition is a built-in sampling profiler called Tachyon (profiling.sampling), joining the renamed tracing profiler profiling.tracing (formerly cProfile). Sampling profilers periodically capture stack traces with low overhead, and the new module can attach to a running process by PID, produce reports, flame graphs, heat maps, and output viewable in the Firefox profiler UI—capabilities Willison previously relied on py-spy for. On performance, Miguel Grinberg's testing against 3.15.0rc3 found results mostly on par with 3.14, except the experimental JIT, which gave a 1.2x boost on a Fibonacci test—the first meaningful JIT gain he has observed.

Because 3.15's release means Python 3.10 is no longer supported, Willison can drop 3.10 from his projects and adopt 3.11 features. He calls out tomllib, asyncio's TaskGroup and timeout(), datetime.UTC, SQLite improvements (including set_authorizer(None), which removes a Datasette workaround), and typing enhancements. He documents using uv to install and pin 3.15 globally and to upgrade installed tools, and plans to land 3.11 improvements across his projects, starting with a Datasette PR removing the set_authorizer workaround and updating several cookiecutter templates to test against 3.11 through 3.15.

- Python 3.15 adds explicit lazy imports (PEP 810), letting modules load on first symbol use—useful for cutting plugin startup costs.
- PEP 798 brings unpacking syntax to comprehensions, e.g. [*L for L in lists] flattening nested lists.
- A new built-in sampling profiler, Tachyon (profiling.sampling), joins the renamed profiling.tracing and can attach to running processes and emit flame graphs and heat maps.
- Miguel Grinberg found 3.15 performance mostly matches 3.14, except the experimental JIT, which showed a 1.2x boost on a Fibonacci test.
- With 3.10 unsupported, Willison can adopt 3.11 features like tomllib, asyncio TaskGroup/timeout(), datetime.UTC, and SQLite set_authorizer(None).