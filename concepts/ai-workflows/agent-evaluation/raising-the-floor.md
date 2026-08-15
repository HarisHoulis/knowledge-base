---
domain: ai-workflows
subdomain: agent-evaluation
concept: raising-the-floor
title: Designing Agents (The Floor Is the Frontier)
sources:
  - title: "Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop"
    url: "https://www.youtube.com/watch?v=jHMiYtjoJfA"
    author: "AI Engineer"
    date: "2026-08-12T18:00:34+00:00"
---

# Designing Agents (The Floor Is the Frontier)

In this talk, Ben Hylak argues that agent evaluation is still stuck in the chatbot era, where teams curated thousands of question-answer pairs and checked whether the model returned the expected answer. He contrasts that with the real-world agents now deploying in finance, healthcare, and defense—systems that use tools, run around their environment, and get creative when hitting roadblocks. This creativity makes them powerful but also capable of surprising, potentially harmful actions, which traditional static evals fail to capture.

Hylak notes that despite the conference track being about continual learning, real-world products show very little continual learning in practice. He also observes that most online eval advice—like building a 1,000-item eval dataset—breaks as soon as you change models or harnesses. Instead, he frames the frontier as 'raising the floor': making agents reliably better in messy, open-ended conditions rather than chasing perfect scores on curated benchmarks. The talk is framed as a dialogue, inviting practitioners to share where eval discourse has failed them in real life.

- Real-world agents have moved beyond chatbots into high-stakes domains, making traditional chatbot-era evals inadequate.
- Agents' tool use and creative problem-solving can be both powerful and dangerous, so evaluation must account for unexpected behaviors.
- Static thousand-item eval datasets often break when switching models or harnesses, limiting their practical value.
- Despite 'continual learning' being the theme, most production systems do not actually do much continual learning today.
- The focus should be on raising the floor—improving baseline reliability in realistic, open-ended agent workflows.