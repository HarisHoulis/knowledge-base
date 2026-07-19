# State Persistence for GitHub Actions Pipeline

## Recommendation

**Use `actions/cache` (Option 2).** It is the simplest correct solution for a single-user cron-style pipeline on ephemeral runners. The state file is tiny (~1 KB of SHA256 hashes), the 7-day eviction window is irrelevant at daily cadence, and the cross-branch cache scope rules don't apply to a default-branch-only workflow. If cache eviction ever becomes a problem (e.g., the pipeline runs less than once a week), fall back to **Option 1 (commit to repo)** — both changes are small and non-breaking. Avoid Option 3 (git-log scan) — it is needlessly expensive — and Option 4 (self-hosted runner) — it defeats the purpose of serverless CI.

---

## Option 1: Commit `state.json` to the repo

Store `state.json` inside the repository (e.g., `state.json` at repo root or `kb_pipeline/state.json`). The pipeline reads from and writes to the checked-out copy. The workflow commits the updated `state.json` alongside any new concept files.

### Pros
- **No external infra.** The state lives in the repo, travels with it, survives fork/copy.
- **Observable.** Anyone can inspect processed hashes in a `git blame` or `git log`.
- **No eviction risk.** State persists as long as the repo exists.

### Cons
- **Race on concurrent runs.** If two workflow runs overlap, both write `state.json` and the last commit wins, losing hashes from the first. For a single-user cron pipeline on a personal repo this is unlikely (< 1 min run time, hourly schedule minimum).
- **Dirty state in mid-run.** The pipeline writes hashes to `state.json` _after_ processing entries (`pipeline.py:196`). If the workflow crashes between the write and the `git commit`, those hashes are gone. Next run re-processes them — wasted tokens, no data loss.
- **Git history bloat.** A commit per run with a 1 KB JSON file is negligible but adds noise to `git log`.
- **Design reversal.** `CONTEXT.md:28` explicitly states state is "stored outside the KB tree." Committing it to the repo contradicts this boundary.

### Merge Conflict Analysis
- The file is append-only (new hashes are added, none removed). Real merge conflicts require divergent edits on the same lines — possible only if two runs modify `state.json` concurrently before either commits. On a single-user repo with a serialized scheduler, this is effectively impossible.

---

## Option 2: GitHub Actions Cache (`actions/cache`)

Use `actions/cache@v4` (or `v6`) to save `~/.kb-pipeline/state.json` after each run and restore it at the start of the next.

### Workflow Snippet (Illustrative)

```yaml
- name: Restore pipeline state
  id: cache-state
  uses: actions/cache@v4
  with:
    path: ~/.kb-pipeline/state.json
    key: kb-state-v1

- name: Run pipeline
  run: python -m kb_pipeline

- name: Save pipeline state
  if: always()
  uses: actions/cache/save@v4
  with:
    path: ~/.kb-pipeline/state.json
    key: kb-state-v1
```

### Pros
- **Zero git history impact.** State is ephemeral — no commits, no noise.
- **Preserves existing code.** `config.py` already reads `KB_STATE` (defaults to `~/.kb-pipeline/state.json`). No pipeline changes needed — only a workflow file.
- **Correct for the constraint.** Ephemeral runners _should_ use ephemeral caches when possible.

### Cons
- **7-day eviction (default).** `actions/cache` removes entries not accessed in 7 days ([GitHub docs](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#usage-limits-and-eviction-policy)). At daily cadence this is fine. At weekly+ cadence the cache is evicted and the next run starts cold (re-processes everything).
- **10 GB per-repo limit.** Irrelevant for a 1 KB state file, but worth noting.
- **Cross-branch scope.** Cache can only be restored from the same branch or the default branch ([GitHub docs — Restrictions](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#restrictions-for-accessing-a-cache)). For a single-branch pipeline this is not a limitation.
- **Cache miss on first run or key change.** Cold start re-processes all sources once. The pipeline handles this correctly (empty `processed_hashes` → processes everything).
- **Only usable within GitHub Actions.** Unlike a committed file, the cache is invisible outside Actions. Scripts run locally (`python -m kb_pipeline`) need their own `~/.kb-pipeline/state.json`.

### Eviction & Miss Detail
- Eviction is LRU (least recently accessed) per-repo. If the pipeline runs daily, the cache is accessed daily and never evicted.
- On cache miss: the restore step silently succeeds with no output — `cache-hit` is empty. The pipeline loads an empty state and processes every source entry.
- Cache keys are strings ≤ 512 chars. Use a static key (`kb-state-v1`) — no `hashFiles` needed because state is the cache payload, not a dependency fingerprint.

---

## Option 3: Repo Git Log as State

Remove `state.json` entirely. At pipeline start, scan `concepts/` (and optionally `drafts/`) for committed source URLs, hash them, and use that set for dedup.

### Implementation Approach

```python
# Hypothetical — replaces load_state()
import subprocess, re, hashlib

def load_state_from_git():
    result = subprocess.run(
        ["git", "grep", "--no-index", "-h", "^  url:", "concepts/", "drafts/"],
        capture_output=True, text=True, check=False, cwd=KB_PATH,
    )
    urls = re.findall(r'url:\s*"(.+)"', result.stdout)
    return {"processed_hashes": [hashlib.sha256(u.encode()).hexdigest()[:16] for u in urls]}
```

### Pros
- **No state file to manage.** State is derived from the KB tree — truly "no extra state."
- **Survives anything.** A fresh checkout has full history — no cache misses, no file to lose.
- **Consistent across environments.** Works on any machine with a `git` checkout.

### Cons
- **Performance.** `git grep` on a repo grows linearly with the number of concept files. For <300 files this is fast (~100 ms). For 10,000+ files it becomes slow (~2-5 s). Reading a JSON file is O(1) (~1 ms). See benchmark below.
- **Drafts ambiguity.** URLs in `drafts/` represent in-progress work that may never be promoted. If the pipeline crashes mid-run, draft URLs _should_ be considered processed (so they aren't re-generated). If they aren't in `concepts/`, they'd be reprocessed. The current state file captures all URLs attempted, not just successfully committed ones.
- **No offline/recovery safety net.** If the last commit was a bad merge that dropped some concept files, the next run re-processes those URLs — no backstop.
- **Couples pipeline to git.** Currently `load_state()` is a JSON read; this change adds a hard `git` dependency at import time.

### Performance Benchmark (Estimated)

| Method | Latency (300 files) | Latency (10,000 files) | Complexity |
|---|---|---|---|
| `json.loads(state_path.read_text())` | ~1 ms | ~1 ms | O(1) |
| `git grep` all concept files | ~80-120 ms | ~2-5 s | O(n) |
| `git log --all --diff-filter=A` + parse | ~200-400 ms | ~10-30 s | O(n × commits) |

_Estimates based on typical macOS/Linux ext4/APFS performance. The relative cost difference (1 ms vs 100+ ms) is negligible for a pipeline whose bottleneck is LLM API calls (~2-10 s per entry)._

---

## Option 4: Persistent Self-Hosted Runner

Run the pipeline on a machine with a persistent filesystem — either a self-hosted GitHub Actions runner or a separate cron/launchd process that bypasses Actions entirely.

### Pros

- **Full filesystem control.** Persistent `~/.kb-pipeline/state.json`. No cache eviction, no cold starts.
- **No cache-scope or key-management overhead.**
- **Can run on the same machine** that already has credentials, Python environment, etc.

### Cons

- **Operational overhead.** Must maintain a host (VM, Raspberry Pi, old laptop). Patch it. Monitor uptime.
- **Defeats serverless CI.** The whole point of Actions is ephemeral, zero-maintenance runners. Adding a persistent host reintroduces maintenance cost.
- **Not portable.** Ties the pipeline to a specific machine. Moving to a new machine requires setup.
- **No free tier nuance.** Self-hosted runners are free, but the _maintenance_ cost (time, not money) is real.

---

## Summary Matrix

| Criterion | Option 1: Commit | Option 2: Cache | Option 3: Git Log | Option 4: Self-Hosted |
|---|---|---|---|---|
| Code changes needed | STATE_PATH + workflow | Workflow only | load_state() rewrite | None |
| Survives fresh checkout | ✅ | ❌ (cold start) | ✅ | ❌ (different host) |
| 7-day gap safe | ✅ | ❌ (evicted) | ✅ | ✅ |
| Consistent local + CI | ✅ | ❌ (CI-only) | ✅ | N/A |
| Git history pollution | ❌ (minor) | ✅ | ✅ | ✅ |
| Merge conflict risk | ✅ (none) | ✅ | ✅ | ✅ |
| Ops cost | Zero | Zero | Zero | Real |
| Supports drafts correctly | ✅ | ✅ | ⚠️ (partial) | ✅ |
