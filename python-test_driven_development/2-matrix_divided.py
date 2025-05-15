#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.

It handles a list of a list integers or floats.
If matrix is not a list of lists of integers or floats, it raises a TypeError.

You are not allowed to import any module.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    >>> matrix_divided([[2, 2], [4, 8]], 2)
    [[1.0, 1.0], [2.0, 4.0]]
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """

    if not isinstance(matrix, (list)):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, (list)):
            raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)
    return new_matrix
