# Visualization Catalog

Reference for `explain-it` Rule 5 — *visual scaffold mandatory + rotate patterns*.

Every teaching chunk must include ≥1 non-prose visual element. Catalog lists 9 patterns. Rotate through them — don't repeat same pattern on two consecutive chunks of same lesson.

When unsure which pattern to pick, choose one that makes relationship between elements most spatially obvious:

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

Show chain of operations on one stream of value.

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

Show single source flowing to multiple recipients.

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

Rule is not just *include visual* — it is *rotate visual style across chunks*. Five vertical flow diagrams in a row fragments engagement; eye stops seeing them as scaffold, starts seeing them as background noise.

Heuristic: track pattern used in previous chunk. Next chunk must use different pattern, even if previous pattern would technically fit. Force variety.

If lesson genuinely demands same pattern twice (e.g., two sequential transformations), use different formatting variant — change arrow direction, swap horizontal for vertical, add side annotation — so eye registers it as fresh element.

## Anti-patterns

- **Pure-prose chunk with no visual** — violates Rule 5. Insert at minimum a boxed identity or causal-arrow chain; either takes one line.
- **Repeating same pattern on consecutive chunks** — v1.1 diversity violation. Force rotation.
- **Visual that duplicates prose** — bulleted restatement of what prose already said is not scaffold; it's redundancy. Visuals should show RELATIONSHIPS prose can't easily express (parallel structure, proportion, causal propagation).
- **Decorative visual unrelated to concept** — only include visuals that load-bear meaning. Decoration ≠ scaffold.

## Pedagogical basis

Graphical organizers reduce extraneous cognitive load when they make relationships between elements spatially explicit (Mayer's multimedia learning principles; Sweller's Cognitive Load Theory worked-examples corollary). Pure prose forces learner to construct spatial relationships mentally, competes with germane load for concept itself.

Rotation requirement is empirical. Variety preserves load-reducing scaffold effect; repeating same pattern causes it to recede into background noise.
