#!/usr/bin/env python3
import subprocess
import sys
from datetime import datetime

def build():
    """Build Docker image with current timestamp."""
    build_date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        subprocess.run([
            "docker", "build",
            "--build-arg", f"BUILD_DATE={build_date}",
            "-t", "exp-42-kafkaiftastic-avalanche",
            "."
        ], check=True)
        print(f"Docker image built successfully with BUILD_DATE={build_date}.")
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build()
