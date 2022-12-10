import math


"""The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence."""


def get_permutation(n, k, removed=None, maximum=None):
    """Return kth permutation sequence of set 1 <= x <= n"""
    if not n:
        return ''
    factor = math.factorial(n - 1)
    digit = math.ceil(k / factor)
    if removed:
        remaining = (i for i in range(1, maximum + 1) if i not in removed)
        digit = next(j for i, j in enumerate(remaining) if i + 1 == digit)
    removed = {digit} if not removed else removed.union({digit})
    if not maximum:
        maximum = n
    new_k = (k - 1) % factor + 1
    return str(digit) + get_permutation(n - 1, new_k, removed=removed, maximum=maximum)


print(get_permutation(10, 110))
