'''

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:
Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011

Example 2:
Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # method one  用内置函数
        # return bin(n).count('1')

        # method　two 用位操作
        # num = 0
        # while n:
        #     num += n % 2
        #     n //= 2
        # return num

        # Approach #3
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result
