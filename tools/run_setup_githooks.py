#!/usr/bin/env python3
import subprocess
import sys


def setup_githooks():
    """Install and run pre-commit hooks."""
    print(
        "Setting up git hooks to catch all the bots... Here’s your bot net! 🤖"
    )
    try:
        subprocess.run(["pre-commit", "install"], check=True)
        result = subprocess.run(
            ["pre-commit", "run", "--all-files"], check=False
        )
        if result.returncode != 0:
            subprocess.run(["git", "add", "."], check=True)
            print("Auto-fixes applied and staged!")
        print(
            "Hooks installed and tested. Now fishing with chaotical splendor—"
        )
        print("way more bots in sight!")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Error setting up githooks: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(setup_githooks())
