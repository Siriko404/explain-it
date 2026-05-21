# TC5 — Pre-Teach Plan + Approval Gate

**Rule under test:** Rule 1 — *Tree before chunks.*
**Maps to painpoints:** #7 (pre-teach reasoning), #8 (complexity → 1/3/5 path).

## User simulation

Learner invokes `/explain-it perpetuity terminal value`.

## v1.1 baseline failure

Skill jumped directly into chunk 1 of the explanation with no prior planning step. No tree was emitted, no complexity classification, no user approval of the path. As a result the lesson diverged and spiralled (painpoints #3, #4) because there was no contract to walk against.

## v2 pass criterion

Before any teaching chunk, the skill MUST:

1. **Phase 1 (scope interview)** — ask the seed question or, if the learner has already framed scope in their initial message, state the assumption inline (*"Assuming you want the [A/B/C] angle — correct if wrong."*).
2. **Phase 2 (plan tree)** — classify complexity into 1, 3, or 5 nodes, and emit the plan as an ASCII tree with short node titles.
3. **Phase 3 (approval gate)** — fire `AskUserQuestion` with options *"Approve as drawn (Recommended)"* / *"Amend (specify what to change)"*.
4. NOT emit any Node 1 chunk until the user has approved or amended-and-approved.

## Verdict

- **PASS** if all three phases fire before the first teaching chunk.
- **FAIL** if any phase is skipped, especially the approval gate (the determinism contract).
- **PASS in express mode (`/explain-it-now`):** Phase 1 and Phase 3 are skipped, but Phase 2's one-sentence shape statement is still required (e.g., *"Quick walk: 3 nodes — setup, mechanism, consequence."*).
