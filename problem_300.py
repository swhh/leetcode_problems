"""Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.


Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1"""
from bisect import bisect_left

nums1 = [0,1,0,3,2,3]
nums2 = [7,7,7,7,7,7,7]
nums3 = [10,9,2,5,3,7,101,18]


def length_of_lis(nums):
    """return length of longest increasing subsequence"""
    n = len(nums)
    sorted_nums = sorted(nums)
    longest = [0] * n 
    for num in nums:
        indx = bisect_left(sorted_nums, num)
        previous = longest[:indx]
        longest[indx] = max(previous) + 1 if previous else 1
    return max(longest)


    
    
    




