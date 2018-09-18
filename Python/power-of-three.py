'''
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
'''




class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Approach #1 低效的循环
        # if n :
        #     while n % 3 == 0:
        #         n /= 3
        #     return n == 1
        # return False


        # Approach #2     3 ** 19 == 1162261467
        return n > 0 and 1162261467 % n == 0
