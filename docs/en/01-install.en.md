# Install

Run this command in a terminal. It needs Node.js (for `npx`).

```bash
npx skills add tranthethang/agent-plain-writing -g
```

- `tranthethang/agent-plain-writing` is the GitHub repository that holds the skill.
- `-g` installs the skill globally (for your user), not into one project. Drop `-g` to install into the current project.

The command installs all six skills together: the router `agent-plain-writing` and the five `agent-plain-writing-<type>` sub-skills. Then ask your agent to use `agent-plain-writing`, or one sub-skill. See [02-usage](02-usage.en.md).

## Install by hand

If you do not use `npx`, copy every folder `skills/agent-plain-writing*/` into the skills folder of your agent. Copy all six. Keep each folder name equal to the `name` in its `SKILL.md`.

| Tool | Where |
|---|---|
| Claude Code | `.claude/skills/` (project) or `~/.claude/skills/` (personal) |
| Other tools that read `SKILL.md` | See the tool's documentation |

## Notes

- Python 3.7 or later is needed only to run the checker ([03-checker](03-checker.en.md)). The skill has no other dependency.

Next: [02-usage](02-usage.en.md).
