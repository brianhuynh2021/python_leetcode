# Chapter 22: Math + Geometry — MIT-Style Notes

> Goal: Understand spatial and numerical transformations through algebraic invariants and matrix indexing. Replace brute-force recalculation with structured patterns.

---

## 1) Rotate Image (LC 48)

**Problem.** Rotate n×n matrix 90° clockwise in-place.

**Brute-force.** Create new matrix and assign rotated positions. O(n²) space.

**In-place trick.** Transpose (swap `i,j`) → reverse each row.

**Complexity.** O(n²) time, O(1) extra.

---

## 2) Spiral Matrix (LC 54)

**Problem.** Return elements of matrix in spiral order.

**Idea.** Maintain four boundaries (top, bottom, left, right); shrink after traversing each side.

**Complexity.** O(mn), O(1).

---

## 3) Valid Sudoku (LC 36)

**Problem.** Validate partially filled 9×9 board.

**Brute-force.** Check every row, col, subgrid repeatedly → O(81²).

**Optimized.** Track sets for rows, cols, and boxes.  
Index of 3×3 box = `(r // 3) * 3 + c // 3`.

**Complexity.** O(81) ≈ O(1).

---

## 4) Greatest Common Divisor (GCD)

**Euclid’s Algorithm.**
```
while b != 0:
    a, b = b, a % b
```
**Complexity.** O(log(min(a,b))).

---

## 5) Count Primes (LC 204)

**Problem.** Count primes < n.

**Brute-force.** Check divisibility → O(n√n).

**Sieve of Eratosthenes.** Mark multiples starting from i².  
**Complexity.** O(n log log n), O(n) space.

---

# Complexity Summary

| Problem | Time | Space |
|---|---|---|
| Rotate Image | O(n²) | O(1) |
| Spiral Matrix | O(mn) | O(1) |
| Valid Sudoku | O(81) | O(81) |
| GCD | O(log n) | O(1) |
| Count Primes | O(n log log n) | O(n) |