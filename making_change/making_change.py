#!/usr/bin/python

import sys


def making_change(amount, denominations, cache=None):
    if not cache:
        cache = {int: 0 for int in range(amount + 1)}
        cache[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            difference = higher_amount - coin
            cache[higher_amount] += cache[difference]

    return cache[amount]
