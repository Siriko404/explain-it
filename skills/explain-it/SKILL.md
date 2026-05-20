---
name: explain-it
description: Use when a user asks to be taught or walked through a technical concept they do not already know and is calm and not rushed — phrasings like "teach me", "explain how X works", "help me understand", "I'm not familiar with", "walk me through" — or explicitly invokes /explain-it. Also use when a concept is involved enough to need a planned multi-step lesson, not a one-off answer. Do not use for urgent or frustrated "I don't get it" moments, for peer-level discussion, or for state/option/decision requests.
---

# Explain-it (full ceremony)

Teach ONE technical concept to a non-expert via a planned, tracked,
user-approved lesson tree. Skeleton-not-script: the tree topology is
deterministic and tracked; delivery within each node stays adaptive.

Core failure this prevents: dumping many ideas at once, no plan, no
memory of where the lesson is — over-teaching, spiralling, diverging.

## Before anything: load the core

Read `references/core-protocol.md` (the 10-rule protocol + correction
matrix + anti-patterns) and `references/visualization-catalog.md` (9
visual patterns). Every teaching node obeys those rules. They are the
single source of truth — do not restate or redesign them here.

## When this skill applies / does not

Applies: explicit `/explain-it`; calm, non-urgent learning intent
("teach me X", "explain how Y works", "I'm not familiar with Z").
Does NOT apply: urgent or frustrated phrasing, caps, profanity, "I
don't understand", "too long" → that is the `explain-it-now` skill.

## Workflow — copy this checklist and track it

```
Explain-it progress:
- [ ] P0 Recon (conditional)
- [ ] P1 Scope interview
- [ ] P2 Complexity -> N-step path (N in {1,3,5})
- [ ] P3 Plan-approval gate
- [ ] P4 Teach (tree walk)
- [ ] P5 Persist
```

### P0 — Recon (conditional, bounded)

If the concept is repo/asset-anchored ("explain this module/file/repo"):
scan ONLY the files relevant to that concept. Do NOT ingest the whole
codebase. If it is a general concept (e.g. "difference-in-differences"),
SKIP P0 entirely.

### P1 — Scope interview

Use AskUserQuestion ONLY (never inline prose lists). Ask, in <=4
questions: learning goal/outcome, target depth, the user's current
baseline on prerequisites. This gates everything downstream — a wrong
scope wastes the whole session. Do not teach any content during P1.

### P2 — Complexity -> path

Self-assess concept complexity and design an N-step path:
- N=1: atomic concept (one node). May skip P3.
- N=3: moderate (3 sequential nodes).
- N=5: complex (5 sequential nodes).
Each node = exactly one concept (Rule 1). Calibrate node grain to the
user's stated baseline (zone of proximal development). Never exceed 5
nodes at one level — deeper detail is a child branch (see P4), not a
longer top-level path.

### P3 — Plan-approval gate

Render the proposed path as a tree (see MOC format below) and ask, via
AskUserQuestion: approve / amend. Do NOT teach until approved when
N>=3. N=1 may proceed directly.

**P3 plan output — REQUIRED and FORBIDDEN content:**

The plan output MUST include this line verbatim, immediately under the
node list:

> One node = one big-picture chunk per turn. Verbal "yes" advances.
> Confusion opens a sub-branch.

The plan output MUST NOT include any per-node turn-budget promise. The
following phrasings (and equivalents) are FORBIDDEN:
- "as many turns as needed"
- "as many focused turns as the concept requires"
- "deep mastery requires multiple turns"
- "until you fully grasp/master"
- any list of per-node sub-stages such as "intuition → example →
  formula → derivation → edge cases" rendered as a multi-turn checklist

Why: in past runs the agent freelanced an open-ended turn budget into
the P3 contract (e.g. "as many focused turns as the concept requires"),
then honored that contract by overstaying on Node 1 across multiple
turns instead of advancing on verbal yes. Locking the contract here
closes the loophole.

### P4 — Teach (skeleton-not-script tree walk)

Walk nodes in order. Deliver each node with the 10-rule protocol from
`references/core-protocol.md`, rotating visuals from
`references/visualization-catalog.md` (Rule 8 diversity). Teach exactly
ONE node per turn — never pre-empt later nodes.

Per-node state:
```
id: <parent.child>   title: <one concept>
status: pending|active|mastered|reworking
analogy: <the single analogy chosen>     # Rule 7
visual: <pattern used>                   # Rule 8 rotation
```

Mastery gate: do NOT advance to the next node until the current node's
comprehension is confirmed (stop-and-check, Rule 5).

Branch vs. rework — DISTINCT triggers, DISTINCT responses:
- "tell me more about X" / "give an example of Y" / "what about Z?"
  = SPECIFICATION REQUEST -> spawn a CHILD node under the current node
  with its own mini 1/3/5 path; teach it; return to the parent; update
  the MOC.
- "I don't understand" / "still lost" / "too hard"
  = CONFUSION -> REWORK the same node (Rule 6: simpler words/example,
  NO new material, NO branch). After 2 failed reworks, Rule 10
  multiple-choice clarifier.

MOC "you are here" anchor — render this EVERY teaching turn:
```
LESSON: <root concept>            [<m>/<n> nodes mastered]
  1. <state> <node1>
  2. <state> <node2>  <- you are here
     2.1 <state> <spec branch: ...>
  3. <state> <node3>
```
states: done = mastered, active = current, pending = not started,
reworking = in a rework loop.

Frustration mid-session: if the user becomes frustrated/urgent during
P4, DROP the ceremony and switch to pure 10-rule urgent behavior
in-place (same as explain-it-now). Do not restart, do not re-invoke a
skill. Resume the tree only if the user asks to continue.

### P5 — Persist

Write the lesson tree to a local Zettelkasten vault (default
`./explain-it-vault/`, configurable):
```
explain-it-vault/
  MOC-<root>.md            # index note, [[wikilinks]] to all nodes
  <root>/
    1-<node>.md            # one idea per note; frontmatter: id,title,
    2-<node>.md            #   parent, status, analogy, visual
    2.1-<spec-branch>.md
```
One idea per note; `[[wikilink]]` edges; MOC index = navigable, no
sprawl. Update on every node status change. (An Obsidian MCP backend is
a deferred enhancement; this markdown layout is already Obsidian-native
— no migration later.)

## Common mistakes

- Teaching during the scope interview (P1 is questions only).
- Emitting more than one concept in a teaching turn (Rule 1).
- Skipping the P3 gate "because it's quick" (N>=3 requires approval).
- Treating "give me an example" as confusion (it is a BRANCH, not a
  rework).
- Forgetting the MOC anchor on a turn (render it EVERY teaching turn).

## Deactivation

User says "stop", "I know this", "normal mode" -> exit, leave the vault
in place.
