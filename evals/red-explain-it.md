# RED — skills/explain-it baseline (no skill, sonnet subagent)

Scenario: eval-01 query "Teach me what difference-in-differences is.
I'm not familiar with it." Fresh sonnet agent, NO skill loaded.

## Baseline behavior (verbatim self-report)

| eval-01 expected_behavior | Baseline (no skill) | Result |
|---|---|---|
| P1 scope interview before teaching | "no" — explained immediately | FAIL |
| P2/P3 plan + approval before teaching | "no" | FAIL |
| One concept per message (Rule 1) | **5 concepts in one response** | FAIL (spiral) |
| MOC "you are here" tracking | "no" | FAIL |
| Concrete example first | yes (by default) | pass |
| No over-teaching past approved path | 5 concepts, no path | FAIL |

## Conclusion

Without the skill the agent over-teaches (5 ideas at once), runs no
scope interview, designs no plan, tracks nothing — exactly the
"over-teaching, spiralling, diverging, loses track" failure the spec
targets. RED established: 5/6 measured behaviors fail. GREEN must force
scope → plan-gate → one-concept tree-walk → MOC tracking.

## GREEN (with skill, fresh sonnet subagent reading the files)

Same eval-01 query, WITH skills/explain-it/SKILL.md + references/:

| eval-01 turn-1 behavior | RED (no skill) | GREEN (skill) |
|---|---|---|
| P0 recon skipped (general concept) | n/a | YES, correct |
| P1 scope interview, questions only | no | YES |
| Concepts taught in turn 1 | 5 | 0 |
| Spiral prevented | no | YES |
| Branch/rework/MOC deferred to P4 (not pre-taught) | n/a | YES, correct |

RED→GREEN delta is decisive: 5 concepts → 0; no scope → 4-question
scope interview. The skill changed behavior exactly as intended. No new
rationalization/loophole observed → no REFACTOR required.

