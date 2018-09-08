'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.


Example:
Input: 19
Output: true

Explanation:
$1^2 + 9^2 = 82$
$8^2 + 2^2 = 68$
$6^2 + 8^2 = 100$
$1^2 + 0^2 + 0^2 = 1$
'''




class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 考虑递归的终止条件，不能收敛为 1 的数字怎么办？
        # 不能收敛为1 的数字一般都是循环结构，寻找数学规律

        # method one  字符串与整数的转换

        # if n < 10:
        #     if n == 1 or n == 7:
        #         return True
        #     else:
        #         return False
        # return self.isHappy(sum([int(i)**2 for i in str(n)]))




        # method two  地板除与取余
        if n < 10:
            if n == 1 or n == 7:
                return True
            else:
                return False
        new_n = 0
        while n:
            new_n += (n % 10)**2
            n //= 10
        return self.isHappy(new_n)





    
