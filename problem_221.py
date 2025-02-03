"""Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area."""
from functools import cache


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix2 = [["0","1"],["1","0"]]
matrix3 = [["0","0"],["0","0"]]



def maximal_square(matrix):
    n = len(matrix)
    m = len(matrix[0])
    k = min(n, m)

    @cache
    def recurse_max_square(i, j, k):
        if k == 1:
            return matrix[i][j] == '1'
        return all(recurse_max_square(a, b, k - 1) for a in range(i, min(i + k, n)) for b in range(j, min(j + k, m)))  
                   
    while k:
        for i in range(n - k + 1):
            for j in range(m - k + 1):
                print(i, j, k)
                if recurse_max_square(i, j, k):
                    return k ** 2
        k -= 1
    return k ** 2



print(maximal_square(matrix))



        