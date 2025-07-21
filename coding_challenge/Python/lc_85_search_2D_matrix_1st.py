'''
🔍 Problem Understanding
You’re given a 2D matrix like this:
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
And a target value. You need to return True if the target exists in the matrix, otherwise False.

Let’s clarify some assumptions first:

💡 Constraints:
	•	Each row is sorted from left to right.
	•	The first integer of each row is greater than the last integer of the previous row.

This means the 2D matrix can be treated as a 1D sorted array, right?
'''

def brute_force_search_matrix(matrix: list[list[int]], target: int)->bool:
  '''
  Brute force solution: check each element one by one
  Time: O(m*n)
  Space: O(1)
  '''
  for row in matrix:
    for val in row:
      if val == target:
        return True
  return False

def optimized_search_matrix_binary(matrix: list[list[int]], target: int) -> bool:
    """
    Optimized using Binary Search on virtual 1D array
    Time: O(log(m * n))
    Space: O(1)
    """
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    left = 0
    right = (rows * cols) - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols
        mid_val = matrix[row][col]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
  
def run_tests_binary():
    print("Test 1:", search_matrix_binary([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ], 3))  # Expected: True

    print("Test 2:", search_matrix_binary([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ], 13))  # Expected: False

    print("Test 3:", search_matrix_binary([[1]], 1))  # Expected: True
    print("Test 4:", search_matrix_binary([[1]], 2))  # Expected: False

if __name__ == "__main__":
    run_tests_binary()