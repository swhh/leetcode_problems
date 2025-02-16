"""Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer."""
from functools import lru_cache
from itertools import combinations_with_replacement as combo
nums = [2,3,-2,4]
num2 = [-1,4,-4,5,-2,-1,-1,-2,-3]



def max_product(nums):
    n = len(nums)
    if not n:
        return 0

    @lru_cache
    def recurse_prod(i, j):
        if i == j:
            return nums[i]
        if j == i + 1:
            return nums[i] * nums[j]
        return nums[i] * recurse_prod(i + 1, j - 1) * nums[j]
      
    return max(recurse_prod(i, j) for i, j in combo(range(n), 2))


print(max_product(nums))




