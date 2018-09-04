'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''




class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # Approach #1
        # return bin(int(a,2)+int(b,2))[2:]

        # Appraoch #2
        # format()函数直接转换进制。   二进制（b）、十进制（d）、八进制（o）、十六进制（x）
        return format(int(a,2)+int(b,2),"b")
