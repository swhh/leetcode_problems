"""Given an integer n, return the number of prime numbers that are strictly less than n."""
import math

def count_primes(n):
    primes = [True for _ in range(2, n + 1)]
    limit = math.floor(math.sqrt(n))
    for i in range(2, limit + 1):
        if primes[i]:
            for j in range(2, n // i + 1):
                primes[i * j - 2] = False
    return sum(primes[:-1])

print(count_primes(10))





