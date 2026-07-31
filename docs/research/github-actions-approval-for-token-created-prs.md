# Making CI Run Automatically on PRs Created by Workflows (GITHUB_TOKEN)

## Short Answer

**A `pull_request`-triggered workflow run lands in an "approval-required" state whenever the PR was created or updated by a workflow using `GITHUB_TOKEN`** — regardless of fork status or whether the PR touches `.github/workflows/`. The only documented way to have such runs execute without manual approval is to **author the PR with a personal access token (PAT) or a GitHub App installation access token instead of `GITHUB_TOKEN`**. GitHub's docs say this verbatim:

> "If you need workflow runs from workflow-created pull requests to execute without requiring approval, use a GitHub App installation access token or a personal access token instead of `GITHUB_TOKEN` when creating or updating the pull request."

- Source: https://docs.github.com/en/actions/concepts/security/github_token

---

## 1. The Mechanism

The `GITHUB_TOKEN` is itself a GitHub App installation token:

> "When you enable GitHub Actions, GitHub installs a GitHub App on your repository. The `GITHUB_TOKEN` secret is a GitHub App installation access token. You can use the installation access token to authenticate on behalf of the GitHub App installed on your repository."

- Source: https://docs.github.com/en/actions/concepts/security/github_token

Events triggered by `GITHUB_TOKEN` are normally suppressed, with an explicit exception for `pull_request` runs created via workflow-created PRs — and those runs require approval:

> "When you use the repository's `GITHUB_TOKEN` to perform tasks, events triggered by the `GITHUB_TOKEN` will not create a new workflow run, with the following exceptions: ... `pull_request` events with the `opened`, `synchronize`, or `reopened` activity types: when a workflow using `GITHUB_TOKEN` creates or updates a pull request, the resulting `pull_request` event creates workflow runs in an **approval-required** state. The pull request displays a banner in the merge box, and a user with write access to the repository can start the runs by selecting **Approve workflows to run**..."

- Source: https://docs.github.com/en/actions/concepts/security/github_token

The events reference repeats the rule:

> "When a pull request is created or updated by a workflow using `GITHUB_TOKEN`, `pull_request` events with the `opened`, `synchronize`, or `reopened` activity types create workflow runs that require approval. A user with write access to the repository can approve these runs from the pull request page. With the exception of `workflow_dispatch` and `repository_dispatch`, other `GITHUB_TOKEN`-triggered events do not create workflow runs at all."

- Source: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request

So the gate is keyed on **the token used to author the PR**, not on fork status and not on whether `.github/workflows/` files changed. This matches the observed case: a same-repo PR authored by `app/github-actions` (no workflow-file changes) still required approval, while a PR authored by the repo owner ran with zero delay.

## 2. A Separate, Configurable Contributor Gate

Independent of the rule above, public repos have a configurable contributor-approval policy. It does **not** bypass the `GITHUB_TOKEN`-created-PR rule:

> "workflows on pull requests to public repositories from some outside contributors will not run automatically, and might need to be approved first. Depending on the 'Approval for running fork pull request workflows from contributors' setting, workflows on pull requests to public repositories will not run automatically and may need approval if: The pull request is **created by** a user that requires approvals based on the selected policy. The pull request event is **triggered by** a user that requires approvals based on the selected policy. By default, all first-time contributors require approval to run workflows."

- Source: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#controlling-changes-from-forks-to-workflows-in-public-repositories

Both the PR author and the triggering actor are evaluated against the policy levels ("Require approval for first-time contributors who are new to GitHub", "Require approval for first-time contributors", "Require approval for all external contributors").

Runs awaiting approval are auto-deleted after 30 days:

> "Workflow runs that have been awaiting approval for more than 30 days are automatically deleted."

- Source: https://docs.github.com/en/actions/managing-workflow-runs/approving-workflow-runs-from-public-forks

## 3. Options to Run Without Manual Approval

### Option A — Author the PR with a PAT owned by a write-access user (chosen here)

Sanctioned directly by the docs quote in the Short Answer. The PR is authored as the PAT owner (a human with write access), so the `GITHUB_TOKEN`-created-PR rule cannot fire. Trade-offs:

- The PAT is a long-lived credential stored as a repo secret: "Any user with write access to your repository has read access to all secrets configured in your repository." — https://docs.github.com/en/actions/reference/security/secure-use
- If the PAT owner has never had a commit/PR merged (or is "external"), the contributor policy in Section 2 can still apply.

PAT usage is also documented as the general alternative to `GITHUB_TOKEN`:

> "If you need a token that requires permissions that aren't available in the `GITHUB_TOKEN`, create a GitHub App and generate an installation access token within your workflow... Alternatively, you can create a personal access token, store it as a secret in your repository, and use the token in your workflow with the `${{ secrets.SECRET_NAME }}` syntax."

- Source: https://docs.github.com/en/actions/tutorials/authenticate-with-github_token

### Option B — Author the PR with a GitHub App installation token

Also explicitly sanctioned by the same note ("use a GitHub App installation access token ... instead of `GITHUB_TOKEN`"). Short-lived tokens, least-privilege via app permissions, but the app bot is a "first-time contributor" until its PRs merge, so the Section 2 policy can still gate it. Highest setup cost.

### Option C — `pull_request_target`

Runs in the context of the base branch and always runs regardless of approval settings:

> "Workflows triggered by `pull_request_target` events are run in the context of the base branch. Since the base branch is considered trusted, workflows triggered by these events will always run, regardless of approval settings."

- Source: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#controlling-changes-from-forks-to-workflows-in-public-repositories

Security risk is documented and severe:

> "Running untrusted code on the `pull_request_target` trigger may lead to security vulnerabilities. These vulnerabilities include cache poisoning and granting unintended access to write privileges or secrets."

- Source: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request_target

### Option D — `workflow_run` / `workflow_dispatch` / `repository_dispatch` chaining

These are not `pull_request` events, so the PR-approval rule never applies. `workflow_dispatch` and `repository_dispatch` are the only events `GITHUB_TOKEN` can always trigger. Costs: extra plumbing, must relay the PR number to the CI job, and `workflow_run` cannot chain more than three levels.

### Option E — Repo approval settings

The "Fork pull request workflows" settings (private repos) and the public-repo contributor policy tune the Section 2 gate only; they **cannot** bypass the `GITHUB_TOKEN`-created-PR approval rule.

## 4. Check Run Names vs. Ruleset Required-Status-Check Contexts

Separate issue, commonly conflated: a required status check that never appears shows as a perpetual pending "Waiting for status to be reported."

- The check run name defaults to the job ID: "Use `jobs.<job_id>` to give your job a unique identifier." — https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_id
- `jobs.<job_id>.name` overrides the displayed check name: "Use `jobs.<job_id>.name` to set a name for the job, which is displayed in the GitHub UI." — https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idname
- The workflow-level `name:` is only the Actions-tab display name and does not become the check run name: "The name of the workflow. GitHub displays the names of your workflows under your repository's 'Actions' tab." — https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#name
- Ruleset `required_status_checks` contexts match the check/status **name** exactly: "The status check context name that must be present on the commit." — https://docs.github.com/en/rest/repos/rules?apiVersion=2022-11-28
- "If a check and a commit status have the same name, both must pass when that name is required." — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/troubleshooting-required-status-checks
- "GitHub Actions generates checks, not commit statuses, when workflows are run." — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks
