# Agentic Acceptance Criteria — Best Practices

Question: what ticket/AC format minimizes misinterpretation by an autonomous coding agent?

## Findings

### 1. How benchmark formats specify work

- SWE-bench instances: `instance_id`, `problem_statement`, `repo`, `base_commit`, `patch`, `test_patch`, `FAIL_TO_PASS`, `PASS_TO_PASS`, `hints_text`. Acceptance is **test-typed**: FAIL_TO_PASS tests prove the behavior, PASS_TO_PASS tests bound scope ("must not break existing functionality"). Tests are hidden from the agent.
- OpenAI SWE-bench Verified (openai.com/index/introducing-swe-bench-verified/) — hiding tests is a design flaw: 38.3% of problem statements were "underspecified", 68.3% of instances filtered as unfair/unsolvable. Published annotation rubric grades problem-statement clarity 0-3 and test validity 0-3.
- Ambig-SWE (arXiv 2502.13069, ICLR 2026) — models "making unwarranted assumptions to compensate for missing information"; interaction recovers up to 74% performance.

**Lesson**: unambiguous = clear problem statement + behavior-typed tests that exactly mirror it.

### 2. Practitioner guidance for writing for agents

- Anthropic Claude Code best practices: "Give Claude a way to verify its work" (test/build/lint); "Explore first, then plan, then code"; "The most useful specs are self-contained: they name the files and interfaces involved, state what is out of scope, and end with an end-to-end verification step." https://code.claude.com/docs/en/best-practices
- AGENTS.md conventions: specific/concise rules, concrete-verifiable phrasing, "README for agents". https://code.claude.com/docs/en/memory
- Devin *Coding Agents 101*: "Say how you want things done, not just what", "Tell the agent where to start", give access to CI/tests/types/linters, checkpoints. https://devin.ai/agents101

**No source recommends Given/When/Then**. Test-first ("give the agent a failing test") is the recommended AC style.

### 3. Explicit negatives / scope boundaries

- No rigorous experimental study isolates "must NOT do X" — evidence gap.
- OpenAI prompt guide puts "what should the model never do?" inside its recommended Instructions section.
- SlopCodeBench (arXiv 2603.24755) — explicit quality guidance reduces initial verbosity/erosion by up to a third.
- PASS_TO_PASS tests are effectively machine-enforced negatives (SWE-bench).
- Weak phrasing warning: classic prompting guidance says specify the replacement action, not just the prohibition.

**Recommendation**: positives + a short "never do" list, worded with the replacement action.

### 4. Seam / bounding box

- Anthropic: "Scope the task. Specify which file, what scenario, and testing preferences" — file-level seams yes.
- Devin 101: "Tell the agent where to start" (repo, relevant modules, example patterns).
- GitHub Copilot cloud agent: bounds box at platform level (one repo, one branch, one PR, 59-min cap). https://gh.io/coding-agent-docs
- Counter-evidence: SlopCodeBench criticizes benchmarks that "heavily constrain an agent's design decision space" and recommends specs that "demand architectural decisions but leave internal structure to the agent."

**Synthesis**: specify the seam and the behavior; leave internal implementation free.

### 5. Published ticket templates

No canonical template with all requested fields exists. Closest:
- Anthropic self-contained spec (files/interfaces, out-of-scope, verification step)
- Devin pre-task checklist (explicit success criteria, context/patterns, size XS-L, checkpoints)
- SWE-bench instance schema

The bounding-box/allow-list/size-cap vocabulary is a practitioner convention, unstandardized externally. Present locally in this repo (`docs/agents/agentic-execution.md`).

## Design implication

ACs should be behavior-typed, name the seam, name the verification (test seam), carry a short explicit negatives list, and leave internal implementation free. Add a "how verified" pointer per AC.
