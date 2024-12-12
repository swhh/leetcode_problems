"""Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer."""
from functools import cmp_to_key

nums = [3,30,34,5,9]
nums2 = [10,2]
nums3 = [824,938,1399,5607,6973,5703,9609,4398,8247]
nums4 = [432,43243]

def cmp(x, y):
    if x == y:
        return 0
    a, b = int(x + y), int(y + x)
    if a == b:
        return 0
    if a > b:
        return 1
    return -1

def largest_number(nums):
    result = ''.join(sorted((str(num) for num in nums), key=cmp_to_key(cmp), reverse=True))
    return result if int(result) else '0'



