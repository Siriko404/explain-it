---
description: Teach a concept urgently using Explain-it (express — skip scope interview and plan gate, single-pass tree walk, max 5 chunks)
argument-hint: <concept>
---

Invoke the `explain-it` skill via the Skill tool. Concept to teach: $ARGUMENTS

Use express mode — read `skills/explain-it/modes/express.md` and follow it verbatim.

Required behavior:

1. State the tree shape in one sentence (e.g., *"Quick walk: 3 nodes — setup, mechanism, consequence. Going."*) — no scope interview, no approval gate
2. Walk the tree — one chunk per node, big-picture first, ≤5 prose sentences + one visual element each
3. Advance on "yes". Spawn child sub-branch on "no" or specification request. Same chunk contract applies in branches.
4. Stop at ≤5 chunks unless user explicitly extends

Express mode is a contract about gates (skip them), NOT a license to compress the chunk-per-node rule. The 5 core rules in `SKILL.md` still apply.

If the concept is too broad for ≤5 chunks (e.g., "explain the entire CFA Level 1 curriculum"), refuse express in one line and recommend `/explain-it` instead.
