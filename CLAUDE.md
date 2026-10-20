# coding-practice

Alex's coding practice repo. Two kinds of work live here, with different rules.

## Hand-written tracks: `python-refresher/`, `algorithms/`

- Alex writes every line. Never create or edit files in these folders (a deny rule in `.claude/settings.json` also blocks edits).
- One exception (agreed 2026-10-20): Claude creates the daily warmup file `python-refresher/YYYY-MM-DD.py` with prompt comments and asserts only, no solutions. Verify the drills against reference solutions in a scratch folder first, then copy the file in. Never touch it after it is created.
- When reviewing his code: mark each line that is wrong and state the rule. Do not rewrite the line or show a corrected version. He fixes it and reruns.
- No hints before he has made an attempt. One drill or problem at a time.
- He commits this work himself.

## Agent-assisted track: `practical/`

- Agree on a short plan before writing code. Keep diffs small enough to review in one sitting.
- Every change comes with a test. Run the checks below before saying a change is done, and report the real output.
- Alex reads every diff before it is committed. Do not commit or push unless he asks.

## Commands

- `uv sync`: create `.venv` and install dev tools
- `uv run pytest`: run tests
- `uv run ruff check .`: lint
- `uv run ruff format .`: format
- `uv run python <file>`: run a script with the project's Python (the system `python3` is 3.9)

## Conventions

- Python 3.12, managed by uv. No dependencies beyond the standard library unless a `practical/` build needs one.
- Tests are `test_*.py` files next to the code they test, with unique file names across the repo.
- Commit subjects are short and imperative.
