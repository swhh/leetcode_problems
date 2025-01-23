"""Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]"""

nums1 = [2,20,2,4,10,3,4,7,5]
nums2 = [0,3,2,5,4,6,1,1]
nums3 = [1, 1, 1, 1, 1, 2, 1, 3, 5, 5, 6, 4, 5, 6, 7]

def longest_consecutive_sequence(nums):
    """Find longest consecutive subsequence in O(n) time and space"""
    seen = dict()
    for num in nums:
        previous = seen.get(num - 1, 0)
        seen[num] = previous + 1
    return max(seen.values())

print(longest_consecutive_sequence(nums3))





    




