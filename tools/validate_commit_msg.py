#!/usr/bin/env python3
import subprocess
import sys
import re

def validate_commit_msg():
    """Validate if the latest commit message triggers a PR creation."""
    try:
        # Haal het laatste commit-bericht op
        commit_msg = subprocess.check_output(["git", "log", "-1", "--pretty=%B"]).decode().strip()
        print(f"DEBUG: Raw commit message: '{commit_msg}'")

        # Check of het bericht begint met create-pr(...)
        pattern = r'^create-pr\(title=(.+?);description=(.+?)\)$'
        match = re.match(pattern, commit_msg)
        if not match:
            print("DEBUG: Commit message does not match 'create-pr(title=<title>;description=<desc>)' format—skipping.")
            return None  # Geen PR nodig

        title, description = match.groups()
        print(f"DEBUG: Parsed title: '{title}'")
        print(f"DEBUG: Parsed description: '{description}'")

        if not title or len(title) < 3:
            print(f"Error: Title must be at least 3 characters long (got '{title}').")
            return False
        if not description:
            print("Error: Description cannot be empty.")
            return False

        print("Commit message validated successfully for PR creation.")
        return {"title": title, "description": description}
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving commit message: {e}")
        return False

if __name__ == "__main__":
    result = validate_commit_msg()
    sys.exit(0 if result is not False else 1)