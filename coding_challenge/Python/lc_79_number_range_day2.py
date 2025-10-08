"""
🧠 Problem: Summary Ranges
📘 Description:
    Given a sorted list of unique integers, return a list of summary ranges.
    - Use "start->end" for ranges
    - Use "n" for single values

📌 Example:
    Input:  [0, 1, 2, 6, 7, 9]
    Output: ["0->2", "6->7", "9"]
"""


def brute_force_summary_ranges(nums: list[int]) -> list[str]:
    n = len(nums)
    if not n:
        return []
    sub_arr = [nums[0]]
    result = []
    for i in range(1, n):
        if nums[i] == nums[i - 1] + 1:
            sub_arr.append(nums[i])
        else:
            result.append(format_number_range(sub_arr))
            sub_arr = [nums[i]]
    result.append(format_number_range(sub_arr))
    return result


def format_number_range(nums: list[int]) -> str:
    return str(nums[0]) if len(nums) == 1 else f"{nums[0]}->{nums[-1]}"


def optimized_summary_range(nums: list[int]) -> list[str]:
    n = len(nums)
    if not n:
        return []
    start = nums[0]
    result = []
    for i in range(1, n):
        if nums[i] != nums[i - 1] + 1:
            end = nums[
                i - 1
            ]  # Pay attention to this because i run to n-1 but, end in for only check end = n--1
            result.append(str(start) if start == end else f"{start}->{end}")
            start = nums[i]  # set up new start
    end = nums[-1]  # so here we put it in last group
    result.append(str(start) if start == end else f"{start}->{end}")
    return result


if __name__ == "__main__":
    arr = [0, 1, 2, 6, 7, 9]
    result = brute_force_summary_ranges(arr)
    print(result)
