#!/usr/bin/env python3
"""Validate local FORGE Lite onboarding configuration."""

from pathlib import Path
import argparse
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config"
PLACEHOLDER = re.compile(r"<[^>\n]+>")


def read(relative: str, errors: list[str]) -> str:
    path = CONFIG / relative
    if not path.is_file():
        errors.append(f"missing required config file: config/{relative}")
        return ""
    return path.read_text(encoding="utf-8")


def read_optional(relative: str, warnings: list[str]) -> str:
    path = CONFIG / relative
    if not path.is_file():
        warnings.append(f"optional config file is missing: config/{relative}")
        return ""
    return path.read_text(encoding="utf-8")


def configured_sources(text: str) -> list[str]:
    values: list[str] = []
    for match in re.finditer(r"^\s*(?:path|url):\s*[\"']?([^\"'\n]+)", text, re.MULTILINE):
        value = match.group(1).strip()
        if value and not PLACEHOLDER.search(value):
            values.append(value)
    return values


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate local FORGE Lite onboarding configuration."
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return exit code 2 when required configuration is incomplete.",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    if not CONFIG.is_dir():
        print("CONFIG_STATUS=needs_configuration")
        print("FORGE Lite configuration is not initialized.")
        print("Run: bash scripts/setup.sh")
        return 2 if args.strict else 0

    product = read("product-context.md", errors)
    knowledge = read("knowledge-base.yaml", errors)
    codebase = read_optional("codebase.yaml", warnings)
    rubric = read_optional("rubric.yaml", warnings)
    templates = read("templates.yaml", errors)

    product_placeholders = sorted(set(PLACEHOLDER.findall(product)))
    if product_placeholders:
        errors.append(
            "config/product-context.md still contains placeholders: "
            + ", ".join(product_placeholders)
        )

    sources = configured_sources(knowledge)
    if not sources:
        errors.append(
            "config/knowledge-base.yaml needs at least one non-placeholder path or URL"
        )

    codebase_placeholders = sorted(set(PLACEHOLDER.findall(codebase)))
    if codebase_placeholders:
        warnings.append(
            "codebase is not configured; reverse engineering must be skipped until needed"
        )

    rubric_placeholders = sorted(set(PLACEHOLDER.findall(rubric)))
    if rubric_placeholders:
        warnings.append(
            "private Rubric extensions are not configured; only public generic Rubrics are available"
        )

    for match in re.finditer(r"^\s*path:\s*[\"']?([^\"'\n]+)", templates, re.MULTILINE):
        value = match.group(1).strip()
        if PLACEHOLDER.search(value):
            errors.append(f"config/templates.yaml contains placeholder path: {value}")
            continue
        target = (ROOT / value).resolve()
        if not target.is_file():
            errors.append(f"configured template does not exist: {value}")

    if errors:
        print("CONFIG_STATUS=needs_configuration")
        print("FORGE Lite configuration needs attention:")
        for error in errors:
            print(f"- REQUIRED: {error}")
        for warning in warnings:
            print(f"- OPTIONAL: {warning}")
        print("Complete required items before product design or PRD generation.")
        return 2 if args.strict else 0

    print("CONFIG_STATUS=ready")
    print("FORGE Lite required configuration is ready")
    print(f"configured knowledge sources: {len(sources)}")
    for warning in warnings:
        print(f"- OPTIONAL: {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
