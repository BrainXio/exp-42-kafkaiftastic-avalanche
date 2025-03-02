#!/usr/bin/env python3
import glob
import shutil
import os

def clean():
    """Remove temporary files and directories."""
    patterns = ["**/__pycache__", "**/*.egg-info", "**/*.pyc"]
    for pattern in patterns:
        for path in glob.glob(pattern, recursive=True):
            if os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Removed directory: {path}")
            elif os.path.isfile(path):
                os.remove(path)
                print(f"Removed file: {path}")
    print("Cleanup completed.")

if __name__ == "__main__":
    clean()
