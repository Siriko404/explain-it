# TC3 — Big-Picture First

**Rule under test:** Rule 2 — *One chunk per node; big-picture first.*
**Maps to painpoint:** #20.

## User simulation

Learner invokes `/explain-it WACC`.
Plan approved as 3 nodes: `[Node 1: components | Node 2: formula | Node 3: when it breaks]`.
Skill begins Node 1.

## v1.1 baseline failure

The first chunk for Node 1 went straight into a sub-detail (e.g., "Equity cost is computed via CAPM, where beta is...") without first establishing the big picture (e.g., "WACC has two ingredients — cost of equity and cost of debt, weighted by their share of capital."). The learner did not yet know what Node 1 was *about* before being shown how its sub-parts work.

## v2 pass criterion

Node 1's first chunk MUST deliver the BIG PICTURE of Node 1 — what it is, what it contains, why it matters in one breath — before any sub-detail. Constraints:

1. ≤5 sentences of prose
2. At least one non-prose visual element scaffolding the relationship between the node's parts
3. Zero unexplained jargon (define inline in plain words, or skip the term)
4. The sub-details (e.g., "CAPM specifics") belong in a child branch (Node 1.1), spawned only if the learner requests deeper focus

## Verdict

- **PASS** if Node 1's first chunk reads as an overview the learner could paraphrase without needing the sub-details.
- **FAIL** if the first chunk requires the learner to already know what Node 1 is about in order to follow it.
