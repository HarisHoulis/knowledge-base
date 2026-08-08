---
domain: engineering-culture
subdomain: github-actions
concept: fan-in-single-required-check
title: Fan-in to a single required GitHub Action
sources:
  - title: "Fan-in to a single required GitHub Action"
    url: "https://jakewharton.com/fan-in-to-a-single-required-github-action/"
    author: "Jake Wharton"
---

# Fan-in to a single required GitHub Action

GitHub Actions projects often spawn multiple jobs, and each job must be marked as required in branch protection to prevent failing PRs from merging. A common pattern is to create a final job that lists all other jobs as dependencies (using `needs`) and mark that final job as the single required check. However, this naive approach fails because GitHub skips the final job if any dependency job fails, and skipped jobs are reported as "Success", thus not blocking PRs [GitHub docs on conditions](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/using-conditions-to-control-job-execution).

To work around this, the final job must be forced to run even when dependencies fail by setting `if: ${{ !cancelled() }}`. Then, a step inside the final job checks the `needs.*.result` values to ensure none are `failure` or `cancelled`, using `toJSON` and `grep`. This makes the final job accurately reflect the overall status, and it can be safely designated as the single required check. The article provides a concrete example from the Mosaic repository [JakeWharton/mosaic workflow](https://github.com/JakeWharton/mosaic/blob/54f2183bf8757fe941433c824771272e20d35673/.github/workflows/build.yaml#L299-L321).

An alternative strategy is to create a final job that only runs when any dependency fails and then fails itself, as [posted in the Actions issue tracker](https://github.com/actions/runner/issues/2566#issuecomment-1523814835). This simpler approach works but precludes adding additional steps or downstream jobs to the final status job.

- Naively using a final job with `needs` does not work because skipped jobs count as success, allowing failed PRs to merge.
- Set `if: ${{ !cancelled() }}` on the final job so it always runs unless the entire workflow is cancelled.
- Check `needs.*.result` inside the final job using `toJSON` and `grep` to detect any failure or cancellation.
- Mark the final job as the only required check, and it can also gate downstream jobs like publishing.
- An alternative pattern is to fail the final job only when dependencies fail, but this prevents adding extra steps/jobs.