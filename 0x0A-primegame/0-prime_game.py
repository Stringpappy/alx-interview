#!/usr/bin/python3
"""Module defining isWinner function."""

def isWinner(x, nums):
    """Function to determine the winner of the prime game."""
    maria_wins_count = 0
    ben_wins_count = 0

    for number in nums:
        rounds_set = list(range(1, number + 1))
        primes_set = primes_in_range(1, number)

        if not primes_set:
            ben_wins_count += 1
            continue

        is_maria_turn = True

        while True:
            if not primes_set:
                if is_maria_turn:
                    ben_wins_count += 1
                else:
                    maria_wins_count += 1
                break

            smallest_prime = primes_set.pop(0)
            rounds_set.remove(smallest_prime)

            rounds_set = [value for value in rounds_set if value % smallest_prime != 0]

            is_maria_turn = not is_maria_turn

    if maria_wins_count > ben_wins_count:
        return "Winner: Maria"

    if maria_wins_count < ben_wins_count:
        return "Winner: Ben"

    return None

def is_prime(number):
    """Returns True if the number is prime, else False."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    primes = [value for value in range(start, end + 1) if is_prime(value)]
    return primes
