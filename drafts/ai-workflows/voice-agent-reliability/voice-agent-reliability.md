---
domain: ai-workflows
subdomain: voice-agent-reliability
concept: voice-agent-reliability
title: I Monitored Crime Audio. Voice Agents Scare Me More.
sources:
  - title: "I Monitored Crime Audio. Voice Agents Scare Me More. — Sumanyu Sharma, Hamming AI"
    url: "https://www.youtube.com/watch?v=qStB9GbppMU"
    author: "Sumanyu Sharma (AI Engineer)"
    date: "2026-09-15"
---

# I Monitored Crime Audio. Voice Agents Scare Me More.

Sumanyu Sharma, founder and CEO of Hamming, previously worked at Citizen, where his team listened to thousands of hours of police radio data and sent millions of alerts across San Francisco, New York, LA, Chicago, and Baltimore [source]. Having monitored crime audio at scale, he argues voice agents scare him more: they are graduating from demos and POCs into production and talking to users at massive scale [source].

Sharma notes voice was "just starting to work" when he began working on reliability in early 2024, and that speech models, hybrid voice-to-voice plus cascading architectures, and the orchestration layer have all meaningfully improved, making it faster to build experiences that are "60% good" in a short period [source]. Voice agents are now connected to calendars, CRMs, HR systems, and reservation systems, so they can take real actions [source]. But the long tail remains hard, and reliability is still the number one problem holding back most voice agent deployments at scale [source].

He contrasts crime, which is decreasing over time, with voice, which is taking off [source]. With roughly a trillion calls per year and most expected to be handled by conversational voice agents within five years, even a 1% error rate implies 10 billion incidents annually [source]. In practice, across the 10,000 agents Hamming monitors, the error rate is closer to 10% [source].

Failure modes include claiming the right policy was found while skipping eligibility or verification steps, applying unauthorized discounts, mishearing what the user said, providing incorrect information, and claiming an appointment was booked when it wasn't [source]. Sharma's personal example: an appointment he believed he booked didn't exist, wasting two hours — and he notes the cost scales dramatically if the person is a parent or grandparent, or if the appointment is for a procedure rather than a checkup [source]. Not every failure carries equal cost; he compares some to "trash fires" that are funny or annoying rather than harmful [source].

- Voice agents are moving from demos into production at scale, and reliability — not capability — is the top blocker to deployment [source].
- Hamming monitors 10,000 agents and observes error rates near 10%, versus the 1% rate that would still mean 10 billion incidents a year given ~1 trillion annual calls [source].
- Common failure modes: skipped eligibility/verification, unauthorized discounts, mishearing users, incorrect information, and false claims that an appointment was booked [source].
- The same failure mode has wildly different costs depending on who is affected (e.g., a parent's procedure vs. a routine checkup) [source].
- Infrastructure improvements — better speech models, hybrid voice-to-voice and cascading stacks — make 60%-good agents fast to build, but the long tail stays hard [source].