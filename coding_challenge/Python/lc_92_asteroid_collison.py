'''
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
'''

def asteroid_collision_brute(asteroids: list[int]) -> list[int]:
    if not asteroids:
        raise ValueError("The asteroids must not be empty")
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(asteroids) - 1:
            a = asteroids[i]
            b = asteroids[i+1]
            if a > 0 and b < 0:
                print(f"Va chạm phát hiện: {a} → gặp {b} ← tại index {i}")
                # 🧨 Có va chạm → xử lý theo luật
                if abs(a) > abs(b):
                    asteroids.pop(i + 1)  # b nổ
                elif abs(a) < abs(b):
                    asteroids.pop(i)      # a nổ
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
        raise ValueError('The asteroids must not me empty')
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
                else:
                    asteroids.pop(i + 1)
                    asteroids.pop(i)
                hit = True
                break
            else:
                i += 1
    return asteroids

def asteroid_collision_optimized(asteroids: list[int]) -> list[int]:
    if not asteroids:
        raise ValueError('The asteroids must not be empty')
    stack = [] # Save those index of positive asteroids
    for i, asteroid in enumerate(asteroids):
        while stack and asteroid < 0:
            if abs(asteroids[stack[-1]]) > abs(asteroid):
                asteroids.pop(i)
                break
            if abs(asteroids[stack[-1]]) < abs(asteroid):
                asteroids.pop(stack[-1])
                break
            else:
                asteroids.pop(i)
                asteroids.pop(stack[-1])
        if asteroid > 0:
            stack.append(i)
    return asteroids

asteroid_collision_optimized([5, 10, -5])