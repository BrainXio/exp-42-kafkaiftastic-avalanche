#!/usr/bin/env python3
import subprocess
import sys


def pre_commit_check():
    """Run pre-commit checks on all files without installing hooks."""
    print("Check commit-worthy formatting... 🤖")
    try:
        result = subprocess.run(
            ["pre-commit", "run", "--all-files"], check=False
        )
        if result.returncode == 0:
            print("Git hooks are !")
            print("All pre-commit checks passed. Bots approve!")
        else:
            print(
                "Pre-commit checks failed. Bots detected issues—fix and retry!"
            )
            sys.exit(1)
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Failed to run pre-commit checks: {e}")
        sys.exit(1)
        return 1


if __name__ == "__main__":
    pre_commit_check()
