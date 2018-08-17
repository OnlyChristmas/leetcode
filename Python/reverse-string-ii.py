'''
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]

'''

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Approach #1 字符串的切片和反序操作不能同时进行
        # Time:  O(n)
        # Space: O(1)

        res = ''
        for i in range(0,len(s),2*k):
            res = res + s[i:i+k][::-1] + s[i+k:i+2*k]
        return res
