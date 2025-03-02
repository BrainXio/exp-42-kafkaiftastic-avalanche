#!/usr/bin/env python3
import subprocess
import sys

def setup_githooks():
    """Install and run pre-commit hooks."""
    print("Setting up git hooks to catch all the bots... Here’s your bot net! 🤖")
    try:
        subprocess.run(["pre-commit", "install"], check=True)
        result = subprocess.run(["pre-commit", "run", "--all-files"])
        if result.returncode != 0:
            subprocess.run(["git", "add", "."], check=True)
            print("Auto-fixes applied and staged!")
        print("Hooks installed and tested. Now fishing with chaotical splendor—way more bots in sight!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to setup githooks: {e}")
        sys.exit(1)

if __name__ == "__main__":
    setup_githooks()
