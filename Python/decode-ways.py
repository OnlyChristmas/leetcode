'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


'''




class Solution:
    def numDecodings(self, s: str) -> int:

        # 注意不从0开始编码，一个有约束的动规。
        if len(s) < 1 : return 0
        a , b = 1 , int(s[0] != '0')
        for i in range(1,len(s)):
            a , b = b , a * (10 <= int(s[i-1:i+1]) <= 26 ) + b * (int(s[i]) > 0)
        return b
