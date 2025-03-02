#!/usr/bin/env python3
import subprocess
import sys

def format_python():
    """Format Python files with Black and Ruff."""
    try:
        subprocess.run(["black", "--line-length", "79", "src/", "tests/"], check=True)
        subprocess.run(["ruff", "check", "--fix", "src/", "tests/"], check=True)
        print("Python files formatted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error formatting Python files: {e}")
        sys.exit(1)

if __name__ == "__main__":
    format_python()
