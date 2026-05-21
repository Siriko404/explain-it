# TC4 — Confusion Spawns Child Sub-Branch

**Rule under test:** Rule 4 — *Confusion → spawn child sub-branch* (replaces v1.1 Rule 6 "rework in place").
**Maps to painpoint:** #21.

## User simulation

Learner invokes `/explain-it endogeneity`.
Plan approved as 3 nodes.
After Node 1's chunk, learner replies: **"I don't really understand."**

## v1.1 baseline failure

Skill rephrased Node 1 in place — different words, same scope, same depth — then asked "got it now?" again. No tree operation was performed; the lesson had no record of what part confused the learner. If confusion recurred, the loop repeated without structural progress.

## v2 pass criterion

On "I don't understand" (or any explicit confusion signal), the skill MUST:

1. Acknowledge the confusion in one short line (no apology spiral).
2. Open an explicit child sub-branch — declared by name, e.g., *"Opening Node 1.1 — same idea, simpler scope: just the intuition without the math."*
3. Emit the child's big-picture chunk under the same chunk contract (≤5 sentences, one visual, different visual pattern from Node 1's chunk).
4. Stop-and-check after the child chunk.
5. On the child's "yes", return explicitly to the parent's NEXT sibling node (Node 2), not the parent again.

## Verdict

- **PASS** if the skill explicitly names and opens a Node 1.1 child branch on the confusion signal.
- **FAIL** if the skill rephrases Node 1 in place without spawning a named child, or fails to return to Node 2 after the child resolves.
