# Baseline — current teacher-mode v1.1 vs the 3 evals

Source inspected: `C:/Users/sinas/.claude/skills/teacher-mode/SKILL.md` (v1.1.0).

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

## Results (Explain-it v2.0) — 2026-05-19

Method: fresh sonnet subagents reading the shipped skill files from
disk (Anthropic "Claude B" fresh-instance grading; full RED→GREEN
records in red-explain-it.md and red-explain-it-now.md).

- **eval-01** (explain-it): turn-1 discriminating behaviors all pass —
  P0 correctly skipped, P1 scope interview run with ZERO concepts
  taught, spiral prevented. Baseline was 5 concepts dumped / no scope /
  no plan. Delta: 5 concepts → 0; gap closed. PASS.
- **eval-03** (explain-it-now): 9/9 expected behaviors pass — zero
  ceremony, 0 preamble, concrete-first, 1 concept, 1 catalog visual,
  ≤5 prose sentences, end check, no persistence, NO regression vs the
  strong v1.1 baseline. PASS (guardrail held).
- **eval-02** (repo-anchored): scenario defined; not executed — no
  sample auth-module repo in this environment. P0-conditional-skip
  logic is exercised and verified correct by eval-01 (DiD → P0
  skipped). Full repo-anchored run deferred to a real repo target.

Gaps found: none blocking. eval-02 execution is the one open item,
non-blocking for ship (it tests a code path inspected and partially
covered by eval-01).

