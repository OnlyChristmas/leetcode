'''

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

'''


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Approach one  用498题思路解答，代码可读性强，但效率有待提升
#         if matrix == [] : return []
#         row , col = len(matrix) , len(matrix[0])
#         i = j = upper_bound = left_bound = 0
#         ans = []
#         count = row * col
#         down = up = left = False
#         right = True
#         while count:
#             count -= 1
#             ans.append(matrix[i][j])
#             if up:
#                 if i == upper_bound:
#                     up, right = False, True
#                     left_bound += 1
#                     j += 1
#                     continue
#                 else:
#                     i -= 1
#             if left:
#                 if j == left_bound:
#                     left, up = False, True
#                     row -= 1
#                     i -= 1
#                     continue
#                 else:
#                     j -= 1
#             if down:
#                 if i == row -1:
#                     down, left = False, True
#                     col -= 1
#                     j -= 1
#                     continue
#                 else:
#                     i += 1
#             if right:
#                 if j == col -1:
#                     right, down = False, True
#                     upper_bound += 1
#                     i += 1
#                     continue
#                 else:
#                     j += 1
#         return ans



        # # Approach two   简化代码
        # if matrix == []: return []
        # ans=[]
        # row , col = len(matrix) , len(matrix[0])
        # # flag = row * [ col * [1]]   # 这种初始化方式为什么有毒？
        # flag =  [[1 for i in range(col)] for i in range(row)]   # 保证每个元素只被添加一次
        # direction = 0  # 代表四个方向
        # i = j = pre_i = pre_j = 0
        # count = row * col
        # while len(ans) < count:
        #     if i >= row or j >= col or i < 0 or j < 0 or flag[i][j]==0:
        #         direction = (direction+1) % 4    # 控制转向
        #         i, j = pre_i, pre_j
        #         if direction==0:
        #             j=j+1
        #         elif direction==1:
        #             i=i+1
        #         elif direction==2:
        #             j=j-1
        #         elif direction==3:
        #             i=i-1
        #     elif flag[i][j] == 1:
        #         flag[i][j] = 0
        #         ans.append(matrix[i][j])
        #         pre_i, pre_j = i, j
        #         if direction==0:
        #             j=j+1
        #         elif direction==1:
        #             i=i+1
        #         elif direction==2:
        #             j=j-1
        #         elif direction==3:
        #             i=i-1
        # return ans





        # Approach three   进一步简化代码，丧失易读性
        if not matrix:return []
        row, col = len(matrix), len(matrix[0])
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        x, y = 0, -1
        boundary = [col - 1, row - 1, 0, 0]
        ans = []
        k = 0
        count = row * col
        while count:
            count -= 1
            x += dx[k]
            y += dy[k]
            ans.append(matrix[x][y])
            if k % 2 == 0 and y == boundary[k] or k % 2 == 1 and x == boundary[k]:
                o = (k - 1) % 4
                boundary[o] += 1 if o >= 2 else -1
                k = (k + 1) % 4
        return ans

            
