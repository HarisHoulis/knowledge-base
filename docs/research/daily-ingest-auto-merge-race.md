# Why the Daily Ingest PR #228 was not auto-merged

## Short Answer

**PR #228 was left open because the auto-merge enable step raced GitHub's index and lost.** `scripts/daily-ingest.sh` enables squash auto-merge by running `gh pr merge --auto --squash` with **no PR selector**, so `gh` resolves the PR implicitly by querying GitHub GraphQL for pull requests whose `headRefName` matches the current branch (`daily-ingest/2026-08-30`). That lookup ran ~7 ms after `gh pr create` returned, and GitHub's index had not yet caught up — the query returned zero PRs, `gh` failed with `no pull requests found for branch "daily-ingest/2026-08-30"`, and the script's best-effort `if !` guard swallowed the failure. The PR stayed open until a human merged it manually.

## 1. The failure in the run log

Daily Ingest run [33339910922](https://github.com/HarisHoulis/knowledge-base/actions/runs/33339910922) (2026-08-30):

```
23:40:19.227  https://github.com/HarisHoulis/knowledge-base/pull/228     <- gh pr create returns
23:40:19.234  [daily-ingest] Enabling squash auto-merge...
23:40:19.990  no pull requests found for branch "daily-ingest/2026-08-30"  <- gh pr merge fails
23:40:19.992  [daily-ingest] Warning: failed to enable auto-merge (best-effort).
```

Compare the successful run [33279128383](https://github.com/HarisHoulis/knowledge-base/actions/runs/33279128383) that produced PR #224 — the identical ~7 ms gap, but the lookup found the PR:

```
23:35:08.124  https://github.com/HarisHoulis/knowledge-base/pull/224     <- gh pr create returns
23:35:08.131  [daily-ingest] Enabling squash auto-merge...
23:35:10.015  [daily-ingest] Done.                                        <- no lookup error; auto-merge enabled
```

(`Done.` at `daily-ingest.sh:94` prints unconditionally, so the success signal here is the **absence** of a `no pull requests found` line — confirmed by the `auto_squash_enabled` timeline event below, not by the `Done.` echo itself.)

The PR timelines confirm the outcome: #214, #217, #219, #221, #224 each carry an `auto_squash_enabled` event; #228 does not, and its merge is recorded as a manual `merged` event by HarisHoulis ~4.7 h after creation.

## 2. The mechanism

`gh pr merge --auto --squash` with no selector argument resolves the PR by branch:

- It reads the current branch (`daily-ingest/2026-08-30`) and runs a GraphQL query (`PullRequestForBranch`) that fetches `repository.pullRequests(headRefName: ...)`.
- If the result is empty, `gh` returns `NotFoundError: no pull requests found for branch "daily-ingest/2026-08-30"` and exits non-zero.
- The `if ! $GH pr merge --auto --squash` guard in `scripts/daily-ingest.sh:89` treats any failure as best-effort: it logs `Warning: failed to enable auto-merge` and continues, per ADR-0006.

GitHub does not guarantee that a just-created PR is immediately findable by the head-branch index; the lookup is eventually consistent. The direct evidence is the two runs themselves: the same script, branch naming, and ~7 ms timing produced opposite outcomes, so the query's freshness at that instant is nondeterministic — #224 won the race, #228 lost it. There is no deterministic difference between the two runs; a retry a second later would have found #228.

## 3. Fix recommendation

Pass the PR number to `gh pr merge` explicitly instead of relying on the implicit branch lookup, e.g.:

```bash
PR_URL=$($GH pr create --fill --base main)
PR_NUMBER=${PR_URL##*/}
...
$GH pr merge "$PR_NUMBER" --auto --squash
```

A selector argument bypasses the branch query entirely (gh fetches the PR by number), removing the eventual-consistency window. Alternatively, add a short retry loop around the existing call. The research ticket is scoped to explaining #228; the fix itself is tracked separately.
