---
domain: ai-workflows
subdomain: cybersecurity-rl
concept: hacking-ladder
title: Teaching AI to Find Real Vulnerabilities: Professional LLM and RL Security Training
sources:
  - title: "Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd"
    url: "https://www.youtube.com/watch?v=ZFxh7sqbUZo"
    author: "AI Engineer"
    date: "2026-08-01T00:30:06+00:00"
---

# Teaching AI to Find Real Vulnerabilities: Professional LLM and RL Security Training

David Brumley, a professor at Carnegie Mellon University and chief AI and science officer at Bugcrowd, discusses how to design reinforcement learning environments for cybersecurity. He argues that as software is shipped faster than ever, machines must be able to check it at scale. He parallels AI training with successful human hacking education, citing the story of Richard Zhu, a 17-year-old who learned to hack through picoCTF by Googling required information, studying write-ups, and practicing on gradually harder challenges. Two years later, Zhu won Pwn2Own, becoming the first person to hack a Tesla and earning $375,000 and a new car (Brumley, 2026).

The talk introduces two axes for designing RL tasks for LLMs: target difficulty and exploitation difficulty. Target difficulty ranges from toy problems through CTF and synthetic problems up to hardened targets. Exploitation difficulty ranges from simply finding a bug and triggering a crash, to achieving arbitrary read/write in memory and full arbitrary code execution. Brumley emphasizes that whether training frontier models like Anthropic or private models, instructors should follow these two axes to create tasks that increase in target difficulty while teaching specific cybersecurity skills (Brumley, 2026).

Hacking, Brumley explains, is fundamentally a ladder. This structure makes cybersecurity particularly well-suited to reinforcement learning, as a ladder of tasks with clear oracles enables sequential skill acquisition. By using the same methodology that has produced elite human hackers, AI agents can be trained to identify vulnerabilities and eventually execute sophisticated exploits (Brumley, 2026).

- Human hacking education based on graduated CTF challenges and write-up emulation is the model for teaching AI agents.
- RL cybersecurity environments should be designed along two axes: target difficulty (toy to hardened) and exploitation difficulty (crash to arbitrary code execution).
- Hacking is a ladder, making it naturally compatible with reinforcement learning's sequential task structure.
- The approach applies to both frontier models and privately tuned LLMs.
- Practical success is illustrated by Richard Zhu, who went from picoCTF to winning Pwn2Own by hacking a Tesla.