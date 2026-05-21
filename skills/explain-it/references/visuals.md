# Visualization Catalog

Reference for `explain-it` Rule 5 — *visual scaffold mandatory + rotate patterns*.

Every teaching chunk must include at least one non-prose visual element. This catalog lists 9 patterns. Rotate through them — do not repeat the same pattern on two consecutive chunks of the same lesson.

When unsure which pattern to pick, choose the one that makes the relationship between elements most spatially obvious:

| If the chunk shows… | Use pattern… |
|---|---|
| A sequence of transformations | 1. Vertical flow diagram |
| A one-to-many split | 2. Branch tree |
| Two computations that should converge | 3. Side-by-side boxes |
| A strength/weakness contrast | 4. Comparison table |
| A forecast or time horizon | 5. Timeline |
| The take-away formula | 6. Boxed identity |
| Causation propagating through steps | 7. Causal-arrow chain |
| Proportions / ratios | 8. Stacked-block ratio |
| Yes/no conditional logic | 9. Decision tree |

---

## 1. Vertical flow diagram — sequential transformation

Show a chain of operations on one stream of value.

```
   Revenue
     │
     │  − operating costs
     ▼
   Operating Profit
     │
     │  − tax
     ▼
   After-Tax Profit
```

## 2. Branch tree — one-to-many split

Show a single source flowing to multiple recipients.

```
        UFCF
         │
   ┌─────┴─────┐
   ▼           ▼
 lender     equity
```

## 3. Side-by-side boxes — two methods, same answer

Show parallel computations that should converge.

```
┌─ Method A ──┐    ┌─ Method B ──┐
│  EBITDA     │    │  Net Income │
│  − tax      │    │  + D&A      │
│  − CapEx    │    │  + Def Tax  │
│  − ΔWC      │    │  − CapEx    │
│  ─────      │    │  − ΔWC      │
│  = $X       │    │  = $X       │
└─────────────┘    └─────────────┘
```

## 4. Compact comparison table — strength / weakness contrast

```
Method        Strength            Weakness
─────────     ──────────────      ──────────────────
Perpetuity    Theory-pure         Sensitive to inputs
Multiple      Market-anchored     Subjective multiple
```

## 5. Timeline with vertical markers — forecast horizon

```
   today  2024  2025  2026  2027  →  Terminal
     │     │     │     │     │         │
     ▼     ▼     ▼     ▼     ▼         ▼
   PV($) PV($) PV($) PV($) PV($)     PV(TV)
```

## 6. Boxed identity — the take-away formula isolated

```
   ┌──────────────────────────────────┐
   │  WACC = wE·rE + wD·rD·(1−t)      │
   └──────────────────────────────────┘
```

## 7. Causal-arrow chain — propagation of effect

```
More debt → more interest → bigger tax shield → lower WACC
```

## 8. Stacked-block ratio — proportional split

```
              Total Capital
       ┌─────────────────────────┐
       │   Equity (85%)          │ ← cost: 10.82%
       │                         │
       ├─────────────────────────┤
       │   Debt (15%)            │ ← cost: 3.64% (after tax)
       └─────────────────────────┘
```

## 9. Decision tree — yes/no branches with consequences

```
  Is project return > WACC?
        │
   ┌────┴────┐
   yes        no
    │          │
   value     destroy
   created    value
```

---

## Rotation discipline

The rule is not just *include a visual* — it is *rotate the visual style across chunks*. Five vertical flow diagrams in a row fragments engagement; the eye stops seeing them as scaffold and starts seeing them as background noise.

A simple heuristic: track the pattern used in the previous chunk. The next chunk must use a different pattern, even if the previous pattern would technically fit. Force the variety.

If a lesson genuinely demands the same pattern twice (e.g., two sequential transformations), use a different formatting variant — change the arrow direction, swap horizontal for vertical, add a side annotation — so the eye registers it as a fresh element.

## Anti-patterns

- **Pure-prose chunk with no visual** — violates Rule 5. Insert at minimum a boxed identity or a causal-arrow chain; either takes one line.
- **Repeating the same pattern on consecutive chunks** — the v1.1 diversity violation. Force rotation.
- **Visual that duplicates the prose** — a bulleted restatement of what the prose already said is not a scaffold; it's redundancy. Visuals should show RELATIONSHIPS the prose cannot easily express (parallel structure, proportion, causal propagation).
- **Decorative visual unrelated to the concept** — only include visuals that load-bear meaning. Decoration ≠ scaffold.

## Pedagogical basis

Graphical organizers reduce extraneous cognitive load when they make relationships between elements spatially explicit (Mayer's multimedia learning principles; Sweller's Cognitive Load Theory worked-examples corollary). Pure prose forces the learner to construct the spatial relationships mentally, which competes with germane load for the concept itself.

The rotation requirement is empirical — derived from the v1.1 → v2 amendment, where the FINANCE-project DCF tutorial used 5 consecutive vertical flow diagrams and the user reported engagement collapse. Variety preserves the load-reducing effect.
