'''

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false


'''



class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # Approach one
        # if matrix == [] or matrix == [[]]: return False
        # length = len(matrix[0]) - 1
        # for i in range(len(matrix)):
        #     if matrix[i][-1] < target: continue
        #     elif matrix[i][-1] == target: return True
        #     else:
        #         for j in range(length):
        #             if matrix[i][0] > target: return False
        #             if matrix[i][j] == target: return True
        # return False



        # Approach two   从中间开始寻找
#         if matrix == [] or matrix == [[]]: return False
#         row , col = len(matrix) - 1 , 0
#         cols = len(matrix[0])
#         while row >= 0 and col < cols:
#             if matrix[row][col] == target: return True
#             elif matrix[row][col] > target:
#                 row -= 1
#             else:
#                 col += 1
#         return False




        # Approach three
        return  any(target in row  for row in matrix)
