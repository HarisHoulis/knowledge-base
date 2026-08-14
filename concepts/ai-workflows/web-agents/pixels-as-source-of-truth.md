---
domain: ai-workflows
subdomain: web-agents
concept: pixels-as-source-of-truth
title: Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori
sources:
  - title: "Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori"
    url: "https://www.youtube.com/watch?v=Ki980nV0__0"
    author: "AI Engineer"
    date: "2026-08-12T13:37:06+00:00"
---

# Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori

Dhruv Batra argues that while AI agents will dominate web interactions, the long tail of websites will not provide APIs or MCP servers. He uses a school district FOIA request to illustrate that mundane workflows still rely on emailing scans and attaching PDFs, and such offices are unlikely to publish programmatic interfaces. The head of distribution might adapt, but the 200 million active sites with slow-changing infrastructure will not.

Reading HTML is not a sufficient fallback, because much of the page's state is not written as static text. A basketball score loads asynchronously via JSON, and a 'sold out' indicator is simply a quantity of zero rendered by a script that grays out an option. This makes the browser a rendering engine rather than a document viewer, meaning pixels are the ultimate source of truth. Batra calls this the bitter lesson for web agents: per-site scaffolding does not generalize, so the universal interface is the visual output.

Yutori's Navigator model embodies this approach by taking screenshots and emitting clicks, while occasionally writing JavaScript when it is faster, then verifying results on screen. It reportedly misses only 8 out of 300 trajectories on a benchmark that Batra thinks should be retired, suggesting that computer-use models are becoming practical despite latency and cost challenges.

- The long tail of websites will never publish APIs, so agents must operate through the browser's rendered output.
- Much web content is stateful and rendered client-side, making pixels the only reliable representation of truth.
- Computer-use models can generalize across sites by acting on screenshots rather than bespoke HTML parsing.
- Hybrid approaches that mix visual understanding with generated JavaScript offer a faster path in some cases.
- Current benchmarks may understate real-world performance, as the model missed only 8 of 300 trajectories.