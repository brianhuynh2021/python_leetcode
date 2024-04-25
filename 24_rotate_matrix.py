"""
    Rotate Matrix: Given an image represented by an NxN matrix, 
    where each pixel in the image is 4 bytes, write a method 
    to rotate the image by 90 degrees. Can you do this in place?
"""

def rotate_matrix(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return False  # Invalid input matrix

    n = len(matrix)
    
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            # Save top
            top = matrix[first][i]
            
            # Move left to top
            matrix[first][i] = matrix[last - offset][first]
            
            # Move bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]
            
            # Move right to bottom
            matrix[last][last - offset] = matrix[i][last]
            
            # Move top to right
            matrix[i][last] = top
    
    return True

# Test case
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix)

for row in matrix:
    print(row)
