#!/usr/bin/env python3
import subprocess
import sys


def run_consumer():
    """Run the consumer."""
    try:
        subprocess.run(["python", "src/consumer.py"], check=True)
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Consumer run failed: {e}")
        sys.exit(1)
        return 1


if __name__ == "__main__":
    run_consumer()
