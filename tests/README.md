# Explain-it v2 — Test Scenarios

Six pressure scenarios derived from real v1.1 baseline failures (wild-transcript T01, 2026-05-19) and the painpoint list that motivated v2. The skill must pass all six.

Each test file specifies:

- The user simulation (what a learner does to trigger the scenario)
- The v1.1 baseline failure (what went wrong in real use)
- The v2 pass criterion (what compliant behavior looks like)
- The rule(s) under test (from `skills/explain-it/SKILL.md`)

| TC | Name | Rule under test | Maps to painpoint |
|---|---|---|---|
| TC1 | advance-on-confirm | Rule 3 | #18 |
| TC2 | no-overstay | Rule 3 | #19 |
| TC3 | big-picture-first | Rule 2 | #20 |
| TC4 | confusion-spawns-branch | Rule 4 | #21 |
| TC5 | pre-teach-plan-gate | Rule 1 | #7 + #8 |
| TC6 | spec-request-branch | Rule 4 | painpoint #6 |

## How to run

Manual: invoke `/explain-it <concept>` or `/explain-it-now <concept>` in a fresh Claude Code session, then play the user role described in each TC file. Verify each pass criterion.

Automated: dispatch a Claude subagent with each TC file as the input scenario and ask it to play the learner role; have the parent agent score the v2 transcript against the pass criterion.

## A note on example transcripts

Example transcripts inside individual TC files (e.g., `"Closing Node 1.1. Back to plan — Node 2: the CAPM equation."` in TC6) illustrate richer wording a teacher might use in practice. The normative spec template lives in `skills/explain-it/SKILL.md` Rule 4: *"Closing Node N.k. Back to Node N+1."* Both are compliant — the TC examples just substitute the actual node title for readability.

## A note on gate format

TC user simulations often show the learner typing a free-form reply in chat (e.g., *"Yes, got it"* in TC1, *"I don't really understand"* in TC4). At runtime, the canonical gate is `AskUserQuestion` with 4 chunk-tailored options (see `SKILL.md` Rule 3). The user can either select an option from the gate or type free-form in chat — both must trigger the same downstream behavior. Free-form chat replies that match an affirmative token (per Rule 3) count as Yes; replies expressing confusion or specification requests count as the corresponding gate option. Tests assess the downstream behavior, not the input modality.
