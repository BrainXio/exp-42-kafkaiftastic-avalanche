#!/usr/bin/env python3
import glob
import os
import sys


def fix_whitespace():
    """Trim trailing whitespace from all files, excluding .git."""
    files = [
        f
        for f in glob.glob("**/*", recursive=True)
        if ".git" not in f and os.path.isfile(f)
    ]
    for file in files:
        try:
            with open(file, "rb") as f:
                lines = f.readlines()
            with open(file, "wb") as f:
                for line in lines:
                    f.write(line.rstrip() + b"\n")
            print(f"Trimmed whitespace in {file}")
            return 0
        except IOError as e:
            print(f"Error trimming whitespace in {file}: {e}")
            sys.exit(1)
            return 1


if __name__ == "__main__":
    fix_whitespace()
