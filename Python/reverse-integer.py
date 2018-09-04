'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''





class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 思路一：利用字符串的反转（简单但效率略低）
        # if x == 0 : return 0   # 单独处理返回0的情况，反转后有符号整数的范围，仔细审题！
        # s = int(str(x).strip('0-')[::-1])
        # if -2**31 < s and s <= (2**31 - 1):
        #     if x < 0:
        #         return -s
        #     return s
        # else:
        #     return 0


        # 思路二： 根据取余操作反转整数
        y = 0
        neg = x < 0
        if neg:
            x = -x
        while x > 0:   # 特殊情况0 ， 直接返回，不用操作
            y *= 10
            y += x % 10
            x //= 10   # 地板除，小数部分全部忽略
        if neg:
            y = -y
        if y > 2**31-1 or y<-2**31:
            return 0
        return y


