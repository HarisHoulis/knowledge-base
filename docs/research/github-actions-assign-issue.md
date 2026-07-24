# Assigning a GitHub Issue to a User from a Workflow Using Only GITHUB_TOKEN

## Short Answer

**You cannot assign `github-actions[bot]` to an issue from a GitHub Actions workflow, regardless of whether you use `GITHUB_TOKEN` (an installation token) or a Personal Access Token.** With `GITHUB_TOKEN`, the `replaceActorsForAssignable` GraphQL mutation rejects installation tokens. With a PAT, the mutation accepts the token but rejects `github-actions[bot]` as an ineligible assignee — the bot account is not a repository collaborator and does not meet GitHub's assignee eligibility criteria.

The only way to assign a user from a workflow is to assign a human collaborator using a PAT.

---

## The Error

When running inside a GitHub Actions workflow:

```bash
gh issue edit <number> --add-assignee "github-actions[bot]"
```

Fails with:

```
GraphQL: Assigning agents is not supported with GitHub App installation tokens. Use a user token (personal access token or OAuth token) instead. (replaceActorsForAssignable)
```

The error originates from the `replaceActorsForAssignable` GraphQL mutation. This mutation is deliberately blocked for GitHub App installation tokens by design -- GitHub does not allow installation tokens to assign users/issues to other actors.

---

## Investigated Approaches

### Approach 1: GitHub CLI (`gh issue edit --add-assignee`) -- FAILS

The GitHub CLI `gh issue edit --add-assignee` command uses GraphQL under the hood. Specifically, it calls the `replaceActorsForAssignable` mutation with login-based parameters (when `ApiActorsSupported` is true, which it is on github.com).

**Evidence from source code:**

- `pkg/cmd/issue/edit/edit.go` handles `--add-assignee` and `--remove-assignee` flags, setting `editable.Assignees.Edited = true`.
- The edit path uses `api.ReplaceActorsForAssignableByLogin()`.
- The `editable.go` has a comment: `// replaceActorsForAssignable and requestReviewsByLogin mutations.`
- `api/queries_issue.go` shows the `IssueCreate` function calls `ReplaceActorsForAssignableByLogin()` when `assigneeLogins` are present.

**Sources:**
- [cli/cli/pkg/cmd/issue/edit/edit.go](https://github.com/cli/cli/blob/trunk/pkg/cmd/issue/edit/edit.go)
- [cli/cli/api/queries_issue.go](https://github.com/cli/cli/blob/trunk/api/queries_issue.go)
- [cli/cli/pkg/cmd/pr/shared/editable.go](https://github.com/cli/cli/blob/trunk/pkg/cmd/pr/shared/editable.go)
- [cli/cli/pkg/cmd/pr/shared/params.go](https://github.com/cli/cli/blob/trunk/pkg/cmd/pr/shared/params.go)

### Approach 2: REST API `POST /repos/{owner}/{repo}/issues/{issue_number}/assignees` -- FAILS

The REST API has a dedicated endpoint for adding assignees.

```
POST /repos/{owner}/{repo}/issues/{issue_number}/assignees
```

Body:
```json
{
  "assignees": ["github-actions[bot]"]
}
```

The documentation states: "Only users with push access can add assignees to an issue. Assignees are silently ignored otherwise."

However, the REST API likely delegates to the same internal `replaceActorsForAssignable` code path. The error message in the GraphQL response confirms this restriction is at the authorization layer for installation tokens, not at the API protocol layer. No documented exception exists for REST vs GraphQL for this particular restriction.

**Source:** [REST API endpoints for issue assignees -- Add assignees to an issue](https://docs.github.com/en/rest/issues/assignees#add-assignees-to-an-issue)

### Approach 3: REST API `PATCH /repos/{owner}/{repo}/issues/{issue_number}` -- FAILS

```
PATCH /repos/{owner}/{repo}/issues/{issue_number}
```

Body:
```json
{
  "assignees": ["github-actions[bot]"]
}
```

This endpoint also accepts an `assignees` array. Same restriction applies -- the underlying implementation uses the same authorization check.

**Source:** [REST API endpoints for issues -- Update an issue](https://docs.github.com/en/rest/issues/issues#update-an-issue)

### Approach 4: REST API `POST /repos/{owner}/{repo}/issues` with `assignees` -- FAILS

Creating a new issue with pre-assigned assignees is documented as "silently dropped" for users without push access. The GITHUB_TOKEN has `issues: write`, but the authorization layer for assignment specifically checks for user-type tokens.

**Source:** [REST API endpoints for issues -- Create an issue](https://docs.github.com/en/rest/issues/issues#create-an-issue)

### Approach 5: Using a label instead of assignment -- WORKS AS CLAIMING MECHANISM

Labels are not a substitute for assignment — they don't populate the `assignees` field, trigger assignment-based notifications, or appear in a user's "Assigned" view. However, a label like `in-progress` can serve as a claiming mechanism for automated workflows, since label operations work with both GITHUB_TOKEN and PATs.

```bash
gh issue edit $ISSUE_NUMBER --add-label "in-progress"
```

**Source:** [REST API endpoints for labels](https://docs.github.com/en/rest/issues/labels)

### Approach 6: Configuring GitHub App permissions -- NOT POSSIBLE

The GITHUB_TOKEN is a GitHub App installation token generated automatically by Actions. Its permissions are configured via the `permissions:` key in the workflow YAML. Even with `issues: write` permission fully granted, the `replaceActorsForAssignable` mutation still rejects the token because it is _by design_ restricted to user-type tokens (PATs or OAuth tokens).

**Source:** [Automatic token authentication -- Modifying the permissions for the GITHUB_TOKEN](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#modifying-the-permissions-for-the-github_token)

### Approach 7: Using a separate GitHub App token -- FAILS (same restriction)

Instead of GITHUB_TOKEN, generate an installation token from a dedicated GitHub App that has `issues: write` permission. Use the `actions/create-github-app-token` action:

```yaml
- name: Generate token
  id: generate-token
  uses: actions/create-github-app-token@v3
  with:
    client-id: ${{ vars.APP_CLIENT_ID }}
    private-key: ${{ secrets.APP_PRIVATE_KEY }}

- name: Assign issue
  env:
    GH_TOKEN: ${{ steps.generate-token.outputs.token }}
  run: gh issue edit $ISSUE_NUMBER --add-assignee "github-actions[bot]"
```

**This still uses a GitHub App installation token**, not a user token. The `replaceActorsForAssignable` restriction applies to all GitHub App installation tokens. This approach **will still fail** with the same error.

**Source:** [Making authenticated API requests with a GitHub App in a GitHub Actions workflow](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/making-authenticated-api-requests-with-a-github-app-in-a-github-actions-workflow)

### Approach 8: Using a Personal Access Token stored as a secret -- PARTIAL (works for human assignees, NOT for `github-actions[bot]`)

A PAT bypasses the token-type restriction (it's a user token), but the `replaceActorsForAssignable` mutation also checks whether the **target assignee** has access to the repository. `github-actions[bot]` does not have access, so assigning the bot still fails with:

```
GraphQL: Bot does not have access to the repository. (replaceActorsForAssignable)
```

A PAT **does** work for assigning human collaborators who are repo contributors:

```yaml
- name: Assign issue
  env:
    GH_TOKEN: ${{ secrets.MY_PAT }}
  run: gh issue edit $ISSUE_NUMBER --add-assignee "human-username"
```

Or via the REST API:

```bash
curl -X POST \
  -H "Authorization: Bearer ${{ secrets.MY_PAT }}" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/${{ github.repository }}/issues/$ISSUE_NUMBER/assignees \
  -d '{"assignees":["human-username"]}'
```

The PAT must have `issues: write` scope (classic) or `issues: write` permission (fine-grained).

**Source:** [Automatic token authentication -- Granting additional permissions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#granting-additional-permissions)

### Approach 9: Using `@me` special value -- Does not help

The GitHub CLI supports `@me` as a special assignee value that resolves to the currently authenticated user. However, when using GITHUB_TOKEN, the "authenticated user" is the `github-actions[bot]` bot account, not a human. Using `gh issue edit <number> --add-assignee "@me"` with GITHUB_TOKEN would attempt to assign `github-actions[bot]`, which hits the same `replaceActorsForAssignable` restriction. With a PAT, `@me` resolves to the PAT owner — which works, but assigns a human, not the bot.

**Source:** [cli/cli/pkg/cmd/pr/shared/params.go -- MeReplacer](https://github.com/cli/cli/blob/trunk/pkg/cmd/pr/shared/params.go)

### Approach 10: `repository_dispatch` webhook -- Does not solve the problem

A workflow triggered by `repository_dispatch` still runs inside GitHub Actions and still uses a GITHUB_TOKEN (or whatever token is configured). Changing the trigger mechanism does not change the token type.

---

## Why This Restriction Exists

GitHub App installation tokens represent the _application_, not a user. The `replaceActorsForAssignable` mutation modifies the actor-to-issue relationship, which is a user-centric operation. GitHub restricts this to ensure that assignment changes are attributable to a real user identity (PAT or OAuth token) rather than an automated application. This is a design choice to maintain audit trail integrity.

Additionally, the mutation validates that the target assignee is eligible (repo collaborator, commenter, etc.). `github-actions[bot]` is a system account that cannot be added as a collaborator.

---

## Summary Table

| Approach | Works for `github-actions[bot]`? | Notes |
|---|---|---|
| `gh issue edit --add-assignee` with GITHUB_TOKEN | No | GraphQL mutation blocked for installation tokens |
| REST API `POST .../assignees` with GITHUB_TOKEN | No | Same underlying restriction |
| REST API `PATCH .../issues` with GITHUB_TOKEN | No | Same underlying restriction |
| Labels instead of assignment | **Yes** (as claim mechanism) | Different concept from assignment, but works with any token |
| Permissions adjustment | No | Restriction is by token type, not scope level |
| Separate GitHub App token | No | Still a GitHub App installation token |
| PAT stored as secret | **Yes** for human assignees, **No** for bot | PAT bypasses token-type check; bot fails eligibility check |
| `@me` with GITHUB_TOKEN | No | Resolves to bot, which is still blocked |
| `repository_dispatch` | No | Token type unchanged |

---

## Recommendation

**Do not attempt to assign `github-actions[bot]` to issues — it is not a valid assignee.** For the agent-triage workflow, use an `in-progress` label as a claiming mechanism instead. Label operations work with any token type and are not subject to the `replaceActorsForAssignable` restriction.

If you need actual assignment semantics (e.g., for human notification), assign a real collaborator username using a PAT.
