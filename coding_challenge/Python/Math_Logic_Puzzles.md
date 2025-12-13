# Math & Logic Puzzles — MIT‑style Walkthroughs (Brute Force → Optimized)

You asked for **.md and .py**. This Markdown is your teacher-style notes. The companion Python file
contains clean, FAANG‑style, flake8‑friendly code you can run and extend.

For each puzzle: we’ll (1) restate it, (2) ask Socratic prompts, (3) sketch a brute force, (4) derive an optimized
insight, and (5) note time/space complexity. Code references point to functions in `Math_Logic_Puzzles.py`.

---

## 1) The Heavy Pill
**Setup.** `n` bottles of pills, each good pill weighs `1.0 g`. Exactly **one bottle** is contaminated: its pills weigh `1.1 g`.
You have a precise digital scale you may use **once**. Identify the heavy bottle.

**Think first (prompts).**
- If you can weigh only once, how can you encode **which bottle** is heavy into a **single number** (the measured weight)?
- What if you took a *distinct* count of pills from each bottle?

**Brute force (not allowed by the rules).**
- Weigh each bottle separately → O(n) weighings. Violates the single‑weigh constraint.

**Optimized idea (information encoding).**
- Take `i` pills from bottle `i` (1‑indexed). Total *normal* weight would be `T = 1.0 * (1 + 2 + ... + n) = n(n+1)/2`.
- The extra weight over `T` will be `0.1 * k` where `k` is the index of the heavy bottle. One weighing ⇒ decode `k`.
- So the answer is achievable in **1 weighing**.

**Complexity.**
- Time to prepare pills: O(n). Scale uses: O(1). Space: O(1).

**Code.** See `heavy_pill_required_weighings(n)` (returns 1) and `heavy_pill_decode(extra_weight)`.

---

## 2) Basketball (2 to tie vs 3 to win — decision under uncertainty)
**Setup.** You’re down 2 points at the end. You can attempt a **2‑pointer** (probability `p2`) then go to **overtime**
with win probability `pOT` if you tie, or attempt a **3‑pointer** (probability `p3`) to **win now**.

**Think first (prompts).**
- Expected win prob if you shoot 3? If you shoot 2?
- What variables matter? (answer: `p2`, `pOT`, `p3`).

**Brute force.**
- Monte‑Carlo simulate end‑game scenarios. Accurate but slow to tune and doesn’t give a closed form.

**Optimized idea (closed‑form).**
- `Win_if_3 = p3`.
- `Win_if_2 = p2 * pOT` (you must make the 2 and then win OT).
- Prefer 3‑pointer iff `p3 > p2 * pOT`.

**Complexity.**
- O(1) decision.

**Code.** See `basketball_better_choice(p2, p_ot, p3)` and `basketball_mc(...)` for simulation.

---

## 3) Dominos (tiling and the “missing corners” board)
**Setup.** Classic: Can a standard 8×8 board with **two opposite corners removed** be tiled by 1×2 dominos?

**Think first (prompts).**
- Color chessboard black/white. How many black squares vs white squares remain after removing opposite corners?
- What does every domino cover in a colored board?

**Brute force.**
- Backtracking search to try all tilings — exponential and unnecessary for insight.

**Optimized idea (invariant).**
- A domino covers **one black + one white**.
- Removing opposite corners removes **two squares of the same color** → color counts unbalanced.
- Therefore **impossible** to tile.

**Generalization helper.**
- A necessary condition for domino tiling on a bipartite grid is equal counts of the two colors after removals.

**Code.** See `domino_tiling_possible(m, n, removed)` which checks the color‑parity necessary condition (fast sanity test).

---

## 4) Ants on a Triangle
**Setup.** 3 ants sit on the vertices of an equilateral triangle. Each ant picks a random direction (clockwise or
counter‑clockwise) and walks along the edges at the same speed. What’s the probability of a collision?

**Think first (prompts).**
- When do we **avoid** collisions entirely?
- Symmetry: all choose CW or all choose CCW.

**Optimized idea.**
- Avoid collision only if all ants choose the **same** direction. Probability = `2 / 2^3 = 1/4`. So collision probability is **3/4**.
- For an n‑gon with one ant per vertex: avoid = `2 / 2^n`, so collide = `1 − 2/2^n`.

**Code.** See `ants_polygon_collision_prob(n)`.

---

## 5) Jugs of Water
**Setup.** Two jugs with capacities `A` and `B` liters. You can fill, empty, or pour between jugs. Can you measure exactly `T`?

**Think first (prompts).**
- What state representation makes BFS straightforward?
- Number‑theory fact: solvable iff `T` is a multiple of `gcd(A, B)` and `T ≤ max(A, B)`.

**Brute force.**
- BFS on states `(x, y)` where `x ∈ [0..A]`, `y ∈ [0..B]` until `x == T or y == T`.

**Optimized idea.**
- Quick feasibility check using `gcd`. If feasible, BFS yields a shortest sequence of moves.

**Complexity.**
- State space size O(A * B).

**Code.** See `water_jugs_shortest_path(A, B, T)`.

---

## 6) Blue‑Eyed Island
**Setup.** Everyone sees others’ eye colors but not their own. A rule: if you **know** you have blue eyes, you must leave
the island at midnight. Common knowledge, perfect logicians. There are `K` blue‑eyed people. A visitor publicly states:
“I see at least one blue‑eyed person.” When do blue‑eyed people leave?

**Optimized idea (induction).**
- If `K = 1`, that person sees **0** blue eyes; hearing “at least one” implies **they** are blue → leaves night 1.
- If `K = 2`, each sees 1 blue. If there were only 1, they’d leave on night 1. That doesn’t happen, so both deduce `K=2` and leave night 2.
- In general, with `K` blue‑eyed, they leave on **night K**.

**Code.** See `blue_eyed_departure_day(k_blue)`.

---

## 7) The Apocalypse (boy‑girl paradox)
**Setup.** Every family has children until they have a **boy**, then they stop. What’s the ratio of boys to girls in the population?

**Optimized idea.**
- Each birth has 50% chance boy/girl. Stopping rule doesn’t bias the sex of **births** themselves.
- Expected boys ≈ expected girls → ratio ≈ **1:1**.

**Code.** See `apocalypse_sim(num_families, seed)` to verify by simulation.

---

## 8) The Egg Drop Problem
**Setup.** Given `E` eggs and `F` floors, find the minimum worst‑case number of drops to **guarantee** finding the
critical floor where eggs begin breaking.

**Brute force.**
- Plain DP on `(E, F)`: O(E * F^2). Works but slow for big F.

**Optimized idea (DP by moves).**
- Let `dp[m][e]` = maximum floors we can test with `m` moves and `e` eggs.
- Recurrence: `dp[m][e] = dp[m-1][e-1] + dp[m-1][e] + 1`.
- Find smallest `m` with `dp[m][E] ≥ F`. This runs in about O(E * m) steps, with `m << F`.

**Code.** See `egg_drop_min_moves(eggs, floors)`.

---

## 9) 100 Lockers
**Setup.** 100 lockers start closed. For pass `i=1..100`, toggle every locker whose index is divisible by `i`.
Which lockers end open?

**Optimized idea.**
- Locker `k` toggles once per **divisor** of `k`. It ends open iff it has an **odd** number of divisors → perfect squares.
- Open lockers: {1, 4, 9, 16, …}.

**Code.** See `lockers_open(n)` and `lockers_simulate(n)`.

---

## 10) Poison (find the poisoned bottle with test strips)
**Setup.** `N` bottles; exactly one is poisoned. You have test strips that show positive the **next day** after contact
with poison. How many strips are needed to identify the bottle in **one round**?

**Optimized idea (binary encoding).**
- Label bottles in binary; place drops on strips by bit position.
- Number of strips = `ceil(log2 N)`. The set of positive strips decodes the index.

**Code.** See `min_strips(N)` and `decode_poisoned_index(positives)`.

---

## How to practice (your rules)
1) **Restate** the puzzle in your own words. 2) **List** a brute‑force approach first. 3) **Identify** constraints / invariants.
4) **Derive** the optimized insight. 5) **Prove/argue** correctness. 6) **Check** edge cases. 7) **Analyze** time/space.
8) **Implement** cleanly (flake8). 9) **Test** with small cases. 10) **Reflect** what general tool you learned.