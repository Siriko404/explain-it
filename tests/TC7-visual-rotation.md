# TC7 — Visual Pattern Rotation

**Rule under test:** Rule 5 — *Visual scaffold mandatory + rotate patterns.*
**Maps to painpoint:** v1.1 FINANCE-project DCF tutorial — five consecutive vertical flow diagrams triggered engagement collapse ("messing the shit at me"); rotation requirement added in v2.

## User simulation

Learner invokes `/explain-it WACC`.
Plan approved as 3 nodes: `[Node 1: components | Node 2: formula | Node 3: when it breaks]`.
Learner advances on every gate (selects *"Yes — advance to Node N+1"* each time, no branches).

## v1.1 baseline failure

v1.1 had Rule 8 mandate visuals but no rotation requirement. A multi-node walk could (and did) use the same visual pattern (e.g., vertical flow diagram) on every node, causing the visual scaffold to recede into background noise rather than reinforce structure.

## v2 pass criterion

Across Node 1's chunk, Node 2's chunk, and Node 3's chunk, the skill MUST:

1. Emit at least one non-prose visual element per chunk (Rule 5 mandatory clause).
2. Use a **different visual pattern** on each chunk vs the previous chunk (Rule 5 rotation clause).
3. Draw the patterns from `references/visuals.md` 9-pattern catalog (vertical flow, branch tree, side-by-side boxes, comparison table, timeline, boxed identity, causal-arrow chain, stacked-block ratio, decision tree) — OR a clearly-distinct formatting variant of one already-used pattern if the lesson genuinely demands the same logical pattern twice.
4. Phase 5 synthesis chunk's integrating visual also follows the rotation rule — its pattern must differ from Node 3's chunk pattern.

For WACC specifically, a passing 3-node walk might use:
- **Node 1 (components)** — Stacked-block ratio (pattern 8) showing equity/debt split with cost annotations
- **Node 2 (formula)** — Boxed identity (pattern 6) showing `WACC = wE·rE + wD·rD·(1−t)`
- **Node 3 (when it breaks)** — Comparison table (pattern 4) showing valid-WACC vs broken-WACC scenarios
- **Phase 5 synthesis** — Vertical flow diagram (pattern 1) showing capital structure → cost ingredients → blended rate → discounting

Each adjacent pair uses a different pattern. Pass.

## Verdict

- **PASS** if no two adjacent chunks (Node N's chunk + Node N+1's chunk, OR Node N's chunk + Node N.1 child chunk, OR Node 3's chunk + Phase 5 synthesis) share the same visual pattern.
- **PASS** if a logically-forced repeat uses a clearly-distinct formatting variant (different orientation, annotation, or side-element) AND the repeat is acknowledged inline (*"Same pattern, different angle — ..."*).
- **FAIL** if any two adjacent chunks use the same visual pattern without an acknowledged variant adjustment.
- **FAIL** if any chunk emits prose-only with no visual element (Rule 5 mandatory-clause violation, distinct from the rotation-clause failure).
