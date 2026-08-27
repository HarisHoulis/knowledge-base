---
domain: ai-workflows
subdomain: clinical-ai-evaluation
concept: clinical-note-omissions
title: Inside 847 Production Clinical AI Notes
sources:
  - title: "Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo"
    url: "https://www.youtube.com/watch?v=yqF6XhzbWBk"
    author: "Sebastian Fox"
    date: "2026-08-22T17:00:32+00:00"
---

# Inside 847 Production Clinical AI Notes

The talk exposes dangerous failures in AI-generated clinical notes, focusing on subtle omissions rather than blatant errors. For example, a patient's mention of jaw pain when chewing was omitted from the note, causing the clinician to miss giant cell arteritis—a same-day steroid emergency that can blind the patient within days. The note looks completely fine on the page, but the dangerous part is what isn't there (Fox, 2026).

Real-world data from the largest production study shows about 1 in 20 notes carry an error serious enough to cause significant harm, nearly 1 in 5 have an important omission, and more than 1 in 10 contain a hallucination. Ambient scribes are already used in about a third of US practices and physician AI use doubled last year, yet none of this is tracked through adverse event reporting. Errors silently sit in the medical record, making the system effectively flying blind (Fox, 2026).

The causes lie in both transcription and generation layers. A patient saying "it just happened" can be recorded as "abrupt sudden onset," a red flag for a brain bleed that drives the entire workup. Similarly, a patient who talks out of tests and chooses antibiotics may find the note records the opposite plan: "arrange tests today." Current automated checks catch only the least subtle errors, while the high-stakes ones—that look perfectly plausible—are missed entirely (Fox, 2026).

- Omission of a single symptom (jaw pain on chewing) can transform a routine headache into a missed emergency diagnosis.
- Largest real-world study: 1 in 20 AI notes have serious errors, 1 in 5 have important omissions, and 1 in 10 have hallucinations.
- Ambient scribes are deployed in ~1/3 of US practices, but no adverse event reporting tracks their errors.
- Errors stem from both transcription misinterpretation and generation of plausible-sounding but reversed or invented plans.
- Current automated checks fail to catch the most dangerous errors, which appear unremarkable at face value.