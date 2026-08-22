---
domain: ai-workflows
subdomain: clinical-ai-evaluation
concept: silent-errors
title: Inside 847 Production Clinical AI Notes
sources:
  - title: "Inside 847 Production Clinical AI Notes"
    url: "https://www.youtube.com/watch?v=yqF6XhzbWBk"
    author: "AI Engineer"
    date: "2026-08-22T17:00:32+00:00"
---

# Inside 847 Production Clinical AI Notes

Fox (2026) illustrates how AI-generated clinical notes can be dangerously misleading while appearing routine. He recounts a headache consultation where the AI omitted the patient's jaw pain on chewing—a clue that, combined with age and new headache, points to giant cell arthritis, a same-day emergency. "Nothing in the note is technically wrong," but the dangerous part is the omission.

He cites a real-world study indicating about 1 in 20 notes carried an error serious enough to cause significant harm, with nearly 1 in 5 having important omissions and more than 1 in 10 having hallucinated content. These errors are common and often undetected because ambient scribes are deployed in about a third of US practices without adverse event reporting.

Fox identifies specific failure modes: models inferring red-flag features (e.g., recording "abrupt sudden onset" when the patient said "it just happened") and reversing clinical decisions (e.g., noting tests were arranged when the plan was to hold off). He notes the problem occurs in both transcription and generation layers, and current automated checks catch only a minority of errors, especially missing those with high clinical stakes.

- AI clinical notes can look normal yet omit critical symptoms, leading to missed emergencies like giant cell arthritis.
- Production studies show ~5% of AI notes contain significant harm-level errors; ~20% have key omissions; >10% have hallucinations.
- Ambient scribe deployment (in ~1/3 of US practices) is racing ahead of oversight, with no incident reporting for AI errors.
- Failure modes include inferring red flags from ambiguous patient speech and flipping decisions to the option that was not chosen.
- Current automated checks are inadequate: they catch errors that matter least and miss the high-stakes ones.