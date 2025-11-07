# Chapter 21: Bit Manipulation — MIT-Style Notes

> Goal: Learn to think at the bit level. Use XOR, masks, and shifts to encode, count, or swap efficiently. Understand invariants (e.g., XOR cancels duplicates) and constraints (32-bit overflow, sign bits).

---

## 1) Single Number

**Problem.** Every element appears twice except one. Find that element.

**Brute-force.** Use hash map to count → O(n) space.

**Bit trick.** XOR of all numbers cancels duplicates (`a ^ a = 0`, `a ^ 0 = a`).  
→ The result is the unique element.

**Complexity.** O(n) time, O(1) space.

---

## 2) Single Number II

**Problem.** Every element appears three times except one.

**Observation.** Each bit position’s count mod 3 reveals the unique number’s bit.

**Approach.** Count bits in all numbers → if `sum(bit_i) % 3 != 0`, that bit belongs to the answer.

**Alternative.** Bitwise FSM trick: maintain `(ones, twos)` bitmasks.

**Complexity.** O(32n) ≈ O(n), O(1) space.

---

## 3) Missing Number

**Problem.** Given array `nums` of length n containing numbers `0..n`, find missing number.

**Brute-force.** Sum formula or hash set.

**Bit trick.** XOR all indices and values → missing = XOR(0..n) ^ XOR(nums).

**Complexity.** O(n), O(1).

---

## 4) Reverse Bits

**Problem.** Reverse bits of a 32-bit unsigned integer.

**Brute-force.** Convert to binary string, reverse, reparse → O(32).

**Bit trick.** Iterate 32 times: `res = (res << 1) | (n & 1); n >>= 1`.

**Complexity.** O(1) constant time per call.

---

## 5) Counting Bits

**Problem.** For all numbers ≤ n, return count of set bits.

**Brute-force.** For each i, count bits manually → O(n·log n).

**DP relation.** `bits[i] = bits[i >> 1] + (i & 1)`.

**Complexity.** O(n), O(n) space.

---

## 6) Sum of Two Integers

**Problem.** Add two integers without `+` or `-`.

**Idea.** Simulate binary addition using XOR (sum without carry) and AND (carry).

```
while carry != 0:
    a, b = a ^ b, (a & b) << 1
```

Handle 32-bit overflow using masks.

**Complexity.** O(1) average, O(32) worst case.

---

# Complexity Summary

| Problem | Time | Space |
|---|---|---|
| Single Number | O(n) | O(1) |
| Single Number II | O(n) | O(1) |
| Missing Number | O(n) | O(1) |
| Reverse Bits | O(1) | O(1) |
| Counting Bits | O(n) | O(n) |
| Sum of Two Integers | O(1) | O(1) |