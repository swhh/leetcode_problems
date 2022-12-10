"""Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []


Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice."""
nums_test1 = [1, 1, 2]
nums_test2 = [4, 3, 2, 7, 8, 2, 3, 1]


def find_duplicates(nums):
    if len(nums) < 2:
        return []
    i = j = 0
    previous = False
    while i < len(nums):
        num = nums[j]
        if num is False:
            if previous:
                nums[j] = True
        elif num is None:
            if previous:
                nums[j] = False
        elif num is True:
            pass
        else:
            if previous:
                nums[j] = False
            else:
                nums[j] = None
            j = num - 1
            previous = True
            continue
        i += 1
        j = i
        previous = False

    return [i + 1 for i, x in enumerate(nums) if x]


print(find_duplicates(nums_test2))