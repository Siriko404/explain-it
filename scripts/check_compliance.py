#!/usr/bin/env python3
"""Anthropic Agent-Skills compliance verifier for the Explain-it package.

Checks (deterministic, from platform.claude.com skill best-practices):
  - SKILL.md frontmatter: name lowercase/digits/hyphen, <=64 chars,
    no reserved words; description non-empty, <=1024 chars, no XML tags
  - each SKILL.md body <=500 lines
  - reference files >100 lines have a "## Contents" / "## Table of Contents"
  - no backslash paths in markdown link targets
Exit 0 = all pass; exit 1 = any failure (failures printed).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESERVED = ("anthropic", "claude")
failures = []


def parse_frontmatter(text, path):
    if not text.startswith("---"):
        failures.append(f"{path}: missing YAML frontmatter")
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        failures.append(f"{path}: unterminated frontmatter")
        return {}
    fm = {}
    for line in text[3:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm


def check_skill(path):
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text, path)
    name = fm.get("name", "")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        failures.append(f"{path}: name '{name}' must be lowercase/digit/hyphen, <=64")
    if any(r in name for r in RESERVED):
        failures.append(f"{path}: name '{name}' contains a reserved word")
    desc = fm.get("description", "")
    if not desc:
        failures.append(f"{path}: empty description")
    if len(desc) > 1024:
        failures.append(f"{path}: description {len(desc)} chars > 1024")
    if "<" in desc and ">" in desc:
        failures.append(f"{path}: description appears to contain XML tags")
    n_lines = len(text.splitlines())
    if n_lines > 500:
        failures.append(f"{path}: body {n_lines} lines > 500")
    if "\\" in "".join(re.findall(r"\]\(([^)]+)\)", text)):
        failures.append(f"{path}: backslash in a markdown link path")


def check_reference(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) > 100:
        head = "\n".join(lines[:15]).lower()
        if "## contents" not in head and "## table of contents" not in head:
            failures.append(f"{path}: >100 lines but no Contents ToC in first 15 lines")


def main():
    skills = list(ROOT.glob("skills/*/SKILL.md"))
    if len(skills) != 2:
        failures.append(f"expected 2 SKILL.md files, found {len(skills)}")
    for s in skills:
        check_skill(s)
    for r in ROOT.glob("references/*.md"):
        check_reference(r)
    if failures:
        print("COMPLIANCE: FAIL")
        for f in failures:
            print("  -", f)
        sys.exit(1)
    print("COMPLIANCE: PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
