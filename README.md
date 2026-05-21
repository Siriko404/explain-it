# Explain-it

A deterministic teaching protocol for Claude Code. Stops the model from diverging, spiralling, and over-delivering when explaining a technical concept to someone who doesn't already know it.

> **Core invariant:** the lesson IS a tree. Every chunk is a tree operation — root, advance to sibling, or descend to child. No exception.

## What it does

Default LLM explanations to non-experts fail in predictable ways: long paragraphs overload working memory; jargon stacks without translation; multiple ideas batch into one message; the model adds *more* material when the learner says "I don't understand" (instead of reworking simpler); and analogies switch mid-explanation.

Explain-it constrains the agent to a zettelkasten-style tree:

1. **Plan first.** Reason about the concept's complexity → emit a 1-, 3-, or 5-node tree → get user approval.
2. **One node per chunk.** Each chunk delivers the node's *big picture*, ≤5 sentences of prose plus one visual element (diagram, table, boxed identity). Sub-detail lives in child branches.
3. **Advance only on confirm.** On "yes" → next sibling node. Never overstay.
4. **Confusion spawns a child branch.** On "don't understand" or "explain deeper" → open a named child node (Node N.1), resolve, return to parent's next sibling. *Tree topology IS the determinism.*
5. **Visual scaffold mandatory + rotate.** Every chunk includes a non-prose visual; rotate patterns chunk-to-chunk.

## Two entry points

| Command | When to use |
|---|---|
| `/explain-it <concept>` | Default. Time to learn properly. Scope interview + plan-approval gate + full tree walk. |
| `/explain-it-now <concept>` | Urgent or mid-task. Skip the gates, single-pass tree walk, max 5 chunks. |

The skill also auto-activates on trigger phrases (*"teach me"*, *"I don't understand"*, *"too much jargon"*, etc.) without an explicit slash command.

## Install

```bash
# Clone
git clone https://github.com/<your-username>/Explain-it.git
cd Explain-it

# Copy skill to your Claude Code skills dir
cp -r skills/explain-it ~/.claude/skills/

# Copy slash commands
cp commands/explain-it.md ~/.claude/commands/
cp commands/explain-it-now.md ~/.claude/commands/
```

On Windows PowerShell:

```powershell
Copy-Item -Recurse skills/explain-it $env:USERPROFILE/.claude/skills/
Copy-Item commands/explain-it.md $env:USERPROFILE/.claude/commands/
Copy-Item commands/explain-it-now.md $env:USERPROFILE/.claude/commands/
```

Restart Claude Code (or `/reload` if your environment supports it).

## Verify

```bash
# In Claude Code, in a fresh conversation:
/explain-it difference-in-differences
```

Expected: Claude asks the seed question, emits a 3-node plan tree, fires the approval gate, then walks the tree one node per chunk with visuals.

## How it's different from other teaching skills

Audited May 2026 against the public landscape ([bevibing/socrates-skill](https://github.com/bevibing/socrates-skill), [DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities), [GarethManning/claude-education-skills](https://github.com/GarethManning/claude-education-skills), Khanmigo, Anthropic Claude Learning Mode):

- **Deterministic tree topology with complexity-to-path mapping (1/3/5).** Every competitor is a flat dialog loop. None pre-commit to a tree before teaching.
- **Confusion is a structural tree operation, not a rewrite.** "Don't understand" spawns a named child branch — preserving the trail and the parent context — instead of in-place rephrasing.
- **Dual entry points + visualization rotation contract.** No surveyed competitor has either the ceremony/express split or a per-chunk visual-pattern rotation rule.

## Architecture

```
skills/explain-it/
├── SKILL.md                    central router + 5 core rules
├── modes/
│   ├── ceremony.md             /explain-it full protocol
│   └── express.md              /explain-it-now urgent protocol
└── references/
    └── visuals.md              9-pattern visualization catalog

commands/
├── explain-it.md               ceremony slash command
└── explain-it-now.md           express slash command

tests/
└── TC1-TC6                     6 baseline failure scenarios v2 must pass
```

## Pedagogy basis

| Source | Evidence strength | Used for |
|---|---|---|
| Cognitive Load Theory (Sweller) | Strong | Worked-examples sequencing; visual scaffold reduces extraneous load |
| Multimedia Learning (Mayer) | Strong | Graphical organizers reduce extraneous load when spatial |
| Feynman Technique | Strong | Sixth-grade-simplicity test for jargon |
| Diátaxis (Procida) | Moderate | Tutorial ≠ explanation distinction |
| Carpentries pedagogy | Moderate | One-idea-per-chunk |
| Zettelkasten tree topology applied to live tutoring | Original | The tree contract |

**Explicitly rejected:** VAK / "learning styles" matching (Pashler et al., 2008 — no robust evidence); "key concepts" bullet lists as substitute for teaching; "adapt style to learner" without scope-interview evidence.

## Origin

- **v1.0 (Apr 2026)** — built after multiple failed econometrics tutorials. User feedback: *"your explanation is too long and too hard to understand"*, *"i did not understand a FUCKING WORD"*.
- **v1.1 (May 2026)** — visual-scaffold rule added after DCF tutorial regression: *"i dont like how you throw a chunk of text with numbers and quations and stuff messing the shit at me"*.
- **v2.0 (May 2026)** — full rewrite around tree topology after CFA Level 1 tutorial revealed the determinism gap: model planned 5 nodes, kept emitting Node-1 material across turns, never advanced. The 6 test cases in `tests/` are derived from that real-world failure transcript.

## License

MIT — see `LICENSE`.

## Author

Sina Soleimanipour — [github.com/<your-handle>](https://github.com/) · [linkedin.com/in/<your-handle>](https://linkedin.com/)
