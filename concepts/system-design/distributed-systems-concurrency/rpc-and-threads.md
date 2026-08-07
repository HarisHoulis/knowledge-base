---
domain: system-design
subdomain: distributed-systems-concurrency
concept: rpc-and-threads
title: Lecture 2: RPC and Threads
sources:
  - title: "Lecture 2: RPC and Threads"
    url: "https://www.youtube.com/watch?v=gA4YXUJX7t8"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-02-07T23:54:55+00:00"
---

# Lecture 2: RPC and Threads

In this lecture from MIT 6.824, the instructor explains why Go is the chosen language for the course's labs. Go is preferred because it offers strong support for threads and synchronization, a convenient remote procedure call (RPC) package, type and memory safety, garbage collection, and simplicity. These features are particularly beneficial for distributed programming, where programs often need to communicate across multiple machines and handle concurrent operations. [MIT 6.824 Lecture 2](https://www.youtube.com/watch?v=gA4YXUJX7t8)

The lecture emphasizes the importance of threads (called goroutines in Go) for managing concurrency. In distributed systems, a single program may need to interact with many clients or servers simultaneously, and threads provide a straightforward way to express these parallel activities. The combination of threads and garbage collection is highlighted as a key advantage, as it eliminates the need for manual reference counting and reduces bugs related to memory management. [MIT 6.824 Lecture 2](https://www.youtube.com/watch?v=gA4YXUJX7t8)

RPC is introduced as a central mechanism for enabling programs on different machines to communicate. Go's built-in RPC package simplifies this process compared to languages like C++, making it easier to build distributed systems. The instructor also mentions the 'Effective Go' document as a recommended resource for learning the language. [MIT 6.824 Lecture 2](https://www.youtube.com/watch?v=gA4YXUJX7t8)

- Go's support for threads, locking, and synchronization makes it ideal for concurrent distributed programming.
- The combination of threads and garbage collection simplifies shared object management in multithreaded programs.
- Go's convenient RPC package facilitates communication between programs on different machines.
- Type safety, memory safety, and simplicity reduce the likelihood of bugs compared to languages like C++.