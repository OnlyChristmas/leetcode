'''

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.

'''



class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Approach one 空间换时间，将暴力解法O(n^2)的复杂度降为O(n)
        # dic = dict()
        # for i in s:
        #     dic[i] = dic.get(i,0) +1
        # for i,n in enumerate(s):
        #     if dic.get(n,0) == 1:
        #         return i
        # return  -1


        # Approach two  因为候选的字符有限，可以从字符的角度循环，不需要辅助的存储空间，还能加速运算
        res = [s.index(i) for i in string.ascii_lowercase if s.count(i) == 1 ]
        return min(res) if res else -1
