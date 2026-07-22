#!/usr/bin/env python3
"""Validate deterministic FORGE Lite framework structure."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.template.md",
    "README.md",
    "QUICKSTART.md",
    "PROJECT_INDEX.md",
    "workflows/runtime-state.md",
    "workflows/context-and-evidence.md",
    "workflows/approval-and-parallelism.md",
    "rubrics/issue-severity.md",
    "rubrics/reverse-engineering-quality.md",
    "rubrics/prototype-output-quality.md",
    "rubrics/prd-quality.md",
    "rubrics/diagram-visual-quality.md",
    "modules/prd-generation.md",
    "templates/prd.md",
    "templates/current-state.md",
    "templates/stage-handoff.md",
    "templates/diagram-brief.md",
    "docs/rule-ownership.md",
    "evals/README.md",
    "evals/scoring.md",
    "evals/cases/generic-regression-cases.md",
    "scripts/validate-config.py",
    "scripts/smoke-test-install.sh",
    ".github/workflows/validate.yml",
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
    if cases.count("EVAL-") < 12:
        errors.append("fewer than 12 generic regression cases")

    diagram_rule_files = {
        "modules/prd-generation.md": ["文档配图与平台写回", "fireworks-tech-graph", "lark-whiteboard", "diagram-visual-quality.md"],
        "rubrics/prd-quality.md": ["图文协同与在线文档写回", "条件必过项", "diagram-visual-quality.md"],
        "rubrics/diagram-visual-quality.md": ["5 秒内", "PNG 预览", "不得静默降级"],
        "templates/diagram-brief.md": ["一句话核心结论", "首选生成工具", "事实边界"],
        "templates/prd.md": ["写回在线文档"],
        "evals/cases/generic-regression-cases.md": ["EVAL-011", "高保真 Skill 已可用但未触发"],
    }
    for relative, phrases in diagram_rule_files.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"diagram writeback rule disconnected: {relative} missing {phrase}")

    configuration_rule_files = {
        "AGENTS.template.md": ["配置门禁", "validate-config.py", "配置引导"],
        "README.md": ["配置与阶段检查", "validate-config.py"],
        "QUICKSTART.md": ["配置不完整时", "validate-config.py"],
        "evals/cases/generic-regression-cases.md": ["EVAL-012"],
    }
    for relative, phrases in configuration_rule_files.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"configuration gate disconnected: {relative} missing {phrase}")

    markdown_link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in markdown_link.findall(text):
            target = raw_target.strip().strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative_target = unquote(target.split("#", 1)[0])
            if relative_target and not (path.parent / relative_target).resolve().exists():
                errors.append(
                    f"broken Markdown link: {path.relative_to(ROOT)} -> {relative_target}"
                )

    index = (ROOT / "PROJECT_INDEX.md").read_text(encoding="utf-8")
    for target in re.findall(r"`([^`]+\.(?:md|yaml|sh|py))`", index):
        if target in {"AGENTS.md"} or target.startswith("config/"):
            continue
        if not (ROOT / target).exists():
            errors.append(f"PROJECT_INDEX references missing file: {target}")

    prd_template = (ROOT / "templates/prd.md").read_text(encoding="utf-8")
    forbidden_template_markers = [
        ".feishu.cn/",
        "kms.",
        "<cite",
        "设计委员会",
        "团队评审",
        "帆软",
    ]
    for marker in forbidden_template_markers:
        if marker.lower() in prd_template.lower():
            errors.append(f"public PRD template contains private marker: {marker}")

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
    print("generic regression cases: >= 12")
    print("PRD high-fidelity diagram writeback: rule chain complete")
    print("configuration gate: rule chain complete")
    print("Markdown links and public template: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
