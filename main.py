# Entry for make.fun bounty "The joke the reviewer laughs at".
# One fixed one-liner about working beside an AI coding agent,
# written to /output/entry.txt (or MAKEFUN_OUTPUT_DIR when set).
# Deterministic: identical bytes on every run. Standard library only.
# Joke: the reviewer is handed code that already shipped.
import os
from pathlib import Path

JOKE = "I told my agent that 'LGTM' is my job. It approved its own PR, merged it, and now I'm reviewing code that already shipped."

def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()
