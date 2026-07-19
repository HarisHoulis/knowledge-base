---
domain: system-design
subdomain: go-concurrency
concept: threads-and-goroutines
title: Lecture 2: RPC and Threads
sources:
  - title: "Lecture 2: RPC and Threads"
    url: "https://www.youtube.com/watch?v=gA4YXUJX7t8"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-02-07T23:54:55+00:00"
---

# Lecture 2: RPC and Threads

This lecture discusses the use of Go (Golang) for distributed systems programming, emphasizing its support for threads (goroutines), garbage collection, type safety, and a convenient remote procedure call (RPC) package. These features make Go particularly suitable for managing concurrency in distributed applications, where a single program often needs to handle multiple simultaneous clients or servers. The speaker explains that threads (goroutines) allow a program to have multiple execution flows within a single address space, enabling efficient handling of concurrent tasks without complex manual memory management. The combination of threads and garbage collection simplifies programming by automatically freeing memory when no thread is using an object, eliminating common bugs like double-free or use-after-free (Source: MIT 6.824 Lecture 2). Additionally, Go's simplicity compared to C++ reduces compiler error complexity and speeds development. The lecture concludes that understanding threads is essential for building distributed systems, as they are the primary tool for managing concurrency.

- Go is chosen for this course due to its thread support, garbage collection, type/memory safety, and convenient RPC package.
- Threads (goroutines) enable a program to handle multiple concurrent tasks, such as serving many clients simultaneously.
- Garbage collection alleviates the burden of manual memory management in multi-threaded programs.
- Go's simplicity reduces debugging time compared to C++.
- Threads are essential for managing concurrency in distributed systems, where a single program interacts with multiple remote machines.