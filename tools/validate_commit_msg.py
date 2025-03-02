#!/usr/bin/env python3
import subprocess
import sys
import re

def validate_commit_msg():
    """Parse and validate the latest commit message for PR creation."""
    try:
        commit_msg = subprocess.check_output(["git", "log", "-1", "--pretty=%B"]).decode().strip()
        print(f"DEBUG: Raw commit message: '{commit_msg}'")

        pattern = r'^create-pr\((.+)\)$'
        match = re.match(pattern, commit_msg)
        if not match:
            print("DEBUG: Commit message does not match 'create-pr(...)' format—skipping.")
            return None

        args_str = match.group(1)
        args = {}
        for pair in args_str.split(';'):
            if '=' in pair:
                key, value = map(str.strip, pair.split('=', 1))
                args[key] = value

        required_fields = {"title"}
        missing = required_fields - set(args.keys())
        if missing:
            print(f"Error: Missing required fields: {', '.join(missing)}")
            return False

        if not args["title"] or len(args["title"]) < 3:
            print(f"Error: Title must be at least 3 characters long (got '{args['title']}').")
            return False

        defaults = {
            "base": "main",
            "description": "No description provided.",
            "labels": "auto-generated"
        }
        for key, default in defaults.items():
            args.setdefault(key, default)

        if "labels" in args:
            args["labels"] = [label.strip() for label in args["labels"].split(",")]

        print(f"DEBUG: Parsed PR data: {args}")
        print("Commit message validated successfully.")
        return args
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving commit message: {e}")
        return False

if __name__ == "__main__":
    result = validate_commit_msg()
    if result is False:
        print("INVALID")
    elif result is None:
        print("None")
    else:
        import json
        print(json.dumps(result))
    sys.exit(0 if result is not False else 1)