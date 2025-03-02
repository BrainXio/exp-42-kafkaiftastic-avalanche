#!/usr/bin/env python3
import subprocess
import sys

def format_markdown():
    """Format Markdown files with mdformat."""
    try:
        subprocess.run(["mdformat", "--wrap", "79", "README.md"], check=True)
        print("Markdown files formatted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error formatting Markdown files: {e}")
        sys.exit(1)

if __name__ == "__main__":
    format_markdown()
