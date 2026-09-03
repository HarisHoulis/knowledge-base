# Implementer Findings Ledger

The append-only record of code-review findings on implemented tickets — the aggregation surface for evaluating implementer performance. One compact row per ticket. Full findings text lives in the originating ticket's issue comment and the code-review output, never here.

Roll rows into a dated archive (`.archive/` or a dated section) once the table passes ~50 rows.

## Severity rubric

| Severity | Threshold |
| --- | --- |
| **blocker** | A finding whose fix requires a decision the ticket didn't cover and the Pre-flight didn't list as an assumption (root-cause `unstated decision`); an out-of-bounds edit; a wrong-seam implementation; a missing requirement the ticket explicitly asked for. |
| **major** | A defect or scope creep that is objectively wrong against the ticket or spec, but fixable within the ticket's bounds and assumptions — a broken behavior, a bypassed seam, a missing-but-recoverable requirement. |
| **minor** | A judgement call: a Fowler smell, a disputed style point, or a partial requirement whose intent is ambiguous and was reasonably inferred. |

Every finding is graded blocker/major/minor; nothing is left ungraded.

## Categories

A finding's category is its review axis:

- **Spec types** — (a) missing/partial requirement, (b) scope creep, (c) wrong implementation, (d) bypassed seam / polluted layer, (e) temp mock left in prod, (f) hallucinated or tautological test, (g) architectural regression, (h) requirement drift, (i) unstated decision needed.
- **Standards (Fowler smells)** — Mysterious Name, Duplicated Code, Feature Envy, Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man, Refused Bequest.

A documented-standard breach is a category of its own ("doc-standard") when no smell name fits.

## Root-cause taxonomy

Each finding is attributed to one class — the fix's root cause, not the surface symptom:

| Class | Meaning |
| --- | --- |
| **spec gap** | The ticket/spec didn't specify the behavior, so the implementer inferred it. |
| **seam gap** | The ticket didn't name a seam, or the implementer worked at the wrong one. |
| **bounding-box gap** | The ticket's bounds didn't contain the edit — the implementer touched something outside them. |
| **unstated decision** | The fix needs a decision the ticket didn't cover and the Pre-flight didn't list as an assumption. |

## Ledger

| # | Date | Signals | Categories | Severity | Root causes | Link |
| --- | --- | --- | --- | --- | --- | --- |
| 63 | 2026-08-23 | ✓ Preflight | ✓ seam | ✓ bounds | 3 asm | 0 esc | unstated-decision ×3, duplicated-code ×1, ambiguous-req ×1 | 5 minor / 0 major / 0 blocker | spec-gap ×2, seam-gap ×1, unstated-decision ×1 | [#179](https://github.com/HarisHoulis/knowledge-base/pull/179) |
| 170 | 2026-08-23 | ✓ Preflight | ✓ seam | ✓ bounds | 0 asm | 0 esc | spec-gap ×1, unstated-decision ×1, doc-standard ×1 | 3 minor / 0 major / 0 blocker | spec-gap ×2, unstated-decision ×1 | [#177](https://github.com/HarisHoulis/knowledge-base/pull/177) |
| 171 | 2026-08-23 | ✓ Preflight | ✓ seam | ✓ bounds | 0 asm | 0 esc | duplicated-code ×1 | 1 minor / 0 major / 0 blocker | spec-gap ×1 | [#171](https://github.com/HarisHoulis/knowledge-base/issues/171) |
| 172 | 2026-08-24 | ✓ Preflight | ✓ seam | ✓ bounds | 0 asm | 0 esc | duplicated-code ×2, requirement-drift ×1 | 3 minor / 0 major / 0 blocker | spec-gap ×3 | pending |
| 229 | 2026-09-03 | ✓ Preflight | ✓ seam | ✓ bounds | 3 asm | 0 esc | primitive-obsession ×1, spec-gap ×1, judgement-call ×1, unstated-decision ×1, requirement-drift ×1, tautological-test ×1 | 6 minor / 0 major / 0 blocker | unstated-decision ×2, bounding-box-gap ×3, spec-gap ×1 | [#243](https://github.com/HarisHoulis/knowledge-base/pull/243) |
| 249 | 2026-09-03 | ✓ Preflight | ✓ seam | ✓ bounds | 4 asm | 0 esc | overclaim ×2, analysis-tension ×1, table-clarity ×1, evidence-mismatch ×1, verification-gap ×1 | 6 minor / 0 major / 0 blocker | spec-gap ×3, bounding-box-gap ×1, unstated-decision ×1, seam-gap ×1 | [#249](https://github.com/HarisHoulis/knowledge-base/issues/249) |

**Signals** columns, per ticket: Pre-flight present (✓/✗), seam named (✓/✗), bounds stated (✓/✗), # assumptions, # escalations.
