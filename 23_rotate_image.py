'''
Given an image represented by an NxN matrix, where each pixel in the image is 
4 bytes, write a method to rotate the image by 90 degrees. Can you do this in 
place?
'''

def rotate_image(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(n//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp
    return matrix

print(rotate_image([[1,2], [3,4]]))