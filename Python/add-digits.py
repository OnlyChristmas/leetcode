'''

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

'''


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # method one 数字与字符串的转换
        # while num > 9:
        #     num = sum([int(_) for _ in str(num)])
        # return num

        # method two 直接操纵int
        while num > 9:
            sumnum = 0
            while num > 0:
                sumnum += num % 10
                num //=  10
            num = sumnum
        return num
