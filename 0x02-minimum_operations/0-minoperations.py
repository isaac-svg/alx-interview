#!/usr/bin/python3
"""
Calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""
def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    
    Args:
    - n (int): The target number of H characters.
    
    Returns:
    - int: The fewest number of operations needed. If n is impossible to achieve, returns 0.
    """

    if n == 0:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        
        while n % factor == 0:
            n //= factor
            operations += factor
        
        factor += 1
        
    return operations


