---
domain: system-design
subdomain: concurrency-patterns
concept: go-concurrency-patterns
title: Lecture 5: Go, Threads, and Raft
sources:
  - title: "Lecture 5: Go, Threads, and Raft"
    url: "https://www.youtube.com/watch?v=UzzcUS2OHqo"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-02-24"
---

# Lecture 5: Go, Threads, and Raft

This lecture from MIT 6.824 focuses on practical concurrency patterns in Go for implementing distributed systems labs. The instructors emphasize that concurrency in labs is primarily used for structuring code to express concurrent interactions naturally, not for CPU parallelism. They advise using coarse-grained locking and large critical sections to keep code easy to reason about. Key patterns include using closures with goroutines to capture variables from the enclosing scope, and using WaitGroups to synchronize multiple goroutines. A common pitfall is loop variable capture when spawning goroutines in a loop, which can lead to races and incorrect behavior. The lecture also briefly touches on the Go memory model, cautioning against over-analysis of happens-before relations and instead advocating for writing correct code by following established patterns.

- Concurrency in labs is used for expressiveness, not performance; avoid fine-grained locking and CPU optimizations.
- Use closures to define goroutines inline, capturing variables from the outer scope; beware of loop variable capture.
- Use WaitGroups to wait for multiple goroutines to complete before proceeding.
- Prefer coarse-grained locks and simple correctness over complex lock-free or fine-grained locking schemes.
- The Go memory model is not meant for detailed reasoning; focus on writing correct code using clear patterns.