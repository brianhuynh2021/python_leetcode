def optimized_number_range(arr: list[int]) -> list[str]:
    """
    Summarizes a sorted list of unique integers into ranges.

    Consecutive numbers are grouped into a range string "start->end".
    Single numbers are returned as "n".

    Args:
        arr (list[int]): A sorted list of unique integers.

    Returns:
        list[str]: A list of strings representing the number ranges.

    Example:
        >>> optimized_number_range([0, 1, 2, 6, 7, 9])
        ['0->2', '6->7', '9']
    """
    # Edge case: return empty list if input is empty
    if not arr:
        return []
    # Initialize variables
    n = len(arr)
    start = arr[0]
    result = []
    # Iterate through the array to detect breaks in consecutive sequences
    for i in range(1, n):
        # Current number is not consecutive with previous → end current range
        if arr[i] != arr[i - 1] + 1:
            # Format and add the range to result: "n" if single, "start->end" if range
            end = arr[i - 1]
            result.append(str(start) if start == end else f"{start}->{end}")
            # Start a new range
            start = arr[i]
    # After loop ends, close the last range
    end = arr[-1]
    # Format and add the range to result: "n" if single, "start->end" if range
    result.append(str(start) if start == end else f"{start}->{end}")
    return result


if __name__ == "__main__":
    # Example input
    arr = [0, 1, 2, 6, 7, 9]
    # Call the function and print the result
    result = optimized_number_range(arr)
    print("Input:", arr)
    print("Output:", result)
