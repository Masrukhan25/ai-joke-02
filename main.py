# ai-joke-02 entry: writes one one-liner joke about AI coding agents to
# /output/entry.txt. Deterministic: the same bytes on every run.
# (Python 3.13, standard library only.)
import os

JOKE = "My AI agent spent three hours debugging, then asked me what the error message meant."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
