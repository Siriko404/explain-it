# Explain-it

Two Claude Code skills that teach you a technical concept properly.

- **`/explain-it <topic>`** — full ceremony. Scopes the session, scales
  a 1/3/5-step path to the concept's complexity, gets your approval,
  then teaches node-by-node as a tracked Zettelkasten lesson tree you
  never lose your place in, and saves it to a local markdown vault.
- **`/explain-it-now <topic>`** — zero ceremony. For when you're stuck
  and frustrated and need it explained *now*.

Both wrap a cognitive-load-grounded 10-rule delivery protocol
(one concept per message, concrete example first, zero unexplained
jargon, mandatory varied visuals, stop-and-check, rework-don't-add)
validated across real teaching sessions.

## Why two skills

`explain-it` prevents over-teaching and spiralling by forcing a
planned, approved, tracked lesson. `explain-it-now` deliberately strips
all of that for the moment a user is frustrated and needs an immediate
plain answer — the two have disjoint triggers so the right one fires.

## Structure

```
explain-it/
├── skills/
│   ├── explain-it/SKILL.md          # full ceremony
│   └── explain-it-now/SKILL.md      # urgent
├── references/
│   ├── core-protocol.md             # the 10-rule protocol (shared)
│   └── visualization-catalog.md     # 9 visual patterns (shared)
├── evals/                           # behavioral test scenarios
└── scripts/check_compliance.py      # Anthropic-compliance gate
```

## Install

Copy `skills/explain-it/` and `skills/explain-it-now/`, plus the
`references/` directory, into your Claude Code skills location. Keep
`references/` one level above the `skills/` directory as shipped — both
skills reference `../../references/*` one content level deep.

## Credits

Successor to the `teacher-mode` skill. Pedagogy grounded in Cognitive
Load Theory, Bloom mastery learning / zone of proximal development, the
Feynman technique, Zettelkasten Maps of Content, and Google LearnLM's
course-tutor "negotiate a study plan then track it" pattern. Built and
verified with the superpowers writing-skills Iron Law (RED-GREEN-
REFACTOR with subagent pressure tests).
