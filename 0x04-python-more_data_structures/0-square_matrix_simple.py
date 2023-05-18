#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    # Iterate over the rows and columns of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            """Compute the square value of each 
            element and store it in the result matrix"""
            result[i][j] = matrix[i][j] ** 2

    return result
