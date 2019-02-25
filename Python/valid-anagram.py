'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false


Note:
You may assume the string contains only lowercase alphabets.
Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''



class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Approach one ：
        # if set(s) == set(t) and len(s) == len(t):
        #     for i in set(s):
        #         if s.count(i) != t.count(i):
        #             return False
        #     return True
        # return False

        # Approach two：一种更优雅的完成方式        all(iterable)：当 iterable 中所有元素都为 True 时（或者 iterable 为空），返回 True 。
        # return set(s) == set(t) and all(s.count(i) == t.count(i) for i in set(s))


        # Approach three
        return collections.Counter(s) == collections.Counter(t)
