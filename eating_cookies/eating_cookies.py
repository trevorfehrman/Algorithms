import sys


def eating_cookies(n, cache=[1, 1, 2]):
    if not n in range(0, len(cache)):
        value = eating_cookies(
            n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
        cache.append(value)
    return cache[n]



