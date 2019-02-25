'''

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

'''


class Solution:
    def isIsomorphic(self, s: 'str', t: 'str') -> 'bool':

        # Approach one
        # dic = {}
        # s = list(s)
        # for i,n in enumerate(t):
        #     if dic.get(s[i], 0) == 0 and n not in dic.values():
        #         dic[s[i]] = n
        #     elif dic.get(s[i], 0) == n:
        #         s[i] = n
        #     else:
        #         return False
        # return True



        # Approach two
        trans=str.maketrans(s,t)     # 将 s,t 建立映射关系，
        return t==s.translate(trans) and len(set(s)) == len(set(t))     # 保证映射的唯一性
