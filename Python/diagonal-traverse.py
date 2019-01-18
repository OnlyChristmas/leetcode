'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.



Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:



Note:

The total number of elements of the given matrix will not exceed 10,000.

'''


class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Approach one   效率低
        # if matrix == []: return []
        # ans = []
        # row,col = len(matrix), len(matrix[0])
        # if row == 1: return matrix[0]
        # for num in range(row + col):
        #     if num % 2 == 0:
        #         for i in range(num+1):
        #             if i >= col:
        #                 break
        #             if num - i >= row:
        #                 continue
        #             ans.append(matrix[num - i][i])
        #     else:
        #         for i in range(num+1):
        #             if i >= row:
        #                 break
        #             if num - i >= col:
        #                 continue
        #             ans.append(matrix[i][num - i])
        # return ans


        # Approach two   不是用循环，免去遍历多余的数, 时间效率前100%
        if matrix == []: return []
        row,col = len(matrix), len(matrix[0])
        ans = []
        number = row * col
        i = j = 0
        up = True
        while number:
            number -= 1
            ans.append(matrix[i][j])
            if up:
                if j == col - 1:
                    i += 1
                    up = False
                elif i == 0:
                    j += 1
                    up = False
                else:
                    i -= 1
                    j += 1
            else:
                if i == row - 1:
                    up = True
                    j += 1
                elif j == 0:
                    i += 1
                    up = True
                else:
                    i += 1
                    j -= 1
        return ans


        
