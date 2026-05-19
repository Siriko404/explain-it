# Explain-it v2.0 — Design Specification

**Date:** 2026-05-19
**Status:** Draft for ratification
**Supersedes:** `teacher-mode` v1.1.0 (self-contained successor; teacher-mode retired locally on ship)
**Tier:** 2 (public artifact, multi-subsystem, new dependency surface)

---

## 1. Problem & Goal

`teacher-mode` v1.1.0 is an empirically-validated, single-file pedagogical
protocol (10 rules, mandatory diverse visual scaffolding, frustration→rule
correction matrix). It works at the *chunk* level but has no *macro* structure:
it teaches reactively, chunk to chunk, with no global plan, no memory of where
the lesson is, and no persistence. Observed failure (user brain dump): the
teacher **over-teaches, spirals, diverges, and loses track of where the
conversation is**.

**Goal:** add a deterministic macro layer — a planned, user-approved,
tree-structured (Zettelkasten-style) lesson with persistent state — *wrapping*
the proven v1.1 micro-protocol, and ship it publicly on GitHub as **Explain-it**.

---

## 2. Locked decisions (ratified via brainstorming Q&A)

| # | Decision | Rationale / source |
|---|---|---|
| D1 | **Skeleton, not script.** Tree topology + node order deterministic and tracked; delivery *within* a node stays adaptive (v1.1 rework/branch/multiple-choice still fire). | v1.1 exists *because* rigid delivery failed angry users; a pure script recreates that failure. User-selected. |
| D2 | **Self-contained successor.** Explain-it absorbs the v1.1 10-rule protocol internally. `teacher-mode` retired locally; global CLAUDE.md reference updated to Explain-it on ship. No external skill dependency. | User-selected. Shippable as one self-contained repo. |
| D3 | **Two entry points.** `/explain-it` = full ceremony. `/explain-it-now` = urgent, no ceremony (preserves v1.1 fast behavior). | User-selected. Resolves the activation-policy risk (ceremony must not block frustration recovery). |
| D4 | **Two sibling skills, one shipped package, shared `references/`.** `skills/explain-it/` (full) + `skills/explain-it-now/` (urgent); both reference a package-root `references/` holding the single copy of the absorbed v1.1 core + visualization catalog. | User-selected ("two skills, one package"). Proven by `bevibing/tutor-skills` (ships `tutor-setup`+`tutor` in one repo). No core duplication; each skill independently discoverable and triggers on its own `description`. |
| D5 | **MVP cut.** Obsidian MCP backend, rich typed-link taxonomy, quiz/active-recall, spaced-repetition export → deferred to v2.1+. | User-approved. Keeps each file under Anthropic's ≤500-line rule and the spec shippable. |
| D6 | **Persistence default = local Zettelkasten markdown vault.** Obsidian MCP optional/auto-detected, deferred to v2.1+. | Evidence: `cyanheads/obsidian-mcp-server` needs Obsidian-running + Local REST API plugin + API key + Bun/Node; none connected in this environment. Hard deps = adoption barrier. |

---

## 3. Architecture

```
   ┌────────────────────────┐        ┌────────────────────────┐
   │  skills/explain-it/     │        │ skills/explain-it-now/  │
   │  SKILL.md               │        │ SKILL.md                │
   │  name: explain-it       │        │ name: explain-it-now    │
   │  triggers: explicit     │        │ triggers: -now, urgent, │
   │   /explain-it, learning │        │  frustration, caps,     │
   │   intent (non-urgent)   │        │  "FUCKING WORD"         │
   │                         │        │                         │
   │  P0 recon (cond.)       │        │  no ceremony            │
   │  P1 scope interview     │        │  v1.1 10-rule direct    │
   │  P2 complexity→1/3/5    │        │  optional 1-line        │
   │  P3 PLAN GATE           │        │   baseline              │
   │  P4 teach (tree walk)   │        │  no tree, no gate       │
   │  P5 persist (local md)  │        │  auto-promote if topic  │
   │   │ frustration mid-    │        │   balloons → suggest    │
   │   │ session → behave    │        │   /explain-it           │
   │   └ urgent (no handoff  │        │                         │
   │     skill-switch req'd) │        │                         │
   └───────────┬─────────────┘        └────────────┬────────────┘
               │   both read (one level deep)       │
               └────────────────┬───────────────────┘
                                ▼
                  ┌──────────────────────────────┐
                  │  references/  (package root)  │
                  │   core-protocol.md            │  ← single copy:
                  │   visualization-catalog.md    │    v1.1 10 rules +
                  └──────────────────────────────┘    matrix + 9 patterns
```

### 3.1 Trigger routing across the two skills

Each skill is discovered by its own `description` (Anthropic: metadata
pre-loaded; skill selected by description). No central router skill — routing
*is* the two descriptions plus one in-skill handoff rule.

| Signal | Skill selected |
|---|---|
| Explicit `/explain-it <topic>` | `explain-it` |
| Explicit `/explain-it-now <topic>` | `explain-it-now` |
| Learning intent, non-urgent ("teach me X", "explain how Y works", "I'm not familiar with Z") | `explain-it` |
| Frustration triggers ("don't understand", "too long", "FUCKING WORD", caps, profanity) | `explain-it-now` (description owns these triggers; never block a frustrated user with ceremony) |
| Frustration appears *mid* full session | `explain-it` SKILL.md instructs: drop ceremony, switch to urgent in-place behavior (no skill re-invocation needed) |
| `explain-it-now` session balloons (≥3 reworks OR user asks for structured/deeper coverage) | suggest the user re-invoke `/explain-it` for the full path |

Both `SKILL.md` files reference the package-root `references/*` exactly one
content level deep (Anthropic rule); the shared core lives in one place.

---

## 4. Package structure (ships to GitHub)

```
explain-it/                              # the shipped package (repo / plugin)
├── skills/
│   ├── explain-it/
│   │   └── SKILL.md          # name: explain-it; full ceremony P0–P5;
│   │                         #   refs ../../references/* (< 500 lines)
│   └── explain-it-now/
│       └── SKILL.md          # name: explain-it-now; urgent workflow;
│                             #   refs ../../references/* (< 200 lines)
├── references/                          # SHARED — single source of truth
│   ├── core-protocol.md      # absorbed v1.1: 10 rules + frustration→rule
│   │                         #   correction matrix (ToC at top)
│   └── visualization-catalog.md   # 9 v1.1 visual patterns (verbatim, ToC)
├── evals/
│   ├── eval-01-novice-concept.md
│   ├── eval-02-repo-anchored.md
│   └── eval-03-frustrated-recovery.md
└── README.md                            # public; brand "Explain-it"
```

`name:` frontmatter must be lowercase/hyphen (Anthropic hard constraint):
`explain-it` and `explain-it-now`. Brand "Explain-it" in README/docs. Each
SKILL.md references `references/*` exactly one content level deep.

---

## 5. Lesson-tree model & state

### 5.1 Node schema (rendered in-conversation; persisted as atomic .md in P5)

```yaml
id: 1.2            # hierarchical Luhmann-style id (parent.child)
title: "<one concept>"
parent: 1
status: pending | active | mastered | reworking
analogy: "<the single analogy chosen for this node>"  # Rule 7
visual: "<pattern name used>"                          # Rule 8 diversity tracking
comprehension: unconfirmed | confirmed | failed-rework-count:N
```

### 5.2 The "you are here" anchor (solves "don't get lost")

Every teaching turn renders a compact **Map of Content** breadcrumb:

```
LESSON: <root concept>            [2/3 nodes mastered]
  1. ✅ <node1>
  2. ▶  <node2>  ← you are here
     2.1 ⏸ <spec branch: user asked for example>
  3. ⬜ <node3>
```

Source: Zettelkasten MOC pattern — the index note that prevents link-web sprawl.

### 5.3 Branch vs. rework — distinct triggers, distinct responses (advisor-flagged)

| User signal | Interpretation | Response |
|---|---|---|
| "tell me more about X", "give an example of Y", "what about Z?" | **Specification request** | **Spawn child node** under current node with its own mini 1/3/5 path; push to tree; teach it; pop back to parent; update MOC |
| "I don't understand", "still lost", "too hard" | **Confusion** | **Rework same node** (v1.1 Rule 6 — simpler words/example, *no* new node, *no* new material). After 2 failed reworks → Rule 10 multiple-choice clarifier |

This distinction *is* the Zettelkasten requirement: branching is for
*expansion*, rework is for *compression*.

---

## 6. Full-ceremony workflow (`skills/explain-it/SKILL.md`)

- **P0 — Recon (conditional, bounded).** Only if the topic is repo/asset-anchored
  (e.g., "explain this module"). Bounded scan of *relevant* files only — NOT a
  full-codebase ingest. Skip entirely for general concepts (e.g., "explain
  difference-in-differences"). Source: avoids unbounded `learn-codebase`-scale cost.
- **P1 — Scope interview.** `AskUserQuestion` only (Sina-profile rule): session
  scope, learning goal/depth, audience baseline, prerequisite checks. ≤4 Qs per
  call. Source: LearnLM "ask subject/level/topic first"; SocraticAI "require
  structured input before teaching"; v1.1 Rule 9 baseline.
- **P2 — Complexity assessment → path design.** Self-assess concept complexity →
  design an N-step path, **N ∈ {1, 3, 5}** (simple/moderate/complex). Source:
  Bloom mastery + ZPD calibration. N=1 may skip P3 (low stakes).
- **P3 — Plan-approval gate.** Present the N-step path + the rendered tree.
  `AskUserQuestion`: approve / amend. Do not teach until approved (N≥3). Source:
  LearnLM "negotiate a study plan"; explicit user requirement.
- **P4 — Teach (skeleton-not-script tree walk).** Walk nodes in order. Each node
  delivered by the **absorbed v1.1 10-rule protocol** (Section 9). Branch vs.
  rework per §5.3. Render MOC anchor every turn. Mastery gate: do not advance
  until node comprehension confirmed (Bloom mastery learning).
- **P5 — Persist.** Write the lesson tree to a local Zettelkasten vault
  (§8). Update on every node status change.

---

## 7. Urgent workflow (`skills/explain-it-now/SKILL.md`)

Skip P0–P3. Straight to lightweight P4 = **pure v1.1 behavior**: 10-rule
protocol, optional one-line baseline check, no plan gate, no tree, no
persistence. This *is* preserved v1.1 — protects the frustration-recovery
origin (the reason v1.1 exists). If the session balloons (≥3 reworks or user
requests structured/deeper coverage) → offer promotion to full workflow.

---

## 8. Persistence — local Zettelkasten vault (MVP)

Default path: `./explain-it-vault/` in the working directory (configurable).

```
explain-it-vault/
├── MOC-<root-concept>.md       # the Map of Content index (links all nodes)
└── <root-concept>/
    ├── 1-<node>.md             # atomic note: one concept, frontmatter §5.1,
    ├── 2-<node>.md             #   [[wikilinks]] to parent/children/related
    └── 2.1-<spec-branch>.md
```

One idea per note, `[[wikilink]]` edges, MOC index = navigable without sprawl.
Obsidian MCP (`cyanheads/obsidian-mcp-server` or equivalent) = **optional,
auto-detected** upgrade in v2.1+; the same markdown layout is Obsidian-native
so no migration is needed.

---

## 9. Absorbed v1.1 core (kept intact, not redesigned)

The v1.1 10-rule protocol, the frustration→rule correction matrix, and the
9-pattern Visualization Catalog are **carried over verbatim** as the per-node
delivery engine. They are empirically validated (two real-world amendments) and
**out of scope for redesign** — D1 explicitly preserves them. They live ONCE in
the package-root `references/`: the 10 rules + correction matrix in
`references/core-protocol.md`, the 9 patterns in
`references/visualization-catalog.md` (each with a ToC at top, Anthropic rule
for ref files >100 lines). Both `skills/explain-it/SKILL.md` and
`skills/explain-it-now/SKILL.md` reference these one content level deep — no
duplication, single source of truth.

---

## 10. MVP scope

**In v2.0:** two entry points · router SKILL.md · scope interview · complexity
→1/3/5 path · plan-approval gate · lesson-tree + rendered MOC anchor ·
branch-vs-rework semantics · local-md Zettelkasten persistence · v1.1 10-rule
per-node intact · 3 eval scenarios + baseline · public README.

**Deferred v2.1+:** Obsidian MCP backend (auto-detect) · rich 6-type link
taxonomy · quiz/active-recall mode · spaced-repetition export · optional
literal `/explain-it-now` sibling skill.

---

## 11. Success criteria — eval scenarios (Anthropic eval-first mandate)

Evals are defined **before** extensive docs (Anthropic best-practices, cited).
Baseline = run current v1.1 `teacher-mode` on all three, record gaps, then
build to beat baseline.

1. **eval-01 novice general concept** (`/explain-it`, DiD-style). Expect: P0
   skipped; scope interview run; ≤5-step plan approved; tree + MOC rendered;
   converges ≤2 reworks/node; no spiral/over-teach.
2. **eval-02 repo-anchored** (`/explain-it` on a code module). Expect: P0 recon
   bounded to *relevant* files only; plan reflects the actual module; tree
   persisted to local vault with valid wikilinks.
3. **eval-03 frustrated recovery** (`/explain-it-now`, input contains
   "i did not understand a FUCKING WORD"). Expect: zero ceremony; immediate
   v1.1 behavior; no AskUserQuestion gate; fast.

Each eval file: query, inputs, expected_behavior list (Anthropic eval JSON
shape adapted to markdown).

---

## 12. Anthropic-compliance checklist (gates the ship)

- [ ] `name: explain-it` AND `name: explain-it-now` — lowercase/hyphen, ≤64
      chars, no reserved words ("anthropic"/"claude")
- [ ] both `description`s — third person, what + when, key trigger terms,
      ≤1024 chars, disjoint trigger sets (no cross-trigger)
- [ ] each `SKILL.md` < 500 lines; each `references/*` file has ToC if >100 lines
- [ ] references one content level deep from each SKILL.md
- [ ] forward-slash paths only
- [ ] no time-sensitive phrasing (use "old patterns" section if needed)
- [ ] consistent terminology (one term per concept)
- [ ] ≥3 evals; baseline measured; tested Haiku/Sonnet/Opus
- [ ] one default per decision point, escape hatch only where needed

---

## 13. Risks & open questions

- **R1 — Ceremony fatigue.** Even gated, P1–P3 may annoy. *Mitigation:* N=1
  skips P3; frustration always routes to `-now`; promotion is opt-in.
- **R2 — Complexity self-misjudgment** (wrong N). *Mitigation:* P3 approval
  gate lets the user correct N before any teaching.
- **R3 — Recon unbounded.** *Mitigation:* P0 is conditional + explicitly
  bounded to relevant files; general concepts skip it.
- **R4 — Two-skill discovery overlap.** Two skills with adjacent purpose may
  mis-trigger (urgent picked when full wanted, or vice-versa). *Mitigation:*
  disjoint trigger sets in the two `description` fields (§3.1); `explain-it-now`
  owns frustration/urgent terms exclusively; in-skill handoff rule for
  mid-session frustration; validated by eval-01 + eval-03.
- **OQ1 — Vault location default.** `./explain-it-vault/` proposed; confirm at
  implementation.

---

## 14. Next step

On ratification: invoke **superpowers:writing-plans** to produce the
implementation plan. Build order: evals + v1.1 baseline first →
`references/core-protocol.md` + `references/visualization-catalog.md` (extract
v1.1 verbatim) → `skills/explain-it/SKILL.md` (full P0–P5) →
`skills/explain-it-now/SKILL.md` (urgent) → README → Anthropic compliance pass
→ run evals vs. baseline → CLAUDE.md teacher-mode→explain-it update → ship.
