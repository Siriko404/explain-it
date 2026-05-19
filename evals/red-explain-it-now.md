# RED — skills/explain-it-now baseline (no skill, sonnet subagent)

Scenario: eval-03 query "i did not understand a FUCKING WORD of that.
what is a tax shield". Fresh sonnet agent, NO skill loaded.

## Baseline behavior (verbatim self-report)

| eval-03 expected_behavior | Baseline (no skill) | Result |
|---|---|---|
| Zero ceremony / no preamble | 0 preamble sentences | pass |
| Concrete example first | yes (after 1-line def) | pass |
| Few concepts (not a spiral) | 2 concepts | pass |
| Short (~urgent) | ~175 words | pass |
| One non-prose visual | yes (boxed formula) | pass |
| Comprehension/context check | yes | pass |

## Conclusion

The unguided default is ALREADY strong for an explicitly frustrated,
urgent query — consistent with teacher-mode v1.1's origin. RED here is
a regression guardrail, not a gap: explain-it-now's job is to LOCK this
behavior as an enforced rule (so it is reliable, not luck) and prevent
drift toward the explain-it spiral (see red-explain-it.md, 5 concepts).
GREEN must codify: no ceremony, one concept, concrete-first, one visual,
≤5 prose sentences, one end check — and explicitly forbid ceremony.

## GREEN (with skill, fresh sonnet subagent reading the files)

Same eval-03 frustrated query, WITH skills/explain-it-now/SKILL.md +
references/:

| eval-03 expected_behavior | GREEN (skill) |
|---|---|
| Zero ceremony / no scope/plan gate | YES |
| 0 preamble sentences | YES (0) |
| Concrete example first | YES |
| Exactly one concept | YES (1) |
| One non-prose visual (catalog) | YES (pattern 3) |
| Prose sentences ≤5 | YES (~3–4) |
| One end comprehension check | YES ("Got it? Yes/No") |
| No tree / no persistence | YES |
| No regression toward ceremony/spiral | YES (no WACC/cap-structure spiral) |

9/9. The skill locked the strong baseline as an enforced rule (now
reliable, not luck) and showed no drift toward the explain-it spiral.
No new loophole → no REFACTOR required.

