# Agent Ambiguity Handling — Stop-and-Ask vs Record-and-Proceed

Question: what should an autonomous coding agent do when a ticket is under-specified?

## Findings

### 1. What vendors and benchmarks say

- SWE-bench definitionally excludes ambiguity: success is test-based only, design ambiguity never adjudicated. https://arxiv.org/abs/2310.06770
- Anthropic *Building Effective Agents* explicitly endorses asking: "Agents begin with a command from, or interactive discussion with, the human user... potentially returning to the human for further information or judgement." https://www.anthropic.com/engineering/building-effective-agents
- Claude Code best practices: for larger features, "have Claude interview you using the `AskUserQuestion` tool... then write a complete spec to SPEC.md" before coding; mandatory explore → plan → code sequence. https://www.anthropic.com/engineering/claude-code-best-practices
- Ambig-SWE (ICLR 2026, arXiv 2502.13069) — the decisive evidence: models can't reliably *detect* underspecification, but interaction recovers up to **74%** over non-interactive baselines on an underspecified SWE-bench variant.

### 2. Ask vs assume in the literature

- Ambig-SWE: "Making unwarranted assumptions... and failing to ask clarifying questions can lead to suboptimal outcomes, safety risks due to tool misuse, and wasted computational resources."
- "Ask or Assume?" (arXiv 2603.26233) — uncertainty-aware scaffold detects underspecification *before* coding, achieves 69.4% resolve rate vs a standard single agent, calibrated to conserve questions on easy tasks.
- HumanEvalComm (TOSEM 2025, arXiv 2406.00215) — senior engineers ask clarifying questions; LLMs should too.
- SpecBench/Buddy (arXiv 2606.20585) — the two failure extremes: entering implementation mode while overestimating understanding, vs exhausting the question budget on every choice.
- Assumption-recording: no controlled study measures "assumption log → debuggability" directly. Reflexion (arXiv 2303.11366) supports verbalized reflection stored in memory. Caveat: Huang et al. (arXiv 2310.01798) — intrinsic self-correction without *external* feedback is unreliable; recorded assumptions only pay off when paired with an external review loop (tests, reviewer, human).

### 3. AFK / CI failure path

- Claude Code headless (`claude -p`): in `dontAsk` mode `AskUserQuestion` is **denied outright** — the agent physically cannot ask; exit codes support fail-fast branching. https://code.claude.com/docs/en/headless
- Claude Code GitHub Action: interactive mode (@claude on issue/PR — async human-in-the-loop, replies in-thread) vs automation mode (unattended, results to workflow logs). Docs recommend issue templates and `--max-turns` caps. https://code.claude.com/docs/en/github-actions
- OpenHands headless: always `always-approve`, no ask channel; callers parse JSONL events for success/failure. https://docs.openhands.dev/openhands/usage/cli/headless

**Documented pattern**: human answerable → route questions to the issue/PR thread; not → pre-resolve via templates/CLAUDE.md and fail fast with structured output + non-zero exit. The needs-info-label escalation is not prescribed by any vendor doc — open design space (our triage skill already implements it).

### 4. Pre-flight assumptions artifact

- Anthropic: "Prioritize transparency by explicitly showing the agent's planning steps"; plan mode + interview → SPEC.md before implementation; "time spent making the spec precise pays off more than time spent watching the implementation."
- Jules (Google) makes planning a hard gate: develops a plan you approve before it edits. https://jules.google
- OpenHands' plan → implement → validate architecture and its headless JSONL event stream provide the same seam.

**No tool mandates an "Assumptions" section in PRs** — open design space; closest primitives are plan-gated execution and `AskUserQuestion`.

## Design implication

The detection step is where models fail — the `/implement` skill should require an explicit pre-flight ambiguity check rather than defaulting to silent inference. Ask when a human is reachable (HITL), else record assumptions visibly and proceed; AFK, fail fast with a `needs-info` escalation.
