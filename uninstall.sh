#!/usr/bin/env bash
set -euo pipefail

CLAUDE_DIR="${HOME}/.claude"
SKILLS_DIR="${CLAUDE_DIR}/skills"
AGENTS_DIR="${CLAUDE_DIR}/agents"

printf "This will remove AI UX Claude skills and agents from ~/.claude. Continue? [y/N] "
read -r answer
case "${answer}" in
  y|Y|yes|YES)
    ;;
  *)
    echo "Uninstall cancelled."
    exit 0
    ;;
esac

echo "Removing main UX skill..."
rm -rf "${SKILLS_DIR}/ux"

echo "Removing UX workflow skills..."
find "${SKILLS_DIR}" -maxdepth 1 -type d -name 'ux-*' -exec rm -rf {} + 2>/dev/null || true

echo "Removing UX agents..."
find "${AGENTS_DIR}" -maxdepth 1 -type f -name 'ux-*.md' -delete 2>/dev/null || true

echo "AI UX Claude uninstalled."
