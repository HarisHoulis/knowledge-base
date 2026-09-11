---
domain: system-design
subdomain: workflow orchestration
concept: workflow-orchestration-scaling
title: Netflix Reworks Conductor for 420 Million Monthly Workflow Executions and 10X Larger Workflows
sources:
  - title: "Netflix Reworks Conductor for 420 Million Monthly Workflow Executions and 10X Larger Workflows"
    url: "https://www.infoq.com/news/2026/09/netflix-conductor-4-workflow/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Leela Kumili"
    date: "Fri, 11 Sep 2026 14:17:00 GMT"
---

# Netflix Reworks Conductor for 420 Million Monthly Workflow Executions and 10X Larger Workflows

Netflix has reworked its Conductor workflow orchestration engine to handle larger workloads. Conductor 4.0 increases the supported workflow size from about 2,500 tasks to 30,000 tasks and reduces p99 workflow evaluation latency by roughly 40% (Kumili 2026).

The redesign separates workflow metadata from task data, moves evaluation to asynchronous processing, and introduces dynamic worker allocation and concurrency controls (Kumili 2026). According to the article title, Conductor handles 420 million monthly workflow executions (Kumili 2026).

- Conductor 4.0 increases maximum workflow size from ~2,500 tasks to 30,000 tasks.
- p99 workflow evaluation latency is reduced by ~40%.
- Workflow metadata is separated from task data.
- Evaluation is moved to asynchronous processing.
- Dynamic worker allocation and concurrency controls are introduced.