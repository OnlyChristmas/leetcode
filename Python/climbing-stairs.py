'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''





class Solution:
    # def __init__(self):
    #         self.dic = {1:1, 2:2}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 这道题本质上是一个斐波那契数列,因为后一个数总是等于前两个数字之和!

        # 思路一:  Top down - TLE  因为前面已经算过的数字不能直接调用,总是需要重新计算.
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # if n > 2:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)

        # Top down + memorization (list) 对于思路一的改进
#         def climbStairs4(self, n):
#             if n == 1:
#                 return 1
#             dic = [-1 for i in xrange(n)]
#             dic[0], dic[1] = 1, 2
#             return self.helper(n-1, dic)

#         def helper(self, n, dic):
#             if dic[n] < 0:
#                 dic[n] = self.helper(n-1, dic)+self.helper(n-2, dic)
#             return dic[n]

        # Top down + memorization (dictionary)  对于思路一的改进,用一个字典来存储前面计算过的部分,减少运算时间
        # if n not in self.dic:
        #     self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        # return self.dic[n]




        # Bottom up, O(n) space  思路二:自底向上. 保存前面计算过的数字,用空间来换取时间
        # if n == 1:
        #     return 1
        # res = [0 for i in range(n)]
        # res[0], res[1] = 1, 2
        # for i in range(2, n):
        #     res[i] = res[i-1] + res[i-2]
        # return res[-1]

        # Bottom up, O(n) space  思路二:自底向上. 进一步压缩占用的存储空间
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            a,b = b,a+b
        return b


