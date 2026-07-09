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
  "rubrics/direction-gate.md"
  "rubrics/product-logic-generic.md"
  "templates/design-plan.md"
  "templates/prd.md"
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

echo "Required files OK."
echo "No .DS_Store files found."
echo "Before publishing, also manually review RELEASE_CHECKLIST.md."
