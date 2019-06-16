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
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach one  尾递归
        # 因为是尾部, 所以根本没有必要去保存任何局部变量. 直接让被调用的函数返回时越过调用者, 返回到调用者的调用者去。
        # 尾递归就是把当前的运算结果（或路径）放在参数里传给下层函数，深层函数所面对的不是越来越简单的问题，而是越来越复杂的问题，因为参数里带有前面若干步的运算路径。
        # 有效减少堆栈的消耗
        # 但仍旧存在大量冗余运算，输入个100，计算复杂度就会爆炸
        # if n <= 2: return n
        # return self.climbStairs(n-1) + self.climbStairs(n-2)



        # Approach two
        # 循环替代递归, 减少冗余计算
        if n < 0 : return
        a , b = 1 , 2
        for i in range(3,n+1):
            a , b = b , a + b
        return b if n > 1 else n
