---
domain: ai-workflows
subdomain: healthcare-ai
concept: clinical-note-omission-errors
title: Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo
sources:
  - title: "Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo"
    url: "https://www.youtube.com/watch?v=yqF6XhzbWBk"
    author: "Sebastian Fox"
    date: "2026-08-22T17:00:32+00:00"
---

# Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo

The talk examines failure modes in AI-generated clinical notes, focusing on ambient scribes. The most dangerous errors are not obvious hallucinations but clinically plausible omissions—details like jaw pain in a headache patient that would signal giant cell arteritis. These omissions read as normal notes and can go uncorrected, leading to missed diagnoses. Real-world studies show about 1 in 20 notes carry a serious error, 1 in 5 have important omissions, and over 1 in 10 contain hallucinations, yet almost none are tracked in adverse event reporting. The speaker illustrates how subtle transcription and generation problems—like converting 'just happened' into 'abrupt sudden onset'—create red flags that drive inappropriate workups. He argues that current evaluation systems fail to catch high-stakes, low-visibility errors and proposes a need for better detection of missing information and clinical context.

- Omission errors—key symptoms left out of AI-generated notes—are more dangerous than obvious hallucinations because they look clinically valid.
- Production data shows ~5% serious error rate and ~40% overall error rate in ambient scribe notes, with no adverse event reporting in most systems.
- Errors originate in both transcription (mishearing words) and generation (inferring, reversing decisions), e.g., 'just happened' becomes 'abrupt sudden onset'.
- Current automated checks catch only a small fraction of high-stakes errors; most sit below the line, silently affecting patient care.