---
description: Teach a concept using Explain-it (full ceremony — scope interview, plan-approval gate, tree walk with confirm/branch protocol)
argument-hint: <concept>
---

Invoke the `explain-it` skill via the Skill tool. Concept to teach: $ARGUMENTS

Use ceremony mode — read `skills/explain-it/modes/ceremony.md` and follow it verbatim.

Required phases in order:

1. Scope interview (Phase 1) — seed question + optional baseline check
2. Reason about complexity → emit plan tree (Phase 2)
3. Plan-approval gate via AskUserQuestion (Phase 3) — do NOT skip
4. Tree walk (Phase 4) — one chunk per node, big-picture first, advance on "yes", spawn child sub-branch on "no" or specification request
5. Synthesis chunk (Phase 5) — integrate all nodes with one visual

Honor the session-budget guard (15 chunks max). Honor the 5 core rules in `SKILL.md`. Use a different visualization pattern from `references/visuals.md` on every consecutive chunk.
