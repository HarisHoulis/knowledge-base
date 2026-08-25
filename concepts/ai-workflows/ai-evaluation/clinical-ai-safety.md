---
domain: ai-workflows
subdomain: ai-evaluation
concept: clinical-ai-safety
title: Inside 847 Production Clinical AI Notes
sources:
  - title: "Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo"
    url: "https://www.youtube.com/watch?v=yqF6XhzbWBk"
    author: "Sebastian Fox"
    date: "2026-08-22T17:00:32+00:00"
---

# Inside 847 Production Clinical AI Notes

Sebastian Fox, a medical doctor and founder of Composo, exposes how AI-generated clinical notes can look flawless while hiding critical omissions. A seemingly routine headache note missed the patient's jaw pain on chewing, which combined with age and new headache points to giant cell arteritis—a same-day emergency. The omission is more dangerous than any obvious error because the note is technically correct but dangerously incomplete (Fox, 2026).

Beyond omissions, the talk details outright hallucinations: a man in his 20s with tonsillitis received a chest pain diagnosis, diabetes medication, and a nonexistent hospital address, leading to an erroneous diabetic eye screening invitation. A large real-world study found about 1 in 20 production notes contained an error serious enough to cause significant harm, nearly 1 in 5 had an important omission, and more than 1 in 10 had a hallucination (Fox, 2026).

Fox notes that ambient AI scribes are already used in about a third of US practices, yet there is no adverse event reporting or tracking. Errors silently persist in medical records. Analyzing notes from three leading ambient scribes, he found that most errors, especially the high-stakes ones, are missed by automated checks. Examples include interpreting a patient's "I don't know, it just happened" as "abrupt sudden onset," a red flag for brain bleed, or recording a plan to order tests that the patient explicitly declined (Fox, 2026).

The root cause lies in both the transcription and generation layers of the AI pipeline. Fox suggests that current evaluation systems are inadequate and calls for better detection of these quiet but dangerous failures across high-stakes AI domains (Fox, 2026).

- AI clinical notes can be dangerously incomplete: critical symptoms like jaw pain may be omitted, leading to misdiagnosis and missed emergencies.
- Hallucinations are frequent, with 1 in 10 notes containing fabricated information (e.g., nonexistent diagnoses, medications, or hospitals).
- Large real-world studies show 1 in 20 notes have serious errors, but no incident reporting exists to catch them in practice.
- Automated checks catch only a small fraction of errors; high-severity omissions and wrong plans often go undetected.
- Failures originate from both transcription (e.g., misinterpreting 'just happened' as 'abrupt onset') and generation (e.g., keeping an outdated plan).