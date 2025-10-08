"""
🚀 Problem Summary

Given an array of integers representing asteroids moving in space:
	•	Each integer represents the size and direction of an asteroid.
	•	Positive = moving right →
	•	Negative = moving left ←
	•	Collisions occur when two asteroids meet:
	•	Smaller one explodes.
	•	If both are the same size, both explode.
	•	Asteroids moving in the same direction never meet.

Return the state of the asteroids after all collisions.
✅ Example:
Input: [5, 10, -5]
Output: [5, 10]
Explanation: -5 moves left and meets 10. -5 explodes.
"""


def asteroid_collision_brute(asteroids: list[int]) -> list[int]:
    if not asteroids:
        raise ValueError("The asteroids must not be empty")
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(asteroids) - 1:
            a = asteroids[i]
            b = asteroids[i + 1]
            if a > 0 and b < 0:
                print(f"Va chạm phát hiện: {a} → gặp {b} ← tại index {i}")
                # 🧨 Có va chạm → xử lý theo luật
                if abs(a) > abs(b):
                    asteroids.pop(i + 1)  # b nổ
                elif abs(a) < abs(b):
                    asteroids.pop(i)  # a nổ
                else:
                    asteroids.pop(i + 1)  # cả hai nổ
                    asteroids.pop(i)
                changed = True  # Có thay đổi ⇒ restart lại vòng ngoài
                break
            else:
                i += 1
    return asteroids


def asteroid_collision_brute_2nd(asteroids: list[int]) -> list[int]:
    if not asteroids:
        raise ValueError("The asteroids must not me empty")
    hit = True
    while hit:
        hit = False
        i = 0
        while i < len(asteroids) - 1:
            a = asteroids[i]
            b = asteroids[i + 1]
            if a > 0 and b < 0:
                print(f"Found the hit {a} -> {b} <- index {i}")
                if abs(a) > abs(b):
                    asteroids.pop(i + 1)
                if abs(a) < abs(b):
                    asteroids.pop(i)
                    i = max(i - 1, 0)
                else:
                    asteroids.pop(i + 1)
                    asteroids.pop(i)
                    i = max(i - 1, 0)
            else:
                i += 1
    return asteroids


def asteroid_collision_optimized(asteroids: list[int]) -> list[int]:
    if not asteroids:
        raise ValueError("The asteroids must not be empty")
    pos = []  # Save those positive asteroids
    out = []
    for a in asteroids:
        if a > 0:
            pos.append(a)
            continue
        alive = True
        while pos and pos[-1] < -a:
            pos.pop()

        if pos and pos[-1] == -a:
            pos.pop()
            alive = False
        elif pos and pos[-1] > -a:
            alive = False

        if alive and not pos:
            out.append(a)

    return out + pos


def asteroid_collision_optimized(asteroids: list[int]) -> list[int]:
    if not asteroids:
        raise ValueError("The asteroids must not be ")
    stack = []  # to handle exploded asteroid
    for a in asteroids:
        alive = True
        while alive and stack and stack[-1] > 0 and a < 0:
            if stack[-1] < -a:
                stack.pop()
            elif stack[-1] == -a:
                stack.pop()
                alive = False
            else:
                alive = False
        if alive:
            stack.append(a)
    return stack


asteroid_collision_optimized([5, 10, -5])
