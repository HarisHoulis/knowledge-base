# Architectural Rules (Constraints)

Architectural rules are **constraints**: decisions that are hard to reverse and affect the system as a whole. Each rule carries its rationale — why it exists, not just how to apply it (Second Law: why > how).

1. **Modularisation** — Treat high cohesion and low coupling as first-class structural concerns; keep modules separated and recombined cleanly.
   - *Rationale:* Modularity is the fundamental structural characteristic (Ch. 1); every other characteristic — testability, extensibility, maintainability — is easier to preserve when modules can be understood, tested, and replaced in isolation.

2. **Extensibility over implementation** — Design seams that absorb change without rewrite; add new behaviour without altering existing behaviour.
   - *Rationale:* Behaviour coupled to a single implementation path requires a rewrite for each new variant; extension seams localise change and keep stable code untouched.

3. **Expose only what's needed** — At module/package boundaries, expose the minimum surface; make dependency direction explicit; encapsulate internals with no leakage.
   - *Rationale:* A wide public surface binds consumers to internals, so internal refactors ripple across the system; explicit dependency direction keeps the graph acyclic and comprehensible.

4. **Trade-off awareness** (First Law) — Every choice states what it gives up; a cost-free decision means the trade-off is unfound.
   - *Rationale:* All architecture is a series of trade-offs (First Law); an unstated trade-off surfaces later as surprise rework, whereas an explicit trade-off is a reviewed decision.

5. **Why over how** (Second Law) — Every rule carries its rationale; future readers know why it exists.
   - *Rationale:* "Why" is harder to reconstruct than "how" (Second Law); a rule without its reason reads as dogma and is discarded at the first inconvenience.

6. **Guidance, not prescription** — Rules steer toward the right choice rather than dictate the specific tool, unless a technology is required to preserve a characteristic.
   - *Rationale:* Prescribing tools goes stale as the ecosystem moves and forces needless migrations; steering rules survive change while still preserving required characteristics.

7. **Right-size decisions** (Ch. 19) — Avoid overly broad, unused, or imprecise rules; an unenforceable rule is worse than none.
   - *Rationale:* Rules that cover everything cover nothing; precise, scoped rules are the ones a reader can apply and a reviewer can enforce.

8. **Compliance / fitness functions** (Ch. 6) — Make rules mechanically checkable where possible (lint, tests, CI); unenforced decisions cause structural decay.
   - *Rationale:* Unenforced decisions decay quietly (Ch. 6); a fitness function turns a rule from an aspiration into a verified invariant.

9. **Variance process** — Exceptions to a rule are explicit and justified, never silent.
   - *Rationale:* Silent violations accumulate until the rule is meaningless; an explicit, justified exception is a documented decision that future readers can reconsider.
