#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

required_files=(
  "README.md"
  "QUICKSTART.md"
  "PROJECT_INDEX.md"
  "AGENTS.template.md"
  "LICENSE"
  "CONTRIBUTING.md"
  "SECURITY.md"
  "CODE_OF_CONDUCT.md"
  "RELEASE_CHECKLIST.md"
  ".github/pull_request_template.md"
  ".github/ISSUE_TEMPLATE/bug_report.md"
  ".github/ISSUE_TEMPLATE/feature_request.md"
  "workflows/end-to-end-prd.md"
  "workflows/single-module-task.md"
  "workflows/review-and-retrospective.md"
  "workflows/runtime-state.md"
  "workflows/context-and-evidence.md"
  "workflows/approval-and-parallelism.md"
  "rubrics/direction-gate.md"
  "rubrics/product-logic-generic.md"
  "rubrics/issue-severity.md"
  "rubrics/reverse-engineering-quality.md"
  "rubrics/prototype-output-quality.md"
  "templates/design-plan.md"
  "templates/current-state.md"
  "templates/stage-handoff.md"
  "templates/prd.md"
  "evals/README.md"
  "evals/scoring.md"
  "evals/cases/generic-regression-cases.md"
  "scripts/validate-framework.py"
  "scripts/validate-config.py"
  "scripts/smoke-test-install.sh"
  ".github/workflows/validate.yml"
)

for file in "${required_files[@]}"; do
  if [ ! -f "$file" ]; then
    echo "Missing required file: $file"
    exit 1
  fi
done

if find . -name ".DS_Store" | grep -q .; then
  echo "Found .DS_Store files. Remove them before publishing."
  find . -name ".DS_Store"
  exit 1
fi

if grep -RInE '(/Users/[^/[:space:]]+/|/home/[^/[:space:]]+/|[A-Za-z]:\\Users\\[^\\[:space:]]+\\)' . \
  --exclude-dir=.git \
  --exclude=RELEASE_CHECKLIST.md \
  --exclude=check-release.sh; then
  echo "Found possible local absolute paths. Review before publishing."
  exit 1
fi

if grep -RInE '(https?://[^[:space:]]*(kms\.|\.feishu\.cn/(wiki|docx|sheets|base)/)|<cite[[:space:]][^>]*doc-id=)' . \
  --exclude-dir=.git \
  --exclude=check-release.sh \
  --exclude=open-source-checklist.md \
  --exclude=RELEASE_CHECKLIST.md; then
  echo "Found possible private documentation links or embedded document tokens."
  exit 1
fi

if [ -n "${FORGE_RELEASE_DENY_PATTERN:-}" ]; then
  if grep -RInE "$FORGE_RELEASE_DENY_PATTERN" . --exclude-dir=.git; then
    echo "Found content matching FORGE_RELEASE_DENY_PATTERN."
    exit 1
  fi
fi

python3 scripts/validate-framework.py
bash scripts/smoke-test-install.sh

echo "Required files OK."
echo "No .DS_Store files found."
echo "Framework structure OK."
echo "Install smoke test OK."
echo "Before publishing, also manually review RELEASE_CHECKLIST.md."
