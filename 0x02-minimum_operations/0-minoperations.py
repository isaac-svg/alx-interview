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
    
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        dp[i] = float('inf')
        
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n] if dp[n] != float('inf') else 0
