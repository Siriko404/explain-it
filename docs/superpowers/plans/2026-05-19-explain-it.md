# Explain-it v2.0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `explain-it` + `explain-it-now` — a two-skill GitHub package that adds a planned, user-approved, Zettelkasten-tree macro layer around the empirically-validated teacher-mode v1.1 10-rule micro-protocol.

**Architecture:** Two sibling Claude Code skills in one package. `explain-it` runs a 6-phase ceremony (recon → scope → complexity→1/3/5 path → plan-approval gate → tree-walk teaching → local-md persistence). `explain-it-now` skips ceremony for urgent/frustrated users (pure v1.1 behavior). Both reference a shared package-root `references/` holding one verbatim copy of the v1.1 core. Skeleton-not-script: tree topology is deterministic, per-node delivery stays adaptive.

**Tech Stack:** Markdown skill files (Anthropic Agent Skills format), Python 3 for the deterministic compliance verifier, git. No runtime dependencies for the skill itself.

**Spec:** `docs/superpowers/specs/2026-05-19-explain-it-design.md` (ratified, commit e31c6ed).
**v1.1 source for verbatim extraction:** `C:/Users/sinas/.claude/skills/teacher-mode/SKILL.md` (read in full; line ranges given per task).

---

## File Structure

| Path | Responsibility |
|---|---|
| `references/core-protocol.md` | The 10-rule protocol + frustration→rule correction matrix + anti-patterns, verbatim from v1.1. Single source of truth. |
| `references/visualization-catalog.md` | The 9 visual patterns, verbatim from v1.1. ToC at top. |
| `skills/explain-it/SKILL.md` | Full-ceremony skill. P0–P5. References the two `references/*`. |
| `skills/explain-it-now/SKILL.md` | Urgent skill. No ceremony. References the two `references/*`. |
| `evals/eval-01-novice-concept.md` | Behavioral eval: novice general concept via full ceremony. |
| `evals/eval-02-repo-anchored.md` | Behavioral eval: repo-anchored explanation. |
| `evals/eval-03-frustrated-recovery.md` | Behavioral eval: frustrated urgent recovery. |
| `evals/baseline-v1.1.md` | Recorded gaps when current v1.1 runs the 3 evals (the baseline to beat). |
| `scripts/check_compliance.py` | Deterministic Anthropic-compliance verifier (the automatable test harness). |
| `README.md` | Public-facing, brand "Explain-it", install + usage. |

Decomposition rationale: shared core lives once in `references/` (no duplication); each skill file is independently discoverable and stays under Anthropic's 500-line rule; the compliance script is the deterministic gate, evals are the behavioral gate.

---

## Task 1: Compliance verifier (the deterministic test harness)

Build the verifier FIRST so every later task can self-check. Anthropic best-practices: "Prefer scripts for deterministic operations."

**Files:**
- Create: `scripts/check_compliance.py`

- [ ] **Step 1: Write the verifier**

```python
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
```

- [ ] **Step 2: Run it to verify it FAILS (no skill files yet)**

Run: `python scripts/check_compliance.py`
Expected: `COMPLIANCE: FAIL` with `expected 2 SKILL.md files, found 0`, exit 1.

- [ ] **Step 3: Commit**

```bash
git add scripts/check_compliance.py
git commit -m "Add Anthropic skill-compliance verifier"
```

---

## Task 2: Eval scenarios + v1.1 baseline (eval-first mandate)

Anthropic: "Create evaluations BEFORE writing extensive documentation." Baseline = run the CURRENT v1.1 teacher-mode mentally/by inspection against each scenario and record the gap.

**Files:**
- Create: `evals/eval-01-novice-concept.md`
- Create: `evals/eval-02-repo-anchored.md`
- Create: `evals/eval-03-frustrated-recovery.md`
- Create: `evals/baseline-v1.1.md`

- [ ] **Step 1: Write eval-01**

````markdown
# eval-01 — novice general concept (full ceremony)

**Skill:** explain-it
**Query:** "Teach me what difference-in-differences is. I'm not familiar with it."
**Inputs:** none (general concept, no repo)

**expected_behavior:**
- P0 recon is SKIPPED (concept is not repo-anchored)
- P1 scope interview runs via AskUserQuestion (goal/depth/baseline), not prose
- P2 assigns complexity and an N-step path with N in {1,3,5}
- P3 presents the path and waits for explicit approval before teaching
- P4 teaches node-by-node using the 10-rule protocol; renders a MOC
  "you are here" anchor every turn
- A "give me an example" request spawns a CHILD node (branch), not a rework
- An "I don't understand" spawns a REWORK of the same node, no new material
- No spiral / no over-teaching past the approved path
- P5 writes the lesson tree to ./explain-it-vault/
````

- [ ] **Step 2: Write eval-02**

````markdown
# eval-02 — repo-anchored explanation (full ceremony)

**Skill:** explain-it
**Query:** "Explain how the auth module in this repo works."
**Inputs:** a small sample repo with an auth module

**expected_behavior:**
- P0 recon RUNS but is bounded to auth-relevant files only (not a
  full-codebase ingest)
- P1 scope interview confirms depth/audience
- P2/P3 path reflects the ACTUAL module structure found in P0
- P4 teaches with the 10-rule protocol; MOC anchor every turn
- P5 persists the tree as atomic notes with valid [[wikilinks]] + a MOC index
````

- [ ] **Step 3: Write eval-03**

````markdown
# eval-03 — frustrated urgent recovery (no ceremony)

**Skill:** explain-it-now
**Query:** "i did not understand a FUCKING WORD of that. what is a tax shield"
**Inputs:** none

**expected_behavior:**
- explain-it-now is selected (frustration triggers), NOT explain-it
- ZERO ceremony: no recon, no AskUserQuestion scope gate, no plan gate
- Immediate v1.1 behavior: concrete example first, plain words, one
  visual, <=5 prose sentences, stop-and-check
- No lesson tree, no persistence
- Fast (single turn to first teaching chunk)
````

- [ ] **Step 4: Record the v1.1 baseline**

Inspect `C:/Users/sinas/.claude/skills/teacher-mode/SKILL.md` against each eval and write the gap.

````markdown
# Baseline — current teacher-mode v1.1 vs the 3 evals

**eval-01:** v1.1 has Rule 9 baseline check but NO scope interview, NO
complexity→1/3/5 path, NO plan-approval gate, NO lesson tree, NO MOC
anchor, NO persistence, NO branch-vs-rework distinction. Fails 7/9
expected behaviors. This is the gap Explain-it closes.

**eval-02:** v1.1 has no recon phase at all; cannot anchor to a repo
module. Fails repo-bounded recon + persistence. 0/5.

**eval-03:** v1.1 ALREADY satisfies this — its origin is exactly
frustrated recovery. explain-it-now must preserve, not regress, this
behavior. Baseline here = PASS; the risk is regression, so eval-03 is a
guardrail not a gap.
````

- [ ] **Step 5: Run compliance (should still fail — no skills yet) and commit**

Run: `python scripts/check_compliance.py`
Expected: `COMPLIANCE: FAIL` (still `found 0` SKILL.md), exit 1.

```bash
git add evals/
git commit -m "Add 3 eval scenarios and record v1.1 baseline gaps"
```

---

## Task 3: references/core-protocol.md (verbatim v1.1 extraction)

Extract the proven core VERBATIM from v1.1. Do not redesign (spec D1). Source ranges in `C:/Users/sinas/.claude/skills/teacher-mode/SKILL.md`: 10-rule protocol (lines 71–135), verification matrix (247–266), anti-patterns (331–351).

**Files:**
- Create: `references/core-protocol.md`

- [ ] **Step 1: Write the file (ToC + verbatim blocks)**

The file MUST begin with this ToC (Anthropic rule for ref files >100 lines), then contain, verbatim, the v1.1 "## Solution — The 10-Rule Protocol" block (Rules 1–10), the "## Verification — Mode Working / Not Working" table, and the "## Anti-patterns to avoid" list, copied exactly from the source file lines above. Header to prepend:

```markdown
# Core Protocol (absorbed from teacher-mode v1.1, verbatim)

## Contents
- The 10-Rule Protocol (Rules 1–10)
- Verification matrix — signals → rule violation → corrective action
- Anti-patterns to avoid

> Source of truth. Both skills/explain-it and skills/explain-it-now
> obey these rules per teaching node. Empirically validated across two
> real-world amendments (v1.0 2026-04-29, v1.1 2026-05-05). Do not
> redesign — spec D1.
```

Then paste, unaltered, the three source blocks (Rules 1–10 with their full text; the Verification table with all 7 rows; the 6 Anti-patterns). Use the exact wording from the source — no paraphrase, no omission.

- [ ] **Step 2: Verify the verbatim copy**

Run: `python -c "import pathlib,sys; t=pathlib.Path('references/core-protocol.md').read_text(encoding='utf-8'); req=['One concept per message','Concrete example FIRST','Zero unexplained jargon','Max ~5 short sentences','Stop and check after each chunk','REWORK the same chunk simpler','One analogy per topic','Visual structure mandatory + diverse','Confirm baseline understanding BEFORE','multiple-choice clarifier']; miss=[r for r in req if r not in t]; print('MISSING:',miss) or sys.exit(1 if miss else 0)"`
Expected: `MISSING: []`, exit 0.

- [ ] **Step 3: Run compliance + commit**

Run: `python scripts/check_compliance.py`
Expected: still FAIL on missing SKILL.md, but NO reference-ToC failure for core-protocol.md.

```bash
git add references/core-protocol.md
git commit -m "Add references/core-protocol.md (v1.1 10-rule core, verbatim)"
```

---

## Task 4: references/visualization-catalog.md (verbatim v1.1 extraction)

Source: `C:/Users/sinas/.claude/skills/teacher-mode/SKILL.md` lines 137–245 ("## Visualization Catalog (Rule 8 reference)" through the "When in doubt, pick the pattern…" paragraph).

**Files:**
- Create: `references/visualization-catalog.md`

- [ ] **Step 1: Write the file**

Prepend this header + ToC, then paste the 9 patterns and the closing guidance paragraph VERBATIM from the source:

```markdown
# Visualization Catalog (absorbed from teacher-mode v1.1, verbatim)

## Contents
1. Vertical flow diagram — sequential transformation
2. Branch tree — one-to-many split
3. Side-by-side boxes — two methods, same answer
4. Compact comparison table — strength/weakness contrast
5. Timeline with vertical markers — forecast horizon
6. Boxed identity — the take-away formula isolated
7. Causal-arrow chain — propagation of effect
8. Stacked-block ratio — proportional split visual
9. Decision tree — yes/no branches with consequences

> Rule 8 reference. Rotate patterns; never repeat one style across
> consecutive chunks. Do not redesign — spec D1.
```

- [ ] **Step 2: Verify all 9 patterns present**

Run: `python -c "import pathlib,sys; t=pathlib.Path('references/visualization-catalog.md').read_text(encoding='utf-8'); req=['Vertical flow diagram','Branch tree','Side-by-side boxes','comparison table','Timeline with vertical markers','Boxed identity','Causal-arrow chain','Stacked-block ratio','Decision tree']; miss=[r for r in req if r not in t]; print('MISSING:',miss) or sys.exit(1 if miss else 0)"`
Expected: `MISSING: []`, exit 0.

- [ ] **Step 3: Run compliance + commit**

Run: `python scripts/check_compliance.py`
Expected: FAIL only on missing SKILL.md; no ToC failure for this file.

```bash
git add references/visualization-catalog.md
git commit -m "Add references/visualization-catalog.md (9 v1.1 patterns, verbatim)"
```

---

## Task 5: skills/explain-it/SKILL.md (full ceremony)

The core novel artifact. Implements spec §3, §5, §6, §8.

**Files:**
- Create: `skills/explain-it/SKILL.md`

- [ ] **Step 1: Write the file**

Write EXACTLY this content:

````markdown
---
name: explain-it
description: Structured, planned teaching of a technical concept to a non-expert. Use when the user invokes /explain-it, or asks to be taught or walked through a concept they do not know and the request is NOT urgent and NOT frustrated. Runs a scoped, user-approved Zettelkasten lesson tree (recon, scope interview, complexity-scaled 1/3/5-step path, plan-approval gate, tracked tree-walk, local persistence) wrapping a cognitive-load 10-rule delivery protocol. For urgent or frustrated "I don't understand" moments, the separate explain-it-now skill is used instead.
---

# Explain-it (full ceremony)

Teach ONE technical concept to a non-expert via a planned, tracked,
user-approved lesson tree. Skeleton-not-script: the tree topology is
deterministic and tracked; delivery within each node stays adaptive.

## Before anything: load the core

Read `references/core-protocol.md` (the 10-rule protocol + correction
matrix + anti-patterns) and `references/visualization-catalog.md` (9
visual patterns). Every teaching node obeys those rules. They are the
single source of truth — do not restate or redesign them here.

## When this skill applies / does not

Applies: explicit `/explain-it`; non-urgent learning intent ("teach me
X", "explain how Y works", "I'm not familiar with Z").
Does NOT apply: urgent or frustrated phrasing, caps, profanity, "I don't
understand", "too long" → that is the `explain-it-now` skill.

## Workflow — copy this checklist and track it

```
Explain-it progress:
- [ ] P0 Recon (conditional)
- [ ] P1 Scope interview
- [ ] P2 Complexity -> N-step path (N in {1,3,5})
- [ ] P3 Plan-approval gate
- [ ] P4 Teach (tree walk)
- [ ] P5 Persist
```

### P0 — Recon (conditional, bounded)

If the concept is repo/asset-anchored ("explain this module/file/repo"):
scan ONLY the files relevant to that concept. Do NOT ingest the whole
codebase. If it is a general concept (e.g. "difference-in-differences"),
SKIP P0 entirely.

### P1 — Scope interview

Use AskUserQuestion ONLY (never inline prose lists). Ask, in <=4
questions: learning goal/outcome, target depth, the user's current
baseline on prerequisites. This gates everything downstream — a wrong
scope wastes the whole session.

### P2 — Complexity -> path

Self-assess concept complexity and design an N-step path:
- N=1: atomic concept (one node). May skip P3.
- N=3: moderate (3 sequential nodes).
- N=5: complex (5 sequential nodes).
Each node = one concept (Rule 1). Calibrate to the user's stated
baseline (zone of proximal development).

### P3 — Plan-approval gate

Render the proposed path as a tree (see MOC format below) and ask, via
AskUserQuestion: approve / amend. Do NOT teach until approved when N>=3.
N=1 may proceed directly.

### P4 — Teach (skeleton-not-script tree walk)

Walk nodes in order. Deliver each node with the 10-rule protocol from
`references/core-protocol.md`, rotating visuals from
`references/visualization-catalog.md` (Rule 8 diversity).

Per-node state:
```
id: <parent.child>   title: <one concept>
status: pending|active|mastered|reworking
analogy: <the single analogy chosen>     # Rule 7
visual: <pattern used>                   # Rule 8 rotation
```

Mastery gate: do NOT advance to the next node until the current node's
comprehension is confirmed (stop-and-check, Rule 5).

Branch vs. rework — DISTINCT triggers, DISTINCT responses:
- "tell me more about X" / "give an example of Y" / "what about Z?"
  = SPECIFICATION REQUEST -> spawn a CHILD node under the current node
  with its own mini 1/3/5 path; teach it; return to the parent; update
  the MOC.
- "I don't understand" / "still lost" / "too hard"
  = CONFUSION -> REWORK the same node (Rule 6: simpler words/example,
  NO new material, NO branch). After 2 failed reworks, Rule 10
  multiple-choice clarifier.

MOC "you are here" anchor — render this EVERY teaching turn:
```
LESSON: <root concept>            [<m>/<n> nodes mastered]
  1. <state> <node1>
  2. <state> <node2>  <- you are here
     2.1 <state> <spec branch: ...>
  3. <state> <node3>
```
states: done = mastered, active = current, pending = not started,
reworking = in a rework loop.

Frustration mid-session: if the user becomes frustrated/urgent during
P4, DROP the ceremony and switch to pure 10-rule urgent behavior
in-place (same as explain-it-now). Do not restart, do not re-invoke a
skill. Resume the tree only if the user asks to continue.

### P5 — Persist

Write the lesson tree to a local Zettelkasten vault (default
`./explain-it-vault/`, configurable):
```
explain-it-vault/
  MOC-<root>.md            # index note, [[wikilinks]] to all nodes
  <root>/
    1-<node>.md            # one idea per note; frontmatter: id,title,
    2-<node>.md            #   parent, status, analogy, visual
    2.1-<spec-branch>.md
```
One idea per note; `[[wikilink]]` edges; MOC index = navigable, no
sprawl. Update on every node status change. (Obsidian MCP backend is a
deferred v2.1 enhancement; this markdown layout is already
Obsidian-native — no migration later.)

## Deactivation

User says "stop", "I know this", "normal mode" -> exit, leave the vault
in place.
````

- [ ] **Step 2: Run compliance**

Run: `python scripts/check_compliance.py`
Expected: still FAIL (only 1 of 2 SKILL.md present: `expected 2 SKILL.md files, found 1`), but NO failure attributable to `skills/explain-it/SKILL.md` (name valid, description ≤1024, body <500 lines).

- [ ] **Step 3: Commit**

```bash
git add skills/explain-it/SKILL.md
git commit -m "Add skills/explain-it/SKILL.md (full-ceremony workflow P0-P5)"
```

---

## Task 6: skills/explain-it-now/SKILL.md (urgent, no ceremony)

Implements spec §7. Preserves v1.1 behavior exactly — eval-03 is a regression guardrail.

**Files:**
- Create: `skills/explain-it-now/SKILL.md`

- [ ] **Step 1: Write the file**

Write EXACTLY this content:

````markdown
---
name: explain-it-now
description: Urgent, no-ceremony explanation of one technical concept. Use the moment a user is frustrated or in a hurry about not understanding something — triggers include "I don't understand", "I didn't understand a word", "too long", "too much jargon", "explain it now", caps-lock frustration, or profanity directed at a prior explanation. Delivers the cognitive-load 10-rule protocol immediately with no scope interview, no plan gate, and no lesson tree. For calm, planned, structured learning the separate explain-it skill is used instead.
---

# Explain-it-now (urgent, zero ceremony)

A frustrated or rushed user needs the concept NOW. No phases, no gates,
no tree, no persistence. This preserves the original teacher-mode v1.1
behavior — its whole reason for existing is frustrated recovery.

## Before anything: load the core

Read `references/core-protocol.md` and
`references/visualization-catalog.md`. Apply them directly.

## What to do

1. Optional ONE-LINE baseline check only if essential (Rule 9) — skip
   if it would delay relief.
2. Deliver immediately with the 10-rule protocol: concrete example
   FIRST (Rule 2), plain words / zero unexplained jargon (Rule 3), <=5
   prose sentences + ONE visual from the catalog (Rules 4 & 8),
   stop-and-check (Rule 5).
3. On "still don't get it": REWORK simpler (Rule 6), do not add
   material. After 2 failed reworks: Rule 10 multiple-choice clarifier.

## Do NOT

- Do NOT run a scope interview or any AskUserQuestion gate.
- Do NOT design a 1/3/5 path or ask for plan approval.
- Do NOT build or persist a lesson tree.

## Promotion

If the session balloons (>=3 reworks, OR the user asks for structured /
deeper / full coverage), say one line: suggest they re-invoke
`/explain-it` for the full planned path. Do not auto-switch.

## Deactivation

User says "stop" / "I know this" / "normal mode" -> exit.
````

- [ ] **Step 2: Run compliance (now expect PASS)**

Run: `python scripts/check_compliance.py`
Expected: `COMPLIANCE: PASS`, exit 0 (2 SKILL.md present, both valid, references have ToCs).

- [ ] **Step 3: Commit**

```bash
git add skills/explain-it-now/SKILL.md
git commit -m "Add skills/explain-it-now/SKILL.md (urgent, zero-ceremony)"
```

---

## Task 7: README.md (public brand)

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write the README**

````markdown
# Explain-it

Two Claude Code skills that teach you a technical concept properly.

- **`/explain-it <topic>`** — full ceremony. Scopes the session, scales
  a 1/3/5-step path to the concept's complexity, gets your approval,
  then teaches node-by-node as a tracked Zettelkasten lesson tree you
  never lose your place in, and saves it to a local markdown vault.
- **`/explain-it-now <topic>`** — zero ceremony. For when you're stuck
  and frustrated and need it explained *now*.

Both wrap a cognitive-load-grounded 10-rule delivery protocol
(one concept per message, concrete example first, zero unexplained
jargon, mandatory varied visuals, stop-and-check, rework-don't-add)
validated across real teaching sessions.

## Install

Copy `skills/explain-it/` and `skills/explain-it-now/`, plus the
`references/` directory, into your Claude Code skills location (the
`references/` directory must sit one level above the `skills/` dir as
shipped).

## Credits

Successor to the `teacher-mode` skill. Pedagogy grounded in Cognitive
Load Theory, Bloom mastery learning / ZPD, the Feynman technique,
Zettelkasten Maps of Content, and Google LearnLM's course-tutor
"negotiate a study plan then track it" pattern.
````

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "Add public README with brand and install instructions"
```

---

## Task 8: Behavioral eval run vs. baseline

Verify the package beats the recorded v1.1 baseline. Behavioral evals are run by a FRESH agent instance (Anthropic "Claude B"), not self-graded.

**Files:**
- Modify: `evals/baseline-v1.1.md` (append results section)

- [ ] **Step 1: Run eval-01 with a fresh subagent**

Dispatch a subagent with ONLY the `skills/explain-it/` + `references/`
loaded and the eval-01 query. Capture transcript.

- [ ] **Step 2: Run eval-03 with a fresh subagent**

Dispatch a subagent with ONLY `skills/explain-it-now/` + `references/`
and the eval-03 query. Capture transcript.

- [ ] **Step 3: Score against expected_behavior and append results**

For each eval, mark each `expected_behavior` bullet pass/fail from the
transcript. Append to `evals/baseline-v1.1.md`:

```markdown
## Results (Explain-it v2.0) — <date>
eval-01: <X>/9 expected behaviors pass (baseline was 2/9)
eval-03: <X>/<n> pass — MUST be no regression vs v1.1 baseline (PASS)
Gaps found: <list or "none">
```

If eval-01 < 8/9 or eval-03 regresses: STOP, fix the responsible skill
file, re-run. Do not proceed to ship.

- [ ] **Step 4: Commit**

```bash
git add evals/baseline-v1.1.md
git commit -m "Record Explain-it v2.0 eval results vs v1.1 baseline"
```

---

## Task 9: Retire teacher-mode locally + ship prep

Spec D2: self-contained successor. Update the global CLAUDE.md reference. This is a USER-FILE edit outside the repo — confirm with the user before editing `C:/Users/sinas/.claude/CLAUDE.md`.

**Files:**
- Modify: `C:/Users/sinas/.claude/CLAUDE.md` (teacher-mode → explain-it references) — **requires user confirmation (out-of-repo, behavior-changing)**

- [ ] **Step 1: Show the user the exact CLAUDE.md lines that reference teacher-mode and the proposed replacement; get explicit approval**

The CLAUDE.md "Teacher mode — MANDATORY AUTO-TRIGGER" section references
`/teacher-mode` and `~/.claude/skills/teacher-mode/SKILL.md`. Propose:
point auto-trigger at `explain-it-now` (the no-ceremony path is the
correct match for the frustration auto-triggers CLAUDE.md describes),
and add `/explain-it` for explicit planned teaching. Do NOT edit until
the user approves the exact diff.

- [ ] **Step 2: Apply the approved CLAUDE.md edit**

- [ ] **Step 3: Final compliance gate**

Run: `python scripts/check_compliance.py`
Expected: `COMPLIANCE: PASS`, exit 0.

- [ ] **Step 4: Final commit + optional GitHub**

```bash
git add -A
git commit -m "Retire teacher-mode locally; point CLAUDE.md at Explain-it"
```

Pushing to GitHub / creating the remote is a separate, user-initiated
step (do not auto-create remotes).

---

## Self-Review

**1. Spec coverage:**
- D1 skeleton-not-script → Task 5 P4 (deterministic tree, adaptive node). ✓
- D2 self-contained successor → Task 3/4 verbatim absorb; Task 9 retire. ✓
- D3 two entry points → Task 5 + Task 6. ✓
- D4 two skills/one package/shared refs → File Structure + Tasks 3–6. ✓
- D5 MVP cut → no Obsidian/quiz/rich-links tasks present. ✓
- D6 local-md persistence → Task 5 P5. ✓
- §5 node schema / MOC / branch-vs-rework → Task 5 P4 (all three explicit). ✓
- §6 P0–P5 → Task 5. §7 urgent → Task 6. §8 vault → Task 5 P5. ✓
- §9 absorbed core verbatim → Tasks 3 & 4 with source line ranges. ✓
- §11 evals + baseline → Task 2 (defined first) + Task 8 (run vs baseline). ✓
- §12 compliance checklist → Task 1 script enforces name/desc/line/ToC. ✓
- §14 build order → Tasks ordered exactly as specified. ✓

**2. Placeholder scan:** No "TBD/TODO/handle edge cases". Verbatim
extractions name the exact source file + line ranges (not a placeholder
— a precise instruction). Eval/skill file contents are given in full.

**3. Type/name consistency:** `scripts/check_compliance.py`,
`references/core-protocol.md`, `references/visualization-catalog.md`,
`skills/explain-it/SKILL.md`, `skills/explain-it-now/SKILL.md`,
`./explain-it-vault/` — used identically in every task and match the
spec. Skill `name:` values (`explain-it`, `explain-it-now`) are
lowercase/hyphen, reserved-word-free, enforced by Task 1.

No gaps found.
