#!/usr/bin/env bash
# uc-open-pr.sh - Create a branch, copy a file, commit, push, and open a PR.
#
# Usage: scripts/uc-open-pr.sh <branch-name> <source-file> <commit-message> [destination]
#
# Requires the GitHub CLI (gh) for automatic PR creation.
set -euo pipefail

if [[ $# -lt 3 ]]; then
  echo "Usage: scripts/uc-open-pr.sh <branch-name> <source-file> <commit-message> [destination]" >&2
  exit 1
fi

branch="$1"
source_file="$2"
commit_msg="$3"
dest="${4:-$(basename "$source_file")}" 

if [[ ! -f "$source_file" ]]; then
  echo "Source file '$source_file' not found" >&2
  exit 1
fi

# Create a branch for the new changes
git checkout -b "$branch"

# Copy the file into the repository
cp "$source_file" "$dest"

# Commit and push
git add "$dest"
git commit -m "$commit_msg"
git push -u origin "$branch"

# Open a pull request with gh CLI if available
if command -v gh >/dev/null 2>&1; then
  gh pr create --fill --title "$commit_msg"
else
  echo "gh CLI not found; create the pull request manually." >&2
fi
