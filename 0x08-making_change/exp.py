#!/usr/bin/python3
""" 
Function to determine the minimum number of coins needed to make a given total.
"""

def makeChange(coins, total):
    """ 
    Determines the minimum number of coins required to make up a given total amount.

    Args:
        coins (List[int]): A list of available coin denominations.
        total (int): The total amount we want to make change for.

    Returns:
        int: The minimum number of coins required to make the total.
             If it's not possible to make the total, returns -1.
    """
    # Return 0 if total is zero or negative
    if total <= 0:
        return 0

    # Sort coins in descending order to try larger denominations first
    coins.sort(reverse=True)

    # Initialize variables to track the current sum and number of coins used
    current_sum = 0
    num_coins = 0

    # Iterate over the sorted coins list
    for coin in coins:
        # Use the current coin as much as possible
        while current_sum < total:
            current_sum += coin
            num_coins += 1
            
            # If we've reached the total, return the number of coins used
            if current_sum == total:
                return num_coins

        # If the current coin overshoots the total, backtrack
        current_sum -= coin
        num_coins -= 1

    # If it's impossible to make the exact total, return -1
    return -1

