#!/usr/bin/env python3
import json
import glob
import os
import sys


def format_json():
    """Format JSON files in artifacts/, excluding mission_template.json."""
    files = [
        f
        for f in glob.glob("artifacts/*.json")
        if "mission_template.json" not in os.path.basename(f)
    ]
    for file in files:
        try:
            with open(file, "r") as f:
                if not f.read().strip():
                    continue  # Skip lege bestanden
                f.seek(0)
                data = json.load(f)
            with open(file, "w") as f:
                json.dump(data, f, indent=4)
                f.write("\n")
            print(f"Formatted {file}")
            return 0
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error formatting {file}: {e}")
            sys.exit(1)
            return 1


if __name__ == "__main__":
    format_json()
