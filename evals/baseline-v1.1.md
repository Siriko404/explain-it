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
