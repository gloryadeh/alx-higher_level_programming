#!/usr/bin/python3
"""
This module divides all elements of a matrix
Raises:
    TypeError: if matrix is not a list of list of integers or floats
    and if div is not a number
    ZeroDivisionError: if div is equal to 0
"""


def matrix_divided(matrix, div):
    """
    Divides all elements in a matrix
    """
    new_matrix = []
    try:
        length = len(matrix[0])
    except Exception as e:
        pass
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError(err_msg)
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(err_msg)
            result = round(i / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix
