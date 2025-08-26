def daily_temperatures_optimize(temperatures: list[int])->list[int]:
    n = len(temperatures)
    if not temperatures or n < 2:
        raise ValueError('Temperature must be non-empty list with at least 2 elements')
    stack = []
    waits = [0]*n
    for i in range(n):
        while temperatures[i] > temperatures[stack[-1]]:
            prev_day = stack.pop()
            waits[prev_day] = i - prev_day
        # 📦 Store today's index for future comparison
        stack.append(i)
    return waits

def daily_temperatures_brute(temperatures: list[int])->list[int]:
    n = len(temperatures)
    if not temperatures or n < 2:
        raise ValueError('The temperature list must be non-empty list with at least 2 elements')
    waits = []
    for i in range(n):
        for j in range(i, n):
            if temperatures[j] > temperatures[i]:
                waits.append(j-i)
                break
        else:
            waits.append(0)
    return waits
