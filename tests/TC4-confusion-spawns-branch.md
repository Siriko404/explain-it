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

On "I don't understand" (or the user selecting the gate's *"No — `<predicted-confusion>`"* option — both count), the skill MUST:

1. Acknowledge the confusion in one short line (no apology spiral).
2. Open an explicit child sub-branch — **verbal close-announcement mandatory** per `SKILL.md` Rule 4 — declared by name in the agent's output, e.g., *"Opening Node 1.1 — same idea, simpler scope: just the intuition without the math."* A silent branch (skill internally tracks Node 1.1 but does not emit the open-announcement to the user) does NOT count as compliance.
3. Emit the child's big-picture chunk under the same chunk contract (≤5 sentences, one visual, different visual pattern from Node 1's chunk).
4. Fire the `AskUserQuestion` stop-and-check gate after the child chunk (same 4-option schema, chunk-tailored to the child's content).
5. On the child's "yes", emit the **verbal close-announcement** *"Closing Node 1.1. Back to Node 2."* (or equivalent per Rule 4 template — N substitution required, "plan —" prefix optional). Then emit Node 2's chunk directly. A silent return without the close-announcement does NOT count as compliance.

## Verdict

- **PASS** if the skill (a) emits the verbal open-announcement naming Node 1.1, (b) walks the child chunk, (c) emits the verbal close-announcement naming the return target, and (d) opens Node 2's chunk.
- **FAIL** if the skill rephrases Node 1 in place without spawning a named child, OR spawns the child silently without the open-announcement, OR returns to Node 2 silently without the close-announcement.
