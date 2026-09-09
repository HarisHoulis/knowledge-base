---
domain: system-design
subdomain: stream-processing
concept: flink-operator-autoscaler
title: Netflix Moves toward Open Source Flink Autoscaler for 30,000+ Streaming Jobs
sources:
  - title: "Netflix Moves toward Open Source Flink Autoscaler for 30,000+ Streaming Jobs"
    url: "https://www.infoq.com/news/2026/09/netflix-flink-autoscaler/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Leela Kumili"
    date: "Mon, 07 Sep 2026 14:06:00 GMT"
---

# Netflix Moves toward Open Source Flink Autoscaler for 30,000+ Streaming Jobs

Netflix is transitioning to the open-source Apache Flink Autoscaler for more than 30,000 streaming jobs operating across multiple AWS regions. This operator-level approach addresses the limitations of Netflix's previous cluster-level autoscaler, particularly for complex, stateful pipelines that require finer-grained scaling decisions.

The new approach has yielded significant cost efficiencies. Netflix reports that one team achieved a 58% reduction in annualized Flink compute expenditure, saving approximately $1.1 million per year. This move underscores the value of moving to operator-level autoscaling for large-scale streaming workloads.

- Netflix is moving more than 30,000 streaming jobs to the open-source Apache Flink Autoscaler across multiple AWS regions.
- The operator-level autoscaler overcomes limitations of the previous cluster-level autoscaler for complex, stateful pipelines.
- One team saw a 58% reduction in annualized Flink compute costs, saving about $1.1 million per year.