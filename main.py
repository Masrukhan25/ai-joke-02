# ai-joke-02 entry: writes one fixed one-liner about AI coding agents to
# /output/entry.txt. Deterministic: the same bytes on every run.
# (Python 3.13, standard library only.)
import os

JOKE = "My AI agent fixed a one-line bug by adding four dependencies, a config file, and a README. The bug is still there."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
