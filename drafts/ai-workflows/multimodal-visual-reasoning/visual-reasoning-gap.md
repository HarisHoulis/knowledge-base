---
domain: ai-workflows
subdomain: multimodal-visual-reasoning
concept: visual-reasoning-gap
title: The Best Models Still Reason Like Toddlers — Andrew Dai
sources:
  - title: "The Best Models Still Reason Like Toddlers — Andrew Dai, Elorian"
    url: "https://www.youtube.com/watch?v=A_I8mw8yfns"
    author: "AI Engineer"
    date: "2026-09-23"
---

# The Best Models Still Reason Like Toddlers — Andrew Dai

In this talk, Andrew Dai (co-founder and CEO of Illumine) argues that today's cutting-edge models — Claude, ChatGPT, and Gemini — remain far from any definition of AGI when it comes to visual thinking, and that examples of failure are easy to reproduce in minutes. He contrasts human visual reasoning with the models' heavy reliance on pattern recognition, which makes them good at identifying plants, animals, and flowers but actively hinders them on complex questions. In one example, given a chessboard image and asked how many white cells it contains, the models answer "32" because they see part of the board, hallucinate the full board, and fall back on the rule that chessboards have 32 same-colored squares.

A second example from the game Catan shows the models over-analyzing detail and failing at spatial navigation: asked how many roads the blue player has, one model answered 10 by counting roads off the playing field, when the correct count is seven. A robotics example shows "contextual amnesia" — the model fails to notice that a robot arm has lifted a lid, and omits that the robot is turning on the stove, because models cannot maintain consistency over long videos and easily lose track of what is happening.

Dai offers a simple test for distinguishing visual comprehension (recognition) from visual reasoning: ask how long a human would need to answer the same question from the same image or video. Recognition questions — identify the game, name the flower, count three pieces — can be answered in under a second, and advanced models handle them correctly. Reasoning questions require looking at the picture in detail and paying attention to different things, which in Daniel Kahneman's framing is slower "System 2" thinking; this is where today's advanced models fail. The practical takeaway for builders is to keep visual tasks very simple, otherwise they will encounter a lot of hallucinations.

On evaluation, Dai pushes back on benchmark optimism. People cite 85–90% scores on ARC-AGI as evidence we are on the way to AGI, but he notes the benchmark images are only 32×32 or 64×64 pixels, and challenges anyone to name a real-world, complex problem that reduces to a 32-by-32 pixel problem.

- Frontier models handle visual thinking very differently from humans; failure cases (chessboard white-cell count, Catan road count, robotics video) are easy to reproduce.
- Pattern recognition makes models strong at identifying objects but causes hallucination on complex visual questions — e.g. answering "32" for a partially visible chessboard.
- Models suffer "contextual amnesia" and lose consistency over long videos, missing events like a robot arm lifting a lid or a stove being turned on.
- Use the one-second test to separate recognition/comprehension from reasoning; recognition tasks work, reasoning tasks fail, so keep visual tasks simple in production systems.
- Skepticism toward visual benchmarks: ARC-AGI images are 32×32 or 64×64 pixels, so high scores don't demonstrate readiness for real-world complexity.