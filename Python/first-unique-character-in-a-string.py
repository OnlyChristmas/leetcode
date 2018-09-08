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
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """


        # 思路一： 最直观的双重循环想法， TLE
#         length = len(s)

#         for i in range(length):
#             for j in range(length):
#                 if s[i] == s[j] and i != j:

#                     break          # 提前中断可以提高效率
#                 elif j == length-1 :
#                     return i
#         return -1                  # 解决没有只出现一次的字符的情况（例如空字符串）


        # 思路二： 建立数组的方法(对输入s只遍历两次)
#         number= []
#         dic = {}
#         for i in range(len(s)):
#             if s[i] not in number:
#                 number.append(s[i])
#                 dic[s[i]] = 1
#             else:
#                 dic[s[i]] += 1

#         for j in range(len(number)):
#             if dic.get(number[j]) == 1:
#                 for k in range(len(s)):
#                     if s[k] == number[j]:
#                         return k
#         return -1






        # Approach #3
        res = [s.index(label) for label in  string.ascii_lowercase if s.count(label) == 1]
        return  min(res) if res != [] else -1
