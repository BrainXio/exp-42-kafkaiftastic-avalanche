#!/usr/bin/env python3
import yaml
import glob
import sys


def format_yaml():
    """Format YAML files in the root directory."""
    files = glob.glob("*.yml")
    for file in files:
        try:
            with open(file, "r") as f:
                data = yaml.safe_load(f)
            with open(file, "w") as f:
                yaml.dump(data, f, indent=2)
            print(f"Formatted {file}")
            return 0
        except (yaml.YAMLError, IOError) as e:
            print(f"Error formatting {file}: {e}")
            sys.exit(1)
            return 1


if __name__ == "__main__":
    format_yaml()
