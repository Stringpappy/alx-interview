#!/usr/bin/python3
"""
Function to determine the minimum number of coins needed to make a given total.
"""


def makeChange(coins, total):
    """
    Determines the minimum number of coins
    required to make up a given total amount.
    Args:
        coins (List[int]): A list of available coin denominations.
        total (int): The total amount we want to make change for.

    Returns:
        int: The minimum number of coins required to make the total.
             If it's not possible to make the total, returns -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    current_sum = 0
    num_coins = 0

    for coin in coins:
        while current_sum < total:
            current_sum += coin
            num_coins += 1
            if current_sum == total:
                return num_coins

        current_sum -= coin
        num_coins -= 1

    return -1
