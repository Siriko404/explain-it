# Explain-it — Ceremony Mode (`/explain-it`)

Loaded by `explain-it` SKILL.md when user invokes `/explain-it <concept>` or activates explain-it via trigger phrase with no urgency signal.

Follow protocol verbatim. Don't skip steps.

## Phase 1 — Scope Interview

Before any planning, ask learner ONE question (via `AskUserQuestion` when available, else plain prompt).

**Seed question** (borrowed from Khanmigo + vuciv tutoring patterns):

> "What part of `<concept>` do you understand least right now — A: the basic definition, B: how it works mechanically, C: when to use it / when not to, D: something else (specify)?"

MAY skip seed question ONLY when user's initial message explicitly names sub-angle (definition / mechanism / use-case / failure-mode). State assumption inline: *"Assuming you want the [A/B/C] angle — correct if wrong."* Phase 3 approval gate NEVER skippable, no matter how well-framed initial message is.

**Also confirm baseline ONLY when concept requires prerequisite.**

*Prereq trigger criterion:* concept requires prereq check if (a) mechanism can't be stated without naming sub-concept learner hasn't confirmed knowing, AND (b) sub-concept itself teachable as 1-node lesson. When in doubt, check — one question costs less than wasted chunk.

> "Do you already know `<prerequisite>`? Yes / No / Sort-of?"

*Handler when learner answers No:* silently prepend prereq as Node 1 of plan tree (shift all planned nodes down by one). Note expansion at Phase 2's ASCII tree — user sees modification at Phase 3 approval gate, can amend there. If prereq itself has unmet prereqs, cap at one level of prepend, flag deeper gap inline: *"Note: `<deeper-prereq>` may also be unfamiliar — flag if needed."*

Don't ask more than 2 questions in scope interview. More = friction. (Prereq handler = silent plan amendment, not third question.)

## Phase 2 — Reason About Complexity → Emit Plan Tree

Based on scope interview, classify concept's complexity (per `SKILL.md` Rule 1):

- **1 node** — atomic concept, single mechanism
- **3 nodes** — setup → mechanism → consequence
- **5 nodes** — context → setup → mechanism → consequence → limits

State plan to user as ASCII tree:

```
Concept: <name>
├── Node 1 — <short title>
├── Node 2 — <short title>
└── Node 3 — <short title>
```

## Phase 3 — Plan-Approval Gate

Fire single `AskUserQuestion`:

> "Plan above: approve as drawn, or amend?"
> Options: "Approve as drawn (Recommended)" / "Amend (specify what to change)"

Do NOT proceed to Phase 4 until user approves. If user amends, edit tree and re-fire gate.

## Phase 4 — Tree Walk (load-bearing phase)

For each node in plan order:

1. **Emit ONE chunk** containing node's BIG PICTURE only. Constraints:
   - ≤5 sentences prose
   - ≥1 non-prose visual element (see `references/visuals.md`)
   - Different visual pattern than previous chunk
   - Zero unexplained jargon (define inline in plain words, or don't use term)
   - **Pre-emission jargon check:** before sending chunk, scan once for technical terms. Each term not in everyday English MUST be defined inline in same sentence, in plain words. If term can't be defined in plain words within sentence budget, rewrite sentence to avoid term. Check mandatory — sentence-budget pressure most common cause of jargon-rule violations at runtime.
2. **Stop-and-check gate** — fire `AskUserQuestion` per `SKILL.md` Rule 3 schema. Options must be chunk-tailored:
   - **"Yes — advance to Node N+1 (Recommended)"** — substitute actual node number
   - **"No — `<predicted-confusion-source>`"** — predict single most likely confusion direction *from chunk you just emitted*. Chunk-specific, not generic.
   - **"Branch deeper — `<predicted-deeper-focus>`"** — predict single most likely deeper-focus direction. Chunk-specific, not generic.
   - **"Other / specify"** — free-form fallback
3. **Branch on response:**
   - **Yes** (or any affirmative token per `SKILL.md` Rule 3) → advance to next sibling node. No transition preamble, no recap of prior node — next turn opens with Node N+1's chunk directly. (Where v1.1 broke — see `tests/TC2-no-overstay.md`.)
   - **No** / "don't understand" → spawn child sub-branch. Announce aloud: *"Opening Node N.1 — same idea, simpler scope: `<focus>`."* Emit child's big-picture chunk under same chunk contract. After child resolves with Yes, announce *"Closing Node N.1. Back to Node N+1."* then emit Node N+1's chunk.
   - **Branch deeper** / specification request on current node's topic → spawn child sub-branch Node N.k with deeper focus. Announce *"Opening Node N.k — `<topic>`."* on descent and *"Closing Node N.k. Back to Node N+1."* on return. Same chunk contract inside child.
   - **Off-topic question** → note as labeled inline aside (one sentence: *"Aside: `<answer>`. Back to Node N."*), then return to planned next sibling. *On-topic vs off-topic test:* question is on-topic (and therefore spawns named child per previous bullet) if and only if answering it requires explaining sub-component, mechanism, or term that was mentioned or implied in current node's chunk. Question introducing concept not referenced in current chunk = off-topic. When in doubt, emit one-sentence aside and continue — don't spawn child for tangential associations.

## Phase 5 — Synthesis Chunk

After last sibling node's "yes", emit ONE synthesis chunk:

- One sentence: *"Here's the whole picture together."*
- One visual that integrates all nodes (typically flow diagram or summary table)
- **Final stop-and-check gate** — fire `AskUserQuestion`:
  - **"Yes — whole picture clicks, lesson complete (Recommended)"**
  - **"No — the synthesis didn't tie it together; re-walk the synthesis chunk"**
  - **"Re-walk Node `<N>` — `<predicted-weakest-node>`"** — pick node where user lingered longest, spawned most child branches, or hesitated most on Yes
  - **"Other / specify"**

On **Re-walk Node N** → spawn child branch on Node N with simpler scope. **A given node may be re-walked at most once.** On second re-walk request for same node, fire `AskUserQuestion`: *"Node N has already been re-walked. Pick: (a) mark lesson complete, (b) specify concrete remaining question, (c) Other / specify."*

On **No** → re-emit synthesis chunk with different integrating visual. This is **single authorized Rule 4 exception** (see `SKILL.md` Rule 4 — *Phase 5 synthesis exception*). If "No" fires second time on re-emitted synthesis, do NOT emit third pass — automatically fire Re-walk Node N path using node user lingered on longest.

## Session-Budget Guard

Before emitting any chunk, count chunks emitted in session. If count ≥ 15, halt and fire `AskUserQuestion`. **Exception:** if child branch currently open (an *"Opening Node N.k"* announcement emitted without corresponding *"Closing Node N.k"*), allow one more chunk to close branch BEFORE halting. Interrupting mid-open-branch prohibited — breaks tree-topology contract.

- **"Continue for `<estimated-remaining>` more chunks to finish the plan (Recommended)"** — estimate based on plan-tree remainder
- **"Pause for break — resume on re-invocation"**
- **"Wrap up now with synthesis chunk"**
- **"Other / specify"**

If user has declined 2 chunks in a row ("stop", "skip", "not now"), suspend teaching and wait for re-invocation.

## Hand-off to Express

If mid-session user signals urgency ("just give me the answer", "skip the rest", "shortcut"), drop ceremony and switch to `modes/express.md` for remaining material. State switch in one line: *"Switching to express mode for the rest."*

## Anti-patterns — Ceremony-Specific

- **Skipping scope interview because user "obviously" wants topic** — costs one question, saves wasted chunk.
- **Skipping plan-approval gate "to save time"** — gate IS determinism contract; without it skill regresses to v1.1.
- **Emitting 2-chunk Node 1 because "it needs more"** — that's child branch (Node 1.1), not longer chunk.
- **Forgetting to vary visual pattern across chunks** — engagement collapses (v1.1 Rule 8 diversity violation).
- **Treating "No" as request to add more material** — "No" means spawn simpler child, not amplify parent.
- **Treating "Yes" as license for victory-lap recap of prior node** — "Yes" means advance, full stop. No transition preamble. No "Great, now that you understand X, let's move to Y..." opener.
- **Silently branching without announcing open/close** — verbal naming IS tree-operation contract (see `SKILL.md` Rule 4). Child branch learner can't see = not child branch.

## Return to SKILL.md

When lesson completes (synthesis chunk acknowledged) or user deactivates ("stop explain-it", "normal mode", "I know this already"), revert to standard explanation style. Acknowledge once: *"Explain-it complete. Back to normal."*
