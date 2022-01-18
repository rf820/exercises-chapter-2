from math import sqrt


def isprime(n):
    if n in (2, 3, 5, 7):
        return True
    if n in (1, 4, 6, 8, 9):
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

