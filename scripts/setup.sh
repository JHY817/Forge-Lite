#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONFIG_EXAMPLE_DIR="$ROOT_DIR/config.example"
CONFIG_DIR="$ROOT_DIR/config"
AGENTS_TEMPLATE="$ROOT_DIR/AGENTS.template.md"
AGENTS_FILE="$ROOT_DIR/AGENTS.md"

if [ -d "$CONFIG_DIR" ]; then
  echo "config/ already exists. Config files were not overwritten."
else
  cp -R "$CONFIG_EXAMPLE_DIR" "$CONFIG_DIR"

  if [ -f "$CONFIG_DIR/product-context.example.md" ]; then
    mv "$CONFIG_DIR/product-context.example.md" "$CONFIG_DIR/product-context.md"
  fi

  if [ -f "$CONFIG_DIR/knowledge-base.example.yaml" ]; then
    mv "$CONFIG_DIR/knowledge-base.example.yaml" "$CONFIG_DIR/knowledge-base.yaml"
  fi

  if [ -f "$CONFIG_DIR/codebase.example.yaml" ]; then
    mv "$CONFIG_DIR/codebase.example.yaml" "$CONFIG_DIR/codebase.yaml"
  fi

if [ -f "$CONFIG_DIR/rubric.example.yaml" ]; then
  mv "$CONFIG_DIR/rubric.example.yaml" "$CONFIG_DIR/rubric.yaml"
fi

  if [ -f "$CONFIG_DIR/templates.example.yaml" ]; then
    mv "$CONFIG_DIR/templates.example.yaml" "$CONFIG_DIR/templates.yaml"
  fi

  echo "Created config/ from config.example/."
fi

if [ -f "$AGENTS_FILE" ]; then
  echo "AGENTS.md already exists. It was not overwritten."
else
  cp "$AGENTS_TEMPLATE" "$AGENTS_FILE"
  echo "Created AGENTS.md from AGENTS.template.md."
fi

echo "Next: edit config/product-context.md, config/knowledge-base.yaml, config/codebase.yaml, config/rubric.yaml, and config/templates.yaml."
