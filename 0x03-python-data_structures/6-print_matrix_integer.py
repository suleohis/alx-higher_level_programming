#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i  in range(len(matrix)):
        for j in range(len(matrix[i])):
            length = len(matrix[i])
            if length - 1 == j:
                print("{}".format(matrix[i][j]))
            else:
                print("{} ".format(matrix[i][j]), end='')
