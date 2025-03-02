#!/usr/bin/env python3
import glob
import os

def fix_eof():
    """Ensure all files end with a newline."""
    files = [f for f in glob.glob("**/*", recursive=True) if ".git" not in f and os.path.isfile(f)]
    for file in files:
        with open(file, "rb") as f:
            content = f.read()
        if not content.endswith(b"\n"):
            with open(file, "ab") as f:
                f.write(b"\n")
            print(f"Fixed EOF for {file}")

if __name__ == "__main__":
    fix_eof()
