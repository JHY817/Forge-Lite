#!/usr/bin/env python3
"""Validate deterministic FORGE Lite framework structure."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.template.md",
    "workflows/runtime-state.md",
    "workflows/context-and-evidence.md",
    "workflows/approval-and-parallelism.md",
    "rubrics/issue-severity.md",
    "rubrics/reverse-engineering-quality.md",
    "rubrics/prototype-output-quality.md",
    "rubrics/prd-quality.md",
    "modules/prd-generation.md",
    "templates/prd.md",
    "templates/current-state.md",
    "templates/stage-handoff.md",
    "docs/rule-ownership.md",
    "evals/README.md",
    "evals/scoring.md",
    "evals/cases/generic-regression-cases.md",
]


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing: {relative}")

    state = (ROOT / "workflows/runtime-state.md").read_text(encoding="utf-8")
    for name in ["not_started", "in_progress", "agent_review_failed", "agent_review_passed", "waiting_user_confirmation", "confirmed", "blocked", "superseded", "completed"]:
        if name not in state:
            errors.append(f"runtime state missing: {name}")

    for relative in ["rubrics/reverse-engineering-quality.md", "rubrics/prototype-output-quality.md"]:
        text = (ROOT / relative).read_text(encoding="utf-8")
        for heading in ["## 适用条件", "## 不适用条件", "## 检查项", "## 达标规则"]:
            if heading not in text:
                errors.append(f"{relative} missing heading: {heading}")

    cases = (ROOT / "evals/cases/generic-regression-cases.md").read_text(encoding="utf-8")
    if cases.count("EVAL-") < 10:
        errors.append("fewer than 10 generic regression cases")

    diagram_rule_files = {
        "modules/prd-generation.md": ["文档配图与平台写回", "lark-whiteboard", "实际预览"],
        "rubrics/prd-quality.md": ["图文协同与在线文档写回", "条件必过项"],
        "templates/prd.md": ["配图并写回在线文档"],
        "evals/cases/generic-regression-cases.md": ["EVAL-011"],
    }
    for relative, phrases in diagram_rule_files.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"diagram writeback rule disconnected: {relative} missing {phrase}")

    agents = (ROOT / "AGENTS.template.md").read_text(encoding="utf-8")
    for reference in ["runtime-state.md", "context-and-evidence.md", "approval-and-parallelism.md"]:
        if reference not in agents:
            errors.append(f"AGENTS template missing reference: {reference}")

    if errors:
        print("FORGE Lite validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("FORGE Lite validation passed")
    print(f"required files: {len(REQUIRED)}")
    print("runtime states: complete")
    print("quality rubrics: structured")
    print("generic regression cases: >= 10")
    print("PRD diagram writeback: rule chain complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
