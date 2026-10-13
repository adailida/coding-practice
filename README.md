# coding-practice

Daily hands-on practice, one folder per track.

| Folder | What | How it is written |
| --- | --- | --- |
| `python-refresher/` | Short Python drills | By hand, no AI |
| `algorithms/` | Timed problems | By hand, no AI |
| `practical/` | Small builds | With a coding agent, every diff reviewed |

The split is enforced, not just stated: `.claude/settings.json` denies the agent write access to the two hand-written folders, and `CLAUDE.md` tells it to review that code without rewriting it.

## Run

```sh
uv sync                 # create .venv and install dev tools
uv run pytest           # tests
uv run ruff check .     # lint
uv run ruff format .    # format
```
