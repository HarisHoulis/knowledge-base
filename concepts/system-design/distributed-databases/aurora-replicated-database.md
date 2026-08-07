---
domain: system-design
subdomain: distributed-databases
concept: aurora-replicated-database
title: Lecture 10: Cloud Replicated DB, Aurora
sources:
  - title: "Lecture 10: Cloud Replicated DB, Aurora"
    url: "https://www.youtube.com/watch?v=jJSh54J1s5o"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-11T15:41:32+00:00"
---

# Lecture 10: Cloud Replicated DB, Aurora

The lecture introduces Aurora, a high-performance reliable database built as a piece of cloud infrastructure on Amazon's own available infrastructure. The paper claims a 35x speedup in transaction throughput, though the comparison system is not well explained. It also explores the limits of performance and fault tolerance using general-purpose storage, ultimately abandoning general-purpose storage in favor of application-specific storage (MIT 6.824, 2020).

The lecture traces the background leading to Aurora, starting with Amazon's EC2 offering. EC2 provided virtual machines with locally attached storage, which worked well for stateless web servers but was problematic for databases. Since storage was attached to the physical hardware, a hardware crash could result in losing access to the data on that hard drive, making EC2 poorly suited for database workloads. This motivates the need for a specialized cloud database design like Aurora (MIT 6.824, 2020).

- Aurora is a cloud database service built on Amazon infrastructure, claiming 35x faster transaction throughput.
- The paper examines the limits of general-purpose storage and decides to build application-specific storage instead.
- EC2's locally attached storage made databases vulnerable to hardware failures, as data could be lost when a server crashed.
- The design of Aurora is presented as a response to the shortcomings of using EC2 with local storage for reliable database services.