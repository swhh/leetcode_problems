"""Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order."""
from itertools import compress

def pad_bin(num, bin_len):
    """Convert int num to binary string with length bin_len"""
    return format(num, 'b').zfill(bin_len)

def subsets(nums):
    """Return power set i.e. all possible subsets of nums"""
    exp = len(nums)
    masks = (map(lambda x: bool(int(x)),pad_bin(num, exp)) for num in range(0, 2 ** exp)) # use binary strings to create subset masks
    return [list(compress(nums, mask)) for mask in masks]

print(subsets([1, 2, 3, 4]))


