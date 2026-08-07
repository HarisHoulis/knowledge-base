---
domain: ai-workflows
subdomain: post-training
concept: on-the-job-learning
title: Learning on the Job: The Future of Post-Training — Raymond Feng, Applied Compute
sources:
  - title: "Learning on the Job: The Future of Post-Training — Raymond Feng, Applied Compute"
    url: "https://www.youtube.com/watch?v=k35LeKZEhiE"
    author: "AI Engineer"
    date: "2026-07-31T22:30:06+00:00"
---

# Learning on the Job: The Future of Post-Training — Raymond Feng, Applied Compute

Raymond Feng (AI Engineer, 2026) discusses the evolution of post-training for AI agents, emphasizing the shift from simple Q&A tasks to adapting agents for custom enterprise harnesses. He highlights the increasing demand for plug-and-play deployment where agents can be trained on tasks within existing infrastructure, even without access to the harness source code (Feng, 2026).

Feng describes a simple training setup where an orchestrator manages rollouts by sending prompts to a model, grading responses, and using a training engine to compute weight updates that sync to inference engines. The only essential input for improvement is the graded chats, but this requires a specific format and a controlled environment (Feng, 2026).

To handle longer-horizon tasks, synthetic environments offload environment state outside the training stack. The orchestrator coordinates multiple turns, tool calls, and sandbox interactions, producing a full task trace that enables training on complex workflows (Feng, 2026).

Looking ahead, Feng envisions 'agentic citizens' that can be deployed once and adapt to many out-of-distribution tasks by learning from their interactions, representing a future where agents continuously improve on the job (Feng, 2026).

- Post-training is moving from controlled Q&A to adapting agents to arbitrary harnesses, including those without source code access.
- The training loop relies on graded chats as the core input for weight updates, with an orchestrator, grader, and training engine.
- Synthetic environments extend post-training to long-horizon tasks by externalizing environment state and supporting tool calls.
- The long-term vision is deploy-once agentic citizens that learn and adapt from real-world interactions.
- Custom model training requires methods that work with any harness, not just those owned by the training stack.