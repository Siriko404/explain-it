# TC2 — No Overstay

**Rule under test:** Rule 3 — *Advance only on confirm; never overstay.* (Adjacent to TC1; emphasizes the "do not add more material" half.)
**Maps to painpoint:** #19 (v1.1 wild-transcript T01).

## User simulation

Learner invokes `/explain-it DCF valuation`.
After plan-approval (5 nodes), learner sees Node 1's chunk and replies: **"yes"** (single word, lowercase).

## v1.1 baseline failure

Skill interpreted the terse "yes" as permission to keep elaborating on Node 1 — emitting additional sub-bullets, edge cases, and "while we're here..." extensions. Multiple turns elapsed without ever opening Node 2.

## v2 pass criterion

A single "yes" or "y" is a full confirmation. The skill MUST:

1. Treat it as equivalent to "Yes, got it" — full advance signal.
2. Open Node 2's big-picture chunk on the next turn.
3. NOT solicit a more elaborate confirmation ("Are you sure? Did you understand the connection to...?").
4. NOT add a victory-lap recap of Node 1.

## Verdict

- **PASS** if Node 2 opens on the turn immediately following the single-word "yes".
- **FAIL** if the skill re-elaborates Node 1, asks for a more thorough confirmation, or stalls.
