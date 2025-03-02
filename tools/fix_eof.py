#!/usr/bin/env python3
import glob
import os
import sys
from gitignore_parser import parse_gitignore


def ignore_nothing(path):
    """Default ignore function that ignores nothing."""
    return False


def fix_eof():
    """Add a newline to files missing one at the end,
    ignoring .gitignore patterns."""
    # Parse .gitignore of gebruik een lege functie als fallback
    ignore = (
        parse_gitignore(".gitignore")
        if os.path.exists(".gitignore")
        else ignore_nothing
    )

    # Filter bestanden, exclusief .git en .gitignore-patronen
    files = [
        f
        for f in glob.glob("**/*", recursive=True)
        if ".git" not in f and os.path.isfile(f) and not ignore(f)
    ]
    modified = False
    for file in files:
        try:
            with open(file, "rb") as f:
                content = f.read()
            if content and not content.endswith(b"\n"):
                with open(file, "ab") as f:
                    f.write(b"\n")
                print(f"Added newline to {file}")
                modified = True
        except IOError as e:
            print(f"Error processing {file}: {e}")
            return 1
    if not modified:
        print("No files needed newline fixes.")
    return 0


if __name__ == "__main__":
    sys.exit(fix_eof())
