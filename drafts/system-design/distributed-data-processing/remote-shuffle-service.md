---
domain: system-design
subdomain: distributed-data-processing
concept: remote-shuffle-service
title: LinkedIn Cuts Spark Shuffle Fetch Failures with Apache Celeborn
sources:
  - title: "LinkedIn Cuts Daily Spark Shuffle Fetch Failures from 750 to 20 with Apache Celeborn"
    url: "https://www.infoq.com/news/2026/11/linkedin-celeborn-remote-shuffle/"
    author: "Leela Kumili"
    date: "2026-11-18"
---

# LinkedIn Cuts Spark Shuffle Fetch Failures with Apache Celeborn

LinkedIn adopted Apache Celeborn as a shared remote shuffle platform across most of its Spark and Flink workloads, cutting daily shuffle fetch failures from roughly 750 to 20 (InfoQ). The move decouples shuffle data from compute nodes by using dedicated storage and replication.

Beyond reliability, the deployment lowered compute costs by 10% and improved application runtimes by 14%. Shuffle costs per task dropped by nearly 90% through dedicated storage, replication, and data-plane optimizations.

The case illustrates how a dedicated remote shuffle service can address both stability and efficiency problems that arise when shuffle data is tied to ephemeral compute nodes.

- Apache Celeborn serves as a shared remote shuffle platform for Spark and Flink at LinkedIn
- Daily shuffle fetch failures fell from ~750 to ~20
- Compute costs dropped 10% and runtimes improved 14%
- Shuffle cost per task fell nearly 90% via dedicated storage, replication, and data-plane optimizations