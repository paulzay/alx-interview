#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """FUNCTION TO GIVE CHANGE"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total = total % coin
    if total != 0:
        return -1
    return num_coins
