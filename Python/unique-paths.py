'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right


Example 2:
Input: m = 7, n = 3
Output: 28



'''




class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        # Approach two  节省存储空间
        dp = [1 for _ in range(m)]
        for i in range(1,n):
            for j in range(1,m):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]




        # Approach one
        # dp = [[0 for _ in range(m)]  for _ in range(n)]
        # dp[0] = [1 for _ in range(m)]
        # for i in range(n):
        #     dp[i][0] = 1
        # for i in range(1,n):
        #     for j in range(1,m):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[n-1][m-1]
