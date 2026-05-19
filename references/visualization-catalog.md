# Visualization Catalog (absorbed from teacher-mode v1.1, verbatim)

## Contents
1. Vertical flow diagram — sequential transformation
2. Branch tree — one-to-many split
3. Side-by-side boxes — two methods, same answer
4. Compact comparison table — strength/weakness contrast
5. Timeline with vertical markers — forecast horizon
6. Boxed identity — the take-away formula isolated
7. Causal-arrow chain — propagation of effect
8. Stacked-block ratio — proportional split visual
9. Decision tree — yes/no branches with consequences

> Rule 8 reference. Rotate patterns; never repeat one style across
> consecutive chunks. Pick the pattern that makes the relationship
> between elements most spatially obvious. Do not redesign — spec D1.

**1. Vertical flow diagram — sequential transformation.**

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

**2. Branch tree — one-to-many split.**

Show a single source flowing to multiple recipients.

```
        UFCF
         │
   ┌─────┴─────┐
   ▼           ▼
 lender     equity
```

**3. Side-by-side boxes — two methods, same answer.**

Show parallel computations that should converge.

```
┌─ Method A ──┐    ┌─ Method B ──┐
│  EBITDA     │    │  Net Income │
│  − tax      │    │  + D&A       │
│  − CapEx    │    │  + Def Tax   │
│  − ΔWC      │    │  − CapEx    │
│  ─────      │    │  − ΔWC       │
│  = $X       │    │  = $X       │
└─────────────┘    └──────────────┘
```

**4. Compact comparison table — strength/weakness contrast.**

```
Method        Strength            Weakness
─────────     ──────────────      ──────────────────
Perpetuity    Theory-pure         Sensitive to inputs
Multiple      Market-anchored     Subjective multiple
```

**5. Timeline with vertical markers — forecast horizon.**

```
   today  2024  2025  2026  2027  →  Terminal
     │     │     │     │     │         │
     ▼     ▼     ▼     ▼     ▼         ▼
   PV($) PV($) PV($) PV($) PV($)     PV(TV)
```

**6. Boxed identity — the take-away formula isolated.**

```
   ┌──────────────────────────────────┐
   │  WACC = wE·rE + wD·rD·(1−t)      │
   └──────────────────────────────────┘
```

**7. Causal-arrow chain — propagation of effect.**

```
More debt → more interest → bigger tax shield → lower WACC
```

**8. Stacked-block ratio — proportional split visual.**

```
              Total Capital
       ┌─────────────────────────┐
       │   Equity (85%)          │ ← cost: 10.82%
       │                         │
       ├─────────────────────────┤
       │   Debt (15%)            │ ← cost: 3.64% (after tax)
       └─────────────────────────┘
```

**9. Decision tree — yes/no branches with consequences.**

```
  Is project return > WACC?
        │
   ┌────┴────┐
   yes        no
    │          │
   value     destroy
   created    value
```

When in doubt, pick the pattern that makes the relationship between elements
most spatially obvious. Sequential = pattern 1. Splitting = pattern 2.
Comparing two computations = pattern 3 or 4. Time = pattern 5. Formula
isolation = pattern 6. Causation = pattern 7. Proportions = pattern 8.
Conditional logic = pattern 9.
