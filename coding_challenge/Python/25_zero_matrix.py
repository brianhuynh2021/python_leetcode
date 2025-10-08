def set_zeros(matrix):
    """
    Sets entire rows and columns to zero in a matrix where a zero element is found.

    Args:
    - matrix (List[List[int]]): The input matrix where zero elements will be processed.

    Returns:
    - None. Modifies the input matrix in-place.
    """
    rows = len(matrix)
    columns = len(matrix[0])
    zero_positions = []

    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                zero_positions.append((i, j))

    for row, column in zero_positions:
        for i in range(rows):
            matrix[i][column] = 0

        for j in range(columns):
            matrix[row][j] = 0
    return matrix


matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]

print(set_zeros(matrix))
[[1, 0, 3], [0, 0, 0], [7, 0, 9]]
