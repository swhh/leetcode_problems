
"""You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104"""

def binary_search(row:list[int], target: int):
        """Perform binary search and return place where target should be if not present"""
        low, high = 0, len(row) - 1
        while low <= high:
            mid = (high + low) // 2
            if row[mid] == target:
                return mid, mid            
            elif row[mid] > target:
                if high == low:
                     return -1, high - 1
                high = mid - 1
            else:
                 if high == low:
                     return -1, high
                 low = mid + 1
        return -1, -1

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Approach: Find row target should be in with binary search and then find column with binary search"""
    if target < matrix[0][0]:
         return False
    _, right_row = binary_search([row[0] for row in matrix], target)
    right_column, _ = binary_search(matrix[right_row], target)
    if right_column != -1:
       return True
    return False

if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(search_matrix(matrix, 23))
