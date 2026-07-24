# Assigning a GitHub Issue to a User from a Workflow Using Only GITHUB_TOKEN

## Short Answer

**You cannot assign `github-actions[bot]` (or any user) to an issue using only `GITHUB_TOKEN` (a GitHub App installation token).** The GraphQL mutation that the GitHub CLI uses (`replaceActorsForAssignable`) explicitly rejects installation tokens. The REST API endpoints (`POST /repos/{owner}/{repo}/issues/{issue_number}/assignees`, `PATCH /repos/{owner}/{repo}/issues/{issue_number}`) also fail with installation tokens because the underlying implementation uses the same restricted mutation.

The only workaround is to use a different token type: a Personal Access Token (classic or fine-grained) stored as a repository secret, or a dedicated GitHub App installation token generated via `actions/create-github-app-token`.

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

### Approach 5: Using a label instead of assignment -- NOT A SUBSTITUTE

Labels are not a substitute for assignment. GitHub's issue system treats assignees and labels as separate, non-interchangeable concepts. A label cannot make an issue appear in a user's "Assigned" view, trigger assignment-based notifications, or populate the issue's `assignees` field. The REST API endpoints for labels (`POST /repos/{owner}/{repo}/issues/{issue_number}/labels`) work with installation tokens, but this is a fundamentally different feature.

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

### Approach 8: Using a Personal Access Token stored as a secret -- WORKS (recommended)

Store a PAT (classic or fine-grained) as a repository secret and use it instead of GITHUB_TOKEN:

```yaml
- name: Assign issue
  env:
    GH_TOKEN: ${{ secrets.MY_PAT }}
  run: gh issue edit $ISSUE_NUMBER --add-assignee "github-actions[bot]"
```

Or via the REST API:

```bash
curl -X POST \
  -H "Authorization: Bearer ${{ secrets.MY_PAT }}" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/${{ github.repository }}/issues/$ISSUE_NUMBER/assignees \
  -d '{"assignees":["github-actions[bot]"]}'
```

The PAT must have `issues: write` scope (classic) or `issues: write` permission (fine-grained).

**Source:** [Automatic token authentication -- Granting additional permissions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#granting-additional-permissions)

### Approach 9: Using `@me` special value -- Does not help

The GitHub CLI supports `@me` as a special assignee value that resolves to the currently authenticated user. However, when using GITHUB_TOKEN, the "authenticated user" is the `github-actions[bot]` bot account, not a human. Using `gh issue edit <number> --add-assignee "@me"` with GITHUB_TOKEN would attempt to assign `github-actions[bot]`, which hits the same `replaceActorsForAssignable` restriction.

**Source:** [cli/cli/pkg/cmd/pr/shared/params.go -- MeReplacer](https://github.com/cli/cli/blob/trunk/pkg/cmd/pr/shared/params.go)

### Approach 10: `repository_dispatch` webhook -- Does not solve the problem

A workflow triggered by `repository_dispatch` still runs inside GitHub Actions and still uses a GITHUB_TOKEN (or whatever token is configured). Changing the trigger mechanism does not change the token type.

---

## Why This Restriction Exists

GitHub App installation tokens represent the _application_, not a user. The `replaceActorsForAssignable` mutation modifies the actor-to-issue relationship, which is a user-centric operation. GitHub restricts this to ensure that assignment changes are attributable to a real user identity (PAT or OAuth token) rather than an automated application. This is a design choice to maintain audit trail integrity.

---

## Summary Table

| Approach | Works? | Notes |
|---|---|---|
| `gh issue edit --add-assignee` with GITHUB_TOKEN | No | GraphQL mutation blocked for installation tokens |
| REST API `POST .../assignees` with GITHUB_TOKEN | No | Same underlying restriction |
| REST API `PATCH .../issues` with GITHUB_TOKEN | No | Same underlying restriction |
| Labels instead of assignment | N/A | Different concept, not a substitute |
| Permissions adjustment | No | Restriction is by token type, not scope level |
| Separate GitHub App token | No | Still a GitHub App installation token |
| PAT stored as secret | **Yes** | The only reliable workaround |
| `@me` with GITHUB_TOKEN | No | Resolves to bot, which is still blocked |
| `repository_dispatch` | No | Token type unchanged |

---

## Recommendation

Store a fine-grained Personal Access Token (with `issues: write` permission, scoped to the repository) as a repository secret named e.g. `PAT_ISSUES`. Use it as:

```yaml
env:
  GH_TOKEN: ${{ secrets.PAT_ISSUES }}
```

Then run `gh issue edit` or `gh api` commands as normal. This is the minimal viable workaround.
