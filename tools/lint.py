#!/usr/bin/env python3
import subprocess
import sys

def lint():
    """Lint Python files with Black, Flake8, and Ruff."""
    try:
        subprocess.run(["black", "--check", "--line-length", "79", "src/", "tests/"], check=True)
        subprocess.run(["flake8", "src/", "tests/"], check=True)
        subprocess.run(["ruff", "check", "src/", "tests/"], check=True)
        print("Linting passed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Linting failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    lint()
