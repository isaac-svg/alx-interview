#!/usr/bin/python3
"""Matrix manipulation"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2d matrix 90 degrees clockwise
    Returns: None
    """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            topLeft = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1