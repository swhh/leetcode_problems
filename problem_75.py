""""Given an array nums with n objects colored red, white, or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
You can only use constant space and only make one pass through the list"""

test_nums1 = [2, 0, 2, 1, 1, 0]
test_output1 = [0, 0, 1, 1, 2, 2]

test_nums2 = [2, 0, 1]
test_output2 = [0, 1, 2]


def swap(array, i, j):
    item = array[i]
    array[i] = array[j]
    array[j] = item


def sort_colors(nums):
    """Sort nums in-place in one pass using constant space"""
    i = k = 0
    j = len(nums) - 1
    while i <= j:
        num = nums[i]
        if num == 0:
            swap(nums, i, k)
            k += 1
        elif num == 2:
            swap(nums, i, j)
            j -= 1
            continue
        i += 1
    return nums


print(sort_colors(test_nums1))
