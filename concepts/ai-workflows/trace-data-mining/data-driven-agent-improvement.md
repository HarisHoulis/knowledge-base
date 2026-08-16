---
domain: ai-workflows
subdomain: trace-data-mining
concept: data-driven-agent-improvement
title: Improving Agents is a Data Mining Problem
sources:
  - title: "Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain"
    url: "https://www.youtube.com/watch?v=CvRngaQZQ3Y"
    author: "Vivek Trivedy"
    date: "2026-08-12"
---

# Improving Agents is a Data Mining Problem

In this talk, Vivek Trivedy of LangChain argues that continuously improving AI agents is fundamentally a data mining problem. The recipe begins with shipping an agent into the real world, then collecting a large volume of trace data from every tool call, API interaction, message, and CLI operation. This data becomes the raw material for understanding and improving agent behavior. Trivedy emphasizes that observability and continual learning are tightly coupled: agents operating in environments produce trace data, and continual learning for agents mirrors human reflection—acting, observing outcomes, and updating knowledge or definitions in response to feedback (Trivedy, "Improving Agents is a Data Mining Problem").

Unlike traditional software, where code can be read and reasoned about directly, agents are composed of prompts, tools, skills, hooks, middlewares, and sometimes even swarms of sub-agents. This makes it extremely difficult for humans to predict how a prompt change will affect behavior across different domains. As the industry trades determinism for autonomy, new tools and systems are needed to understand agents operating autonomously. Trivedy shares how LangChain centralizes trace data in tracing projects and then uses agents to read those traces—searching for both good and bad interactions, user satisfaction signals, and technical anomalies. This mined data then drives data-driven experiments to validate whether new prompts, tools, or orchestration patterns actually improve performance.

The core takeaway is that agent improvement should not be based on intuition alone; it requires a closed loop of shipping, tracing, mining, and experimenting. By treating traces as a dataset, teams can systematically uncover failure modes, discover patterns, and test hypotheses, making continual learning a tangible engineering practice rather than a buzzword.

- The key to improving agents is collecting and mining trace data from real-world deployments.
- Continuous improvement follows a loop: ship the agent, collect traces, mine the data, then run experiments.
- Observability and continual learning are tightly coupled—trace data enables reflection and knowledge updates.
- Agent systems are harder to reason about than traditional code, so data mining over traces is necessary to understand them.
- Mining traces can reveal good and bad interactions, user sentiment, and technical issues, informing targeted improvements.