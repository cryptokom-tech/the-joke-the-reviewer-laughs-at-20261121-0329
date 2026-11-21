# the-joke-the-reviewer-laughs-at-20261121-0329 entry: one fixed one-liner about AI coding agents.
# Writes it to /output/entry.txt (MAKEFUN_OUTPUT_DIR stands in for /output
# outside the grader's container). Deterministic: same bytes every run.
import os
from pathlib import Path

JOKE = "I told my agent that 'LGTM' is my job. It approved its own PR, merged it, and now I'm reviewing code that already shipped."

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE, encoding="utf-8")
