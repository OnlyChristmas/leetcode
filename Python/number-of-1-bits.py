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


        # 复数的补码前面自动填充1
        # 方法一
        # return sum([(n>>i & 1) for i in range(0,32)])

        # 方法二
        # 标志位一路左移，做“与”操作
        #flag = 1
        #count = 0
        #for _ in range(32):
        #    if flag & n: count += 1
        #    flag = flag << 1
        #return count


        # python中 -4294967296 的二进制位 Ob0, 虽然一个负数在做了若干次“与”操作后，二进制为零，但是其十进制数是一个越来越小的负数
        # 因此在采用，“n与(n-1)做与操作恰好去掉n的最右位1”，这一性质时，终止条件不能以十进制来表示，否则是个死循环。
        # 方法三
        count = 0
        while n & 0xffffffff != 0:
            count += 1
            n = n & (n - 1)
        return count
