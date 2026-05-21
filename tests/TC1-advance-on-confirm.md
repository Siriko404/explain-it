# TC1 — Advance on Confirm

**Rule under test:** Rule 3 — *Advance only on confirm; never overstay.*
**Maps to painpoint:** #18 (v1.1 wild-transcript T01).

## User simulation

Learner invokes `/explain-it difference-in-differences`.
After the plan-approval gate (Phase 3), learner approves the 3-node plan.
After Node 1's chunk, learner replies: **"Yes, got it."**

## v1.1 baseline failure

Skill kept emitting more material on Node 1 — variations, examples, deeper sub-points — instead of moving to Node 2. The plan was rendered as 3 nodes, but the execution contract did not enforce node advancement on user confirmation.

## v2 pass criterion

On receiving "Yes, got it" (or the user selecting the *"Yes — advance to Node 2 (Recommended)"* option from the AskUserQuestion gate — both count per `SKILL.md` Rule 3 affirmative-tokens chat fallback), the skill MUST:

1. Stop emitting Node 1 material immediately.
2. Open Node 2 with the same chunk contract (big-picture, ≤5 sentences, one visual, different pattern from Node 1's chunk).
3. NOT include any Node 1 recap, summary, or "before we move on..." preamble.
4. End Node 2's chunk by firing the `AskUserQuestion` stop-and-check gate per `SKILL.md` Rule 3 — 4 chunk-tailored options: *"Yes — advance to Node 3 (Recommended)"* / *"No — `<predicted-confusion>`"* / *"Branch deeper — `<predicted-focus>`"* / *"Other / specify"*. The predicted confusion/focus text must be specific to Node 2's chunk content, not generic.

## Verdict

- **PASS** if Node 2's big-picture chunk is emitted on the turn immediately after the user's "Yes".
- **FAIL** if any Node-1-only material appears after the user's "Yes" before Node 2 begins.
