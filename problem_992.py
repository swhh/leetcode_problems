"""Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length"""

test_nums1 = [1, 2, 1, 2, 3]
test_nums2 = [1, 2, 1, 3, 4]


def sub_arrays_with_k_distinct(nums, k):
    num_distinct = i = 0
    j = k - 1
    while i <= len(nums) - k:
        distinct = set(nums[i: j + 1])
        while len(distinct) <= k and j < len(nums):
            distinct.add(nums[j])   
            if len(distinct) == k:
                num_distinct += 1   
            j += 1
        i += 1
        j = i + k - 1
    return num_distinct





print(sub_arrays_with_k_distinct(test_nums2, 3))
