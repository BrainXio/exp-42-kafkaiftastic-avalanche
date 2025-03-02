#!/usr/bin/env python3
import sys

def validate_pr_txt(file_path="PR.txt"):
    """Validate PR.txt content against required structure."""
    required_fields = {"Title", "Description"}
    content = {}

    try:
        with open(file_path, "r") as f:
            for line in f:
                if ":" in line:
                    key, value = map(str.strip, line.split(":", 1))
                    content[key] = value
    except FileNotFoundError:
        print("Error: PR.txt not found.")
        return False

    missing = required_fields - set(content.keys())
    if missing:
        print(f"Error: Missing required fields in PR.txt: {', '.join(missing)}")
        return False

    if not content.get("Title"):
        print("Error: Title cannot be empty.")
        return False
    if not content.get("Description"):
        print("Error: Description cannot be empty.")
        return False

    print("PR.txt validated successfully.")
    return content

if __name__ == "__main__":
    result = validate_pr_txt()
    sys.exit(0 if result else 1)