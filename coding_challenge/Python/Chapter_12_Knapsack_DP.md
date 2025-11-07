# Chapter 12 — 0/1 Knapsack (Dynamic Programming)

> **Style**: MIT-lecture, start from brute force → recursion → memoization → tabulation → space optimization. Includes Big-O, pitfalls, and practice tests.

## Notation (applies to the whole chapter)
- `n`: number of items/elements
- `W`: knapsack capacity / target sum
- Time complexities are expressed as functions of `n` and `W`

---

## 12.1 0/1 Knapsack — Max Value

**Problem**: Given `weights[i]`, `values[i]`, and `capacity W`, pick each item at most once to **maximize total value** without exceeding `W`.

### Brute Force (Backtracking)
- Choice at index `i`: **take** or **skip** item `i`.
- Recurse until `i == n` or `remaining == 0`.
- **Time**: `O(2^n)`, **Space**: `O(n)` (recursion stack).

### Recursion (Top-down) → Memoization
State `(i, remaining)` → best value from items `i..n-1` with capacity `remaining`. Cache results.
- **Time**: `O(n*W)`, **Space**: `O(n*W)` for memo + `O(n)` stack.

### Tabulation (Bottom-up, 2D)
`dp[i][c] = max value using first i items with capacity c`.
Transition:
```
if weights[i-1] <= c:
  dp[i][c] = max(dp[i-1][c], values[i-1] + dp[i-1][c-weights[i-1]])
else:
  dp[i][c] = dp[i-1][c]
```
- **Time**: `O(n*W)`, **Space**: `O(n*W)`.

### Space-Optimized (1D)
Iterate `c` **downwards** to avoid reusing the same item multiple times:
```
for i in range(n):
  for c in range(W, weights[i]-1, -1):
    dp[c] = max(dp[c], values[i] + dp[c - weights[i]])
```
- **Time**: `O(n*W)`, **Space**: `O(W)`.

### Pitfalls
- Updating `c` upward in 1D will overcount items (becomes unbounded).
- Capacity can be 0: answer must be 0.
- Weights can be greater than `W`: item must be skipped.

---

## 12.2 Subset Sum (Decision)

**Problem**: Given `nums` and integer `target`, determine if **any subset** sums to `target`.

### Brute Force
Try all subsets.
- **Time**: `O(2^n)`, **Space**: `O(n)`.

### Memoized Recursion
State `(i, t)` = can we reach sum `t` using suffix `i..n-1`?
- **Time**: `O(n*target)`, **Space**: `O(n*target)`.

### Tabulation / Space-Optimized
1D boolean dp where `dp[t]` answers reachability of sum `t`.
Iterate numbers and update `t` downward:
```
for x in nums:
  for t in range(target, x-1, -1):
    dp[t] = dp[t] or dp[t-x]
```
- **Time**: `O(n*target)`, **Space**: `O(target)`.

### Pitfalls
- Start with `dp[0] = True`.
- Downward iteration for 0/1 constraint.

---

## 12.3 Equal Subset Sum Partition

**Problem**: Given `nums`, can you split into two subsets with **equal sum**?

Observation: Let `S = sum(nums)`. If `S` is odd → impossible. Otherwise ask **Subset Sum** with `target = S//2`.

- **Time**: `O(n*S)`, **Space**: `O(S)` with 1D DP.

### Pitfalls
- Odd total sum → early return `False`.

---

## 12.4 Minimum Subset Sum Difference

**Problem**: Split `nums` into two subsets minimizing `|sum(A) - sum(B)|`.

Observation: Let total `S = sum(nums)`. Compute reachable sums `t` up to `S//2`. The best difference is `S - 2*t_max` where `t_max` is the largest reachable `t ≤ S//2`.

- **Time**: `O(n*S)`, **Space**: `O(S)`.

### Pitfalls
- Only need half range `[0 .. S//2]`.
- Use boolean reachability DP (like Subset Sum).

---

## 12.5 Count of Subset Sum

**Problem**: Count the number of subsets with sum exactly `target`.

### Recurrence
`count[i][t] = count[i-1][t] + count[i-1][t-nums[i-1]]` (if `nums[i-1] ≤ t`).
1D counting DP (update downward) with `dp[0] = 1`.
- **Time**: `O(n*target)`, **Space**: `O(target)`.

### Pitfalls
- Use integers, not booleans.
- Initialize `dp[0]=1` (empty subset forms 0).

---

## 12.6 Target Sum (LeetCode 494)

**Problem**: Given `nums` and `target`, assign `+/-` signs to reach `target`.
Count the number of ways.

### Transformation to Count Subset Sum
Let `P` be the sum of numbers assigned `+`, `N` for `-`. Then:  
`P - N = target` and `P + N = sum(nums)` ⇒ `2P = target + sum(nums)`.
Hence `P = (target + sum(nums)) / 2` must be integer and non-negative.  
Answer = **Count of Subset Sum** with `target = P`.

- **Time**: `O(n*P)`, **Space**: `O(P)`.

### Pitfalls
- Check parity and non-negativity of `target + sum(nums)`.
- Zeros in input multiply combinations.

---

## Quick Complexity Table

| Problem | Time | Space |
|---|---|---|
| 0/1 Knapsack (max value) | `O(n*W)` | `O(W)` |
| Subset Sum (decision) | `O(n*W)` | `O(W)` |
| Equal Partition | `O(n*S)` | `O(S)` |
| Min Subset Diff | `O(n*S)` | `O(S)` |
| Count Subset Sum | `O(n*W)` | `O(W)` |
| Target Sum | `O(n*P)` | `O(P)` |

---

## Practice Tests
Try these in the provided `__main__` section of the `.py`:

1. Knapsack: `weights=[1,3,4,5], values=[1,4,5,7], W=7 → 9`
2. Subset Sum: `nums=[1,2,3,7], target=6 → True`
3. Equal Partition: `nums=[1,5,11,5] → True`
4. Min Diff: `nums=[1,2,7] → 4`
5. Count Subset Sum: `nums=[1,2,3,3], target=6 → 3`
6. Target Sum: `nums=[1,1,1,1,1], target=3 → 5`

---

## FAANG-Style Tips
- For 1D DP, **iterate capacities downward** to preserve 0/1 constraint.
- Always write the recurrence first on paper; code becomes mechanical.
- Validate early-exit conditions (odd sums, negative capacity).
- Use `lru_cache` during whiteboard for clarity, then convert to tabulation.