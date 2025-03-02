#!/usr/bin/env python3
import subprocess
import sys

def run_producer():
    """Run the dummy producer."""
    try:
        subprocess.run(["python", "src/dummy_producer.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Producer run failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_producer()
