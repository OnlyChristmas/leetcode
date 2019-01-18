'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # Approach #1 以主串为主干，进行一次遍历。边界条件比较多，不容易一次考虑周全。
        # Time:  O()
        # Space: O()
        #
#         substr_len =  len(needle)
#         str_len = len(haystack)

#         if substr_len  == 0: return 0
#         if substr_len <= str_len:               # 考虑子串比主串更长的情况
#             for i in range(str_len):            #  主字符串遍历一次
#                 if haystack[i] == needle[0] and str_len - i >= substr_len:
#                     for j in range(substr_len):
#                         if  i+j >= str_len  or haystack[i+j] != needle[j] :          # 小心主串越界
#                             break
#                         elif haystack[i+j] == needle[j] and j == substr_len - 1:
#                             return i
#                 elif str_len - i < substr_len or i == str_len-1:      # 主串过短，无法完成匹配，提前终止。  主串匹配到了最后一个字符也无法匹配的特殊情况 "mississippi"  "a"
#                     return -1
#         else:
            # return -1


        # Approach #2 是不是有点投机的嫌疑？ 直接用字符串的内建函数s.find()
        # Time:  O(1)
        # Space: O(1)
        #
        # if(len(needle)==0):
        #     return 0
        # else:
        #     return haystack.find(needle)


        # Approach #3
        # Time:  O(n)
        # Space: O(1)
        #
        for i in range(len(haystack)-len(needle)+1):   # 有效减少比较的次数
            if haystack[i:i+len(needle)]==needle:       #　字符串切片操作可以直接比较一个子串，不用每个字符都比较
                return i                              # i 为 0 的时候， haystack[0:0] 表示为 0
        return -1
