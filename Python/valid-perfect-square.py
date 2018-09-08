'''

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false

'''



class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # method one 简单的遍历，低效
        # for i in range(num+1):
        #     if i*i > num:
        #         return False
        #     if i*i == num:
        #         return True





        # method two 二分查找
        # l , r = 0 , num
        # while l <= r:
        #     mid = (l+r)//2
        #     N = mid ** 2
        #     if N < num and (mid + 1)**2 > num:
        #         return False
        #     if N == num:
        #         return True
        #     if N < num:
        #         l = mid + 1
        #     if N > num:
        #         r = mid




        # method three  根据数学性质验证，效率比二分法更高 
        return int(num**0.5) == num**0.5
