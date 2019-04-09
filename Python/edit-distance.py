'''

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''




class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # 经典DP
        # 对于DP来说，迭代一般是比递归更好的选择。一方面递归容易栈溢出；另一方面，不断地函数调用也会消耗很多时间。
        # 对于迭代，有两个角度。   1、我为人人   2、人人为我
        # 如果前面是有两个参数向后传递，一般这时的dp是一个二维矩阵的形式（当然可以压缩存储）；如果只有一个函数向后传递，就是一个简单的一维向量就可以存储。
        # [教你彻底学会动态规划——入门篇](https://blog.csdn.net/baidu_28312631/article/details/47418773)
        # [教你彻底学会动态规划——进阶篇](https://blog.csdn.net/baidu_28312631/article/details/47426445)


        # 1、根据题意，将本问题分解为子序列的编辑距离，符合后效性。dp[i][j]表示将字符串 A[0: i-1] 转变为 B[0: j-1] 的最小步骤数。
        # 2、初始化矩阵dp[m+1][n+1]的两个边界，分别为range(0，m+1)以及range(0,n+1)的单调递增序列。
        # 3、三种操作构造状态转移方程。
        #     插入操作：dp[i][j - 1] + 1 相当于为 B 串的最后插入了 A 串的最后一个字符；
        #     删除操作：dp[i - 1][j] + 1 相当于将 B 串的最后字符删除 ;
        #     替换操作：dp[i - 1][j - 1] +（A[i - 1] != B[j - 1]）相当于通过将 B 串的最后一个字符替换为 A 串的最后一个字符。

        




        # Approach one
        # m = len(word1)
        # n = len(word2)
        # if m == 0 : return n
        # if n == 0 : return m
        # dp = [[0]*(n+1) for i in range(m+1)]              # 初始化边界条件
        # for i in range(m+1):
        #     dp[i][0] = i
        # for j in range(n+1):
        #     dp[0][j] = j
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         if word1[i-1] == word2[j-1]:          # 状态转换方程的两种情况。
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
        # return dp[m][n]




        # Approach two   用一维数组优化存储空间，不过bug free的难度要高于上述方法
        m = len(word1)
        n = len(word2)
        if m == 0 : return n
        if n == 0 : return m
        cur = [i for i in  range(m+1)]
        for i in range(1,n+1):
            pre, cur[0] = cur[0], i
            for j in range(1, m+1):
                tmp = cur[j]
                if word1[j-1] == word2[i-1]:
                    cur[j] = pre
                else:
                    cur[j] = min(cur[j-1], cur[j], pre)+1
                pre = tmp
        return cur[m]
