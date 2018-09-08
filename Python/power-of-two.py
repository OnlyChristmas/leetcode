'''
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true
Explanation: 2^0 = 1

Example 2:
Input: 16
Output: true
Explanation: 2^4 = 16

Example 3:
Input: 218
Output: false
'''


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # once method
        # while int(n) == n and n != 0:
        #     if n == 1:
        #         return True
        #     n /= 2
        # return False



        # twice method
        # if n:
        #     while n % 2 == 0 :
        #         n /= 2
        #     return n == 1
        # return False

        # third method 简洁高效的位运算
        return n > 0 and not (n & n-1)
