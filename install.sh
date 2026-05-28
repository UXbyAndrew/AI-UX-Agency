#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/UXbyAndrew/AI-UX-Agency"
TMP_DIR=""
SOURCE_DIR=""

print_step() { printf "\n==> %s\n" "$1"; }
print_ok() { printf "✅ %s\n" "$1"; }
print_warn() { printf "⚠️  %s\n" "$1"; }

cleanup() {
  if [[ -n "${TMP_DIR}" && -d "${TMP_DIR}" ]]; then
    rm -rf "${TMP_DIR}"
  fi
}
trap cleanup EXIT

if [[ -f "./ux/SKILL.md" && -d "./skills" && -d "./agents" ]]; then
  SOURCE_DIR="$(pwd)"
else
  if ! command -v git >/dev/null 2>&1; then
    echo "git is required when installing remotely. Install git or run this script from the cloned repo."
    exit 1
  fi
  TMP_DIR="$(mktemp -d)"
  print_step "Cloning AI UX Claude suite"
  git clone --depth 1 "${REPO_URL}.git" "${TMP_DIR}/ai-ux-claude"
  SOURCE_DIR="${TMP_DIR}/ai-ux-claude"
fi

print_step "Checking Claude Code installation"
if command -v claude >/dev/null 2>&1; then
  print_ok "Claude Code command found"
else
  print_warn "Claude Code command not found in PATH. Files will still be installed to ~/.claude."
fi

CLAUDE_DIR="${HOME}/.claude"
SKILLS_DIR="${CLAUDE_DIR}/skills"
AGENTS_DIR="${CLAUDE_DIR}/agents"
UX_MAIN_DIR="${SKILLS_DIR}/ux"

print_step "Creating Claude directories"
mkdir -p "${SKILLS_DIR}" "${AGENTS_DIR}"

print_step "Installing main UX orchestrator"
rm -rf "${UX_MAIN_DIR}"
mkdir -p "${UX_MAIN_DIR}"
cp -R "${SOURCE_DIR}/ux/"* "${UX_MAIN_DIR}/"

# Bundle shared resources under main ux skill as well, so the orchestrator can reference them.
mkdir -p "${UX_MAIN_DIR}/scripts" "${UX_MAIN_DIR}/templates" "${UX_MAIN_DIR}/agents" "${UX_MAIN_DIR}/skills"
cp -R "${SOURCE_DIR}/scripts/"* "${UX_MAIN_DIR}/scripts/" 2>/dev/null || true
cp -R "${SOURCE_DIR}/templates/"* "${UX_MAIN_DIR}/templates/" 2>/dev/null || true
cp -R "${SOURCE_DIR}/agents/"* "${UX_MAIN_DIR}/agents/" 2>/dev/null || true
cp -R "${SOURCE_DIR}/skills/"* "${UX_MAIN_DIR}/skills/" 2>/dev/null || true

print_step "Installing UX workflow skills"
for skill_dir in "${SOURCE_DIR}"/skills/ux-*; do
  [[ -d "${skill_dir}" ]] || continue
  skill_name="$(basename "${skill_dir}")"
  rm -rf "${SKILLS_DIR}/${skill_name}"
  mkdir -p "${SKILLS_DIR}/${skill_name}"
  cp -R "${skill_dir}/"* "${SKILLS_DIR}/${skill_name}/"
done

print_step "Installing UX agents"
for agent_file in "${SOURCE_DIR}"/agents/ux-*.md; do
  [[ -f "${agent_file}" ]] || continue
  cp "${agent_file}" "${AGENTS_DIR}/"
done

print_step "Installing shared scripts and templates into main UX skill"
mkdir -p "${UX_MAIN_DIR}/scripts" "${UX_MAIN_DIR}/templates"
cp -R "${SOURCE_DIR}/scripts/"* "${UX_MAIN_DIR}/scripts/" 2>/dev/null || true
cp -R "${SOURCE_DIR}/templates/"* "${UX_MAIN_DIR}/templates/" 2>/dev/null || true

print_step "Checking optional Python dependencies"
if command -v python3 >/dev/null 2>&1; then
  print_ok "python3 found"
  if python3 - <<'PY' >/dev/null 2>&1
import bs4
PY
  then
    print_ok "BeautifulSoup dependency found"
  else
    print_warn "Optional dependency missing: beautifulsoup4. Install with: pip install -r scripts/requirements.txt"
  fi
else
  print_warn "python3 not found. Python utility scripts will not run until Python is installed."
fi

print_step "Installation complete"
cat <<MSG

AI UX Claude has been installed.

Installed locations:
- Main skill: ${UX_MAIN_DIR}
- Workflow skills: ${SKILLS_DIR}/ux-*
- Agents: ${AGENTS_DIR}/ux-*.md

Start a new Claude Code session and try:

  /ux quick <url or product>
  /ux audit <url or product>
  /ux strategy <product problem>

MSG
