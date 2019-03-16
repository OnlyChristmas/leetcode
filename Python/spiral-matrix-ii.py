'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        # Approach one
        res = [[ 0  for _ in range(n)] for _ in range(n)]    # 注意， 不可用 n *[n *[0]] 初始化
        right , down , up ,left = True, False, False, False
        i , j = 0 , 0
        for num in range(1 , n*n+1):
            if right:
                res[i][j] = num
                j += 1
                if j == n or res[i][j] != 0:
                    right, down = False, True
                    j -= 1
                    i += 1
                    continue
            if down:
                res[i][j] = num
                i += 1
                if i == n or res[i][j] != 0:
                    down, left = False, True
                    i -= 1
                    j -= 1
                    continue
            if left:
                res[i][j] = num
                j -= 1
                if j == -1 or res[i][j] != 0:
                    left, up = False, True
                    j += 1
                    i -= 1
                    continue
            if up:
                res[i][j] = num
                i -= 1
                if i == -1 or res[i][j] != 0:
                    up, right = False, True
                    i += 1
                    j += 1
                    continue
        return res
