'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

'''


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # Approach one
        # 与比较两个字符串的最长公共字串的思路完全一致。
        # 确定最小子问题、确定边界条件，确定状态转移方程
        # dp = triangle[-1]
        # for i in range(len(triangle)-2, -1,-1):
        #     for j in range( len(triangle[i])):
        #         dp[j] = triangle[i][j] + min(dp[j],dp[j+1])
        # return dp[0]


        # 重新实现
        if not triangle: return
        for i in range(len(triangle)-1, 0,-1):
            for j in range( len(triangle[i])-1):
                 triangle[i-1][j] += min(triangle[i][j],triangle[i][j+1])
        return triangle[0][0]
