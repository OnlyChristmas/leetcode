'''


The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

'''


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        # method one 强行一行解，代码可读性差，程序效率低
        # return  sum(list(map(lambda x , y : int(x)  ^ int(y) , (max(len(bin(x)),len(bin(y))) - len(bin(x)))*[0] + list(bin(x)[2:]) ,(max(len(bin(x)),len(bin(y))) - len(bin(y)))*[0] + list(bin(y)[2:]))))


        # method two  二进制整数可以直接异或,最简代码
        return bin(x^y).count('1')        # bin() 返回的是一个 前缀为 ”ob“ 的字符串
