#!/usr/bin/env python3
import subprocess
import sys


def format_python():
    """Format Python files with Black and Ruff."""
    try:
        subprocess.run(
            ["black", "--line-length", "79", "tools/", "src/", "tests/"],
            check=True,
        )
        subprocess.run(
            ["ruff", "check", "--fix", "tools/", "src/", "tests/"], check=True
        )
        print("Python files formatted successfully.")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Error formatting Python files: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(format_python())
