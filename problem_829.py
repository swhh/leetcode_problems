from math import log2, floor

"""Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.



Example 1:

Input: n = 5
Output: 2
Explanation: 5 = 2 + 3
Example 2:

Input: n = 9
Output: 3
Explanation: 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: n = 15
Output: 4
Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5


Constraints:

1 <= n <= 109"""


def consecutive_numbers_sum(n):
    total = 1
    log_2 = log2(n)
    if not log_2 - floor(log_2):  # if n is a power of 2
        return total
    if n % 2 != 0:
        total += 1
    for i in range(3, n // 2, 2):
        if n % i == 0:
            total += 1
    return total


print(consecutive_numbers_sum(5))



