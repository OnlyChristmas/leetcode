'''

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



'''



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Approach one
        if s == '' : return 0
        tmp = []
        num = 0
        for i in range(len(s)):
            if s[i] not in tmp:
                tmp.append(s[i])
                num = max(num, len(tmp))
            else:
                tmp =  tmp[tmp.index(s[i]) + 1:]
                tmp.append(s[i])
        return num
