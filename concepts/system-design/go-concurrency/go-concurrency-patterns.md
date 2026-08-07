---
domain: system-design
subdomain: go-concurrency
concept: go-concurrency-patterns
title: Lecture 5: Go, Threads, and Raft
sources:
  - title: "Lecture 5: Go, Threads, and Raft"
    url: "https://www.youtube.com/watch?v=UzzcUS2OHqo"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-02-24T14:08:06+00:00"
---

# Lecture 5: Go, Threads, and Raft

This lecture from MIT 6.824 focuses on Go concurrency patterns for implementing Raft, emphasizing clarity over performance. The instructors argue that the Go memory model reading is not meant to encourage deep reasoning about happens-before relations; instead, programmers should write straightforward code using common patterns like big locks and large critical sections (MIT 6.824, 2020). Concurrency is used primarily to express independent operations (e.g., fan-out RPC calls) cleanly, not to achieve CPU parallelism (MIT 6.824, 2020).

The lecture highlights the use of closures in goroutines, which can capture and mutate variables from the enclosing scope. This is convenient for spawning multiple goroutines in a loop, such as sending RequestVote or AppendEntries RPCs to all servers in parallel. However, a critical pitfall is loop variable capture: if the loop variable is used directly inside the closure, it may be mutated before the goroutine reads it. The safe pattern is to pass the variable as an argument to the goroutine (MIT 6.824, 2020).

- Concurrency is for expressing independent operations in parallel, not necessarily for CPU speedup.
- Use simple locking and big critical sections to make concurrent code easy to reason about.
- Closures allow goroutines to access outer variables, but loop variables must be passed as args to avoid capture issues.
- For Raft, send RPCs (votes, appends) to all peers in parallel using goroutines.