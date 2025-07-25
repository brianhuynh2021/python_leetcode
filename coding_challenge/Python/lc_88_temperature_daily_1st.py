def daily_temperatures_brute(temperatures: list[int]) -> list[int]:
    """
    📌 Problem:
    Given a list of daily temperatures, return a list such that, for each day in the input,
    tells you how many days you would have to wait until a warmer temperature.
    If there is no future day for which this is possible, put 0 instead.

    🔍 Brute Force Approach:
    For each day, loop forward to find the first warmer day.
    Stop immediately when found. Store the number of days waited.

    Args:
        temperatures (list[int]): List of daily temperatures.

    Returns:
        list[int]: List of number of days to wait for a warmer temperature.

    🧪 Example:
    >>> daily_temperatures_brute([50, 55, 53, 60])
    [1, 2, 1, 0]

    >>> daily_temperatures_brute([73, 74, 75, 71, 69, 72, 76, 73])
    [1, 1, 4, 2, 1, 1, 0, 0]
    """
    n = len(temperatures)
    if not temperatures or n < 2:
        raise ValueError(
            "Temperatures must be a non-empty list with at least 2 days."
        )
    waits = []
    for i in range(n):
        j = i + 1
        while j < n:
            if temperatures[j] > temperatures[i]:
                waits.append(j - i)
                break
            j += 1
        else:
            waits.append(0)
    return waits

