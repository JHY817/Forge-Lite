#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEST_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/forge-lite-install.XXXXXX")"
trap 'rm -rf "$TEST_ROOT"' EXIT

mkdir -p "$TEST_ROOT/scripts"
cp -R "$ROOT_DIR/config.example" "$TEST_ROOT/config.example"
cp -R "$ROOT_DIR/templates" "$TEST_ROOT/templates"
cp "$ROOT_DIR/AGENTS.template.md" "$TEST_ROOT/AGENTS.template.md"
cp "$ROOT_DIR/scripts/setup.sh" "$TEST_ROOT/scripts/setup.sh"
cp "$ROOT_DIR/scripts/validate-config.py" "$TEST_ROOT/scripts/validate-config.py"

bash "$TEST_ROOT/scripts/setup.sh"

required=(
  "AGENTS.md"
  "config/product-context.md"
  "config/knowledge-base.yaml"
  "config/codebase.yaml"
  "config/rubric.yaml"
  "config/templates.yaml"
)

for relative in "${required[@]}"; do
  if [ ! -f "$TEST_ROOT/$relative" ]; then
    echo "Install smoke test missing: $relative"
    exit 1
  fi
done

if python3 "$TEST_ROOT/scripts/validate-config.py" --strict; then
  echo "Fresh placeholder configuration unexpectedly passed validation."
  exit 1
else
  status=$?
  if [ "$status" -ne 2 ]; then
    echo "Fresh configuration returned unexpected status: $status"
    exit 1
  fi
fi

printf '\nSMOKE_SENTINEL\n' >> "$TEST_ROOT/config/product-context.md"
bash "$TEST_ROOT/scripts/setup.sh"

if ! grep -q "SMOKE_SENTINEL" "$TEST_ROOT/config/product-context.md"; then
  echo "Repeated setup overwrote existing configuration."
  exit 1
fi

echo "FORGE Lite install smoke test passed"
