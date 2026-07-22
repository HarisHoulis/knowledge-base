# OpenCode Repo-Level Skill Loading

## Question

Can opencode load skills vendored inside a repo (e.g., under `.opencode/skills/`), or are skills only loaded from `~/.config/opencode/skills/`?

## Answer: Yes — skills can be vendored in-repo

OpenCode discovers skills from **both** the repo and the global config directory. Repo-level skills are the recommended approach for project-specific workflows.

## Discovery locations (in order of search)

OpenCode searches these paths for `<name>/SKILL.md`:

| Scope | Path |
|---|---|
| Project (repo) | `.opencode/skills/<name>/SKILL.md` |
| Project (Claude compat) | `.claude/skills/<name>/SKILL.md` |
| Project (agent compat) | `.agents/skills/<name>/SKILL.md` |
| Global | `~/.config/opencode/skills/<name>/SKILL.md` |
| Global (Claude compat) | `~/.claude/skills/<name>/SKILL.md` |
| Global (agent compat) | `~/.agents/skills/<name>/SKILL.md` |

## How discovery works

For project-local paths, OpenCode walks up from the current working directory until it reaches the git worktree root. It loads any matching `skills/*/SKILL.md` in `.opencode/`, `.claude/skills/*/SKILL.md`, or `.agents/skills/*/SKILL.md` along the walk.

Global definitions from `~/.config/opencode/skills/*/SKILL.md`, `~/.claude/skills/*/SKILL.md`, and `~/.agents/skills/*/SKILL.md` are always loaded.

## Skill file format

Each `SKILL.md` must have YAML frontmatter with:
- `name` (required) — must match the directory name, lowercase alphanumeric with hyphens
- `description` (required) — 1–1024 chars
- `license` (optional)
- `compatibility` (optional)
- `metadata` (optional, string-to-string map)

## Permission control

Skills can be allowed/denied/ask per agent or globally in `opencode.json` using pattern-based permission rules on the `skill` key:

```json
{
  "permission": {
    "skill": {
      "*": "allow",
      "internal-*": "deny"
    }
  }
}
```

## No config needed to enable repo-level skills

You do **not** need an `opencode.json` or any config file in the repo. Simply create e.g. `.opencode/skills/my-skill/SKILL.md` and opencode discovers it automatically when the agent is inside the repo's git worktree.

## Current state of this repo (`knowledge-base`)

This repo has **no** `.opencode/` directory and **no** `opencode.json`/`opencode.jsonc` at its root. All 26 skills in use are loaded from the global directory (`~/.config/opencode/skills/`). A repo-local skill could be added at any time by creating `.opencode/skills/<name>/SKILL.md`.

## Sources

- [OpenCode Skills docs](https://opencode.ai/docs/skills) — official skill format, placement, and discovery rules
- [OpenCode Config docs](https://opencode.ai/docs/config/) — config precedence, project vs. global, `.opencode/` directory loading
- [OpenCode Agents docs](https://opencode.ai/docs/agents/) — how agents use skills and override permissions
- Local inspection of `~/.config/opencode/skills/` and `~/.config/opencode/opencode.json`
