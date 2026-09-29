---
domain: ai-workflows
subdomain: voice-ai interaction design
concept: act-confirm-or-stop
title: Act, Confirm, or Stop? Smarter behavior for AI assistants, wearables and robots
sources:
  - title: "Act, Confirm, or Stop? Smarter behavior for AI assistants, wearables & robots — Amit Desai, Roku"
    url: "https://www.youtube.com/watch?v=Zd5b40Jbp_k"
    author: "AI Engineer"
    date: "2026-09-15"
---

# Act, Confirm, or Stop? Smarter behavior for AI assistants, wearables and robots

Amit Desai, a voice-AI practitioner who has worked at Alexa, Roku and his own startups, frames voice as the most natural interface but one with a painful other half: it is error-prone, and those errors will persist for a while. Their cost, he argues, will grow as systems move from conversational bots to embodied AI that takes physical or digital actions — if a robot throws your watch out with the trash, that is far worse than playing the wrong song [1].

Desai says there are two knobs for improving user satisfaction with a voice assistant. The familiar one is accuracy: improving wake-word, ASR, NLU (intent classification, entity extraction) and VAD layers point by percentage point. The second, under-used knob is what he calls the "system decision," which he describes as orthogonal to accuracy and which leaves accuracy exactly as it is [1]. He illustrates with a simple music-playing smart speaker: of a thousand spoken requests, human annotation shows 790 correct songs (79%) and 210 wrong ones (21%).

The proposed behavior change is to give the system at least one more option than right-answer or wrong-answer: it may reject the hypothesis and do nothing, saying "sorry, I didn't get that" or asking the user to repeat. The open question is when to stop, quantitatively. Desai argues that guessing a threshold would leave you worse off than a more rigorous approach, and proposes assigning a single confidence score to annotated data points as the basis for that decision [1]. He presents this as a scalable approach applicable across surfaces and devices, not just smart speakers.

- Voice AI has two independent levers for user satisfaction: accuracy and "system decisions" that leave accuracy unchanged.
- The consequences of voice errors grow as AI shifts from answering questions to taking physical/digital actions in embodied systems.
- Adding a stop/reject behavior gives the assistant a third option beyond acting correctly or acting wrongly — e.g. asking the user to repeat.
- The decision of when to stop must be set quantitatively using annotated data and confidence scores; a rough guess performs worse than a rigorous approach.