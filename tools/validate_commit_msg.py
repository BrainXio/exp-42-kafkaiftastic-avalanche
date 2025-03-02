#!/usr/bin/env python3
import subprocess
import sys

def validate_commit_msg():
    """Validate the latest commit message for PR creation."""
    try:
        # Haal het laatste commit-bericht op
        commit_msg = subprocess.check_output(["git", "log", "-1", "--pretty=%B"]).decode().strip()
        print(f"Validating commit message: '{commit_msg}'")
        if not commit_msg:
            print("Error: No commit message found.")
            return False

        lines = commit_msg.splitlines()
        title = lines[0].strip() if lines else ""
        description = "\n".join(line.strip() for line in lines[1:]) if len(lines) > 1 else ""

        # Minimaal 3 karakters voor titel (minder streng dan 5)
        if not title or len(title) < 3:
            print(f"Error: Commit title must be at least 3 characters long (got '{title}').")
            return False

        print("Commit message validated successfully.")
        return {"title": title, "description": description}
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving commit message: {e}")
        return False

if __name__ == "__main__":
    result = validate_commit_msg()
    sys.exit(0 if result else 1)