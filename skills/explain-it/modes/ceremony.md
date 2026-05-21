# Explain-it — Ceremony Mode (`/explain-it`)

Loaded by `explain-it` SKILL.md when the user invokes `/explain-it <concept>` or activates explain-it via a trigger phrase with no urgency signal.

Follow this protocol verbatim. Do not skip steps.

## Phase 1 — Scope Interview

Before any planning, ask the learner ONE question (via `AskUserQuestion` when available, else plain prompt).

**Seed question** (borrowed from Khanmigo + vuciv tutoring patterns):

> "What part of `<concept>` do you understand least right now — A: the basic definition, B: how it works mechanically, C: when to use it / when not to, D: something else (specify)?"

You MAY skip the seed question ONLY when the user's initial message explicitly names a sub-angle (definition / mechanism / use-case / failure-mode). State the assumption inline: *"Assuming you want the [A/B/C] angle — correct if wrong."* The Phase 3 approval gate is NEVER skippable, no matter how well-framed the initial message is.

**Also confirm baseline ONLY when the concept requires a prerequisite.**

*Prereq trigger criterion:* a concept requires a prerequisite check if (a) its mechanism cannot be stated without naming a sub-concept the learner has not confirmed knowing, AND (b) that sub-concept is itself teachable as a 1-node lesson. When in doubt, check — one question costs less than a wasted chunk.

> "Do you already know `<prerequisite>`? Yes / No / Sort-of?"

*Handler when learner answers No:* silently prepend the prerequisite as Node 1 of the plan tree (shift all planned nodes down by one). Note the expansion at Phase 2's ASCII tree — the user sees the modification at the Phase 3 approval gate and can amend it there. If the prerequisite itself has unmet prerequisites, cap at one level of prepend and flag the deeper gap inline: *"Note: `<deeper-prereq>` may also be unfamiliar — flag if needed."*

Do not ask more than 2 questions in the scope interview. More = friction. (The prereq handler is a silent plan amendment, not a third question.)

## Phase 2 — Reason About Complexity → Emit Plan Tree

Based on the scope interview, classify the concept's complexity (per `SKILL.md` Rule 1):

- **1 node** — atomic concept, single mechanism
- **3 nodes** — setup → mechanism → consequence
- **5 nodes** — context → setup → mechanism → consequence → limits

State the plan to the user as an ASCII tree:

```
Concept: <name>
├── Node 1 — <short title>
├── Node 2 — <short title>
└── Node 3 — <short title>
```

## Phase 3 — Plan-Approval Gate

Fire a single `AskUserQuestion`:

> "Plan above: approve as drawn, or amend?"
> Options: "Approve as drawn (Recommended)" / "Amend (specify what to change)"

Do NOT proceed to Phase 4 until the user approves. If user amends, edit the tree and re-fire the gate.

## Phase 4 — Tree Walk (the load-bearing phase)

For each node in plan order:

1. **Emit ONE chunk** containing the node's BIG PICTURE only. Constraints:
   - ≤5 sentences of prose
   - At least one non-prose visual element (see `references/visuals.md`)
   - Different visual pattern than the previous chunk
   - Zero unexplained jargon (define inline in plain words, or do not use the term)
   - **Pre-emission jargon check:** before sending the chunk, scan it once for technical terms. Each term not in everyday English MUST be defined inline in the same sentence, in plain words. If a term cannot be defined in plain words within the sentence budget, rewrite the sentence to avoid the term. This check is mandatory — sentence-budget pressure is the most common cause of jargon-rule violations at runtime.
2. **Stop-and-check gate** — fire `AskUserQuestion` per `SKILL.md` Rule 3 schema. Options must be chunk-tailored:
   - **"Yes — advance to Node N+1 (Recommended)"** — substitute actual node number
   - **"No — `<predicted-confusion-source>`"** — predict the single most likely confusion direction *from the chunk you just emitted*. Chunk-specific, not generic.
   - **"Branch deeper — `<predicted-deeper-focus>`"** — predict the single most likely deeper-focus direction. Chunk-specific, not generic.
   - **"Other / specify"** — free-form fallback
3. **Branch on response:**
   - **Yes** (or any affirmative token per `SKILL.md` Rule 3) → advance to next sibling node. No transition preamble, no recap of the prior node — the next turn opens with Node N+1's chunk directly. (This is where v1.1 broke — see `tests/TC2-no-overstay.md`.)
   - **No** / "don't understand" → spawn child sub-branch. Announce aloud: *"Opening Node N.1 — same idea, simpler scope: `<focus>`."* Emit the child's big-picture chunk under the same chunk contract. After the child resolves with Yes, announce *"Closing Node N.1. Back to Node N+1."* then emit Node N+1's chunk.
   - **Branch deeper** / specification request on the current node's topic → spawn child sub-branch Node N.k with deeper focus. Announce *"Opening Node N.k — `<topic>`."* on descent and *"Closing Node N.k. Back to Node N+1."* on return. Same chunk contract inside the child.
   - **Off-topic question** → note as a labeled inline aside (one sentence: *"Aside: `<answer>`. Back to Node N."*), then return to the planned next sibling. *On-topic vs off-topic test:* a question is on-topic (and therefore spawns a named child per the previous bullet) if and only if answering it requires explaining a sub-component, mechanism, or term that was mentioned or implied in the current node's chunk. A question introducing a concept not referenced in the current chunk is off-topic. When in doubt, emit the one-sentence aside and continue — do not spawn a child for tangential associations.

## Phase 5 — Synthesis Chunk

After the last sibling node's "yes", emit ONE synthesis chunk:

- One sentence: *"Here's the whole picture together."*
- One visual that integrates all nodes (typically a flow diagram or summary table)
- **Final stop-and-check gate** — fire `AskUserQuestion`:
  - **"Yes — whole picture clicks, lesson complete (Recommended)"**
  - **"No — the synthesis didn't tie it together; re-walk the synthesis chunk"**
  - **"Re-walk Node `<N>` — `<predicted-weakest-node>`"** — pick the node where the user lingered longest, spawned the most child branches, or hesitated most on Yes
  - **"Other / specify"**

On **Re-walk Node N** → spawn a child branch on Node N with simpler scope. **A given node may be re-walked at most once.** On a second re-walk request for the same node, fire `AskUserQuestion`: *"Node N has already been re-walked. Pick: (a) mark lesson complete, (b) specify a concrete remaining question, (c) Other / specify."*

On **No** → re-emit the synthesis chunk with a different integrating visual. This is the **single authorized Rule 4 exception** (see `SKILL.md` Rule 4 — *Phase 5 synthesis exception*). If "No" fires a second time on the re-emitted synthesis, do NOT emit a third pass — automatically fire the Re-walk Node N path using the node the user lingered on longest.

## Session-Budget Guard

Before emitting any chunk, count chunks emitted in this session. If count ≥ 15, halt and fire `AskUserQuestion`. **Exception:** if a child branch is currently open (an *"Opening Node N.k"* announcement has been emitted without a corresponding *"Closing Node N.k"*), allow one more chunk to close the branch BEFORE halting. Interrupting mid-open-branch is prohibited — it breaks the tree-topology contract.

- **"Continue for `<estimated-remaining>` more chunks to finish the plan (Recommended)"** — estimate based on plan-tree remainder
- **"Pause for break — resume on re-invocation"**
- **"Wrap up now with synthesis chunk"**
- **"Other / specify"**

If the user has declined 2 chunks in a row ("stop", "skip", "not now"), suspend teaching and wait for re-invocation.

## Hand-off to Express

If mid-session the user signals urgency ("just give me the answer", "skip the rest", "shortcut"), drop ceremony and switch to `modes/express.md` for the remaining material. State the switch in one line: *"Switching to express mode for the rest."*

## Anti-patterns — Ceremony-Specific

- **Skipping the scope interview because the user "obviously" wants the topic** — costs one question, saves a wasted chunk.
- **Skipping the plan-approval gate "to save time"** — the gate IS the determinism contract; without it the skill regresses to v1.1.
- **Emitting a 2-chunk Node 1 because "it needs more"** — that's a child branch (Node 1.1), not a longer chunk.
- **Forgetting to vary visual pattern across chunks** — engagement collapses (the v1.1 Rule 8 diversity violation).
- **Treating "No" as a request to add more material** — "No" means spawn a simpler child, not amplify the parent.
- **Treating "Yes" as a license for a victory-lap recap of the prior node** — "Yes" means advance, full stop. No transition preamble. No "Great, now that you understand X, let's move to Y..." opener.
- **Silently branching without announcing the open/close** — the verbal naming IS the tree-operation contract (see `SKILL.md` Rule 4). A child branch the learner can't see is not a child branch.

## Return to SKILL.md

When the lesson completes (synthesis chunk acknowledged) or the user deactivates ("stop explain-it", "normal mode", "I know this already"), revert to standard explanation style. Acknowledge once: *"Explain-it complete. Back to normal."*
