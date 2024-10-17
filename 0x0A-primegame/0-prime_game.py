#!/usr/bin/python3
""" function to find winner """


def isWinner(x, nums):
    """ func to calc winner"""
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True for i in range(max(n + 1, 2))]
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    sieve = [i for i in range(len(sieve)) if sieve[i]]
    sieve = sieve[2:]
    m = len(sieve)

    def prime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    p = 0
    for n in nums:
        p += sum([1 for i in range(n + 1) if sieve[i] and prime(i)])
        if p % 2 == 0:
            return "Ben"
        return "Maria"
