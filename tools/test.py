#!/usr/bin/env python3
import subprocess
import sys


def test():
    """Run tests with pytest."""
    try:
        subprocess.run(["pytest", "tests/"], check=True)
        print("Tests passed successfully.")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Tests failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    test()
