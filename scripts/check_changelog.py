"""Fail a pull request that changes what the service depends on without a changelog entry."""

import subprocess
import sys

base = sys.argv[1]
changed = subprocess.run(["git", "diff", "--name-only", f"{base}...HEAD"], capture_output=True,
                         text=True, check=True).stdout.split()
if "requirements.txt" in changed and "CHANGELOG.md" not in changed:
    print("::error::requirements.txt changed and CHANGELOG.md did not. Every dependency change "
          "needs a line under '## Unreleased' in CHANGELOG.md saying what moved and why.")
    sys.exit(1)
print("changelog check passed")
