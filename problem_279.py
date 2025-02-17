"""Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9."""
import math
from functools import cache
import sys

sys.setrecursionlimit(4000)

@cache
def num_squares(n):
    root = math.sqrt(n)
    floor = math.floor(root)
    if n == 1 or (root - floor) == 0:
        return 1
    perfect_sqs = (i ** 2 for i in range(1, int(floor) + 1))
    return min(num_squares(n - i) for i in perfect_sqs) + 1

print(num_squares(12))

    








    