# Install

Run this command in a terminal. It needs Node.js (for `npx`).

```bash
npx skills add tranthethang/agent-plain-writing -g
```

- `tranthethang/agent-plain-writing` is the GitHub repository that holds the skill.
- `-g` installs the skill globally (for your user), not into one project. Drop `-g` to install into the current project.

Then ask your agent to use `agent-plain-writing`. See [02-usage](02-usage.en.md).

## Install by hand

If you do not use `npx`, copy the folder `skills/agent-plain-writing/` into the skills folder of your agent. Keep the folder name equal to the `name` in `SKILL.md`.

| Tool | Where |
|---|---|
| Claude Code | `.claude/skills/` (project) or `~/.claude/skills/` (personal) |
| Other tools that read `SKILL.md` | See the tool's documentation |

## Notes

- Python 3.7 or later is needed only to run the checker ([03-checker](03-checker.en.md)). The skill has no other dependency.

Next: [02-usage](02-usage.en.md).
