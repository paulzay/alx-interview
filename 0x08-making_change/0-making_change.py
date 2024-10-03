#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """FUNCTION TO GIVE CHANGE"""
    if total == 0:
        return 1
    if total < 0:
        return 0
    if len(coins) == 0:
        return 0
    return makeChange(coins[:-1], total) + makeChange(coins, total - coins[-1])
