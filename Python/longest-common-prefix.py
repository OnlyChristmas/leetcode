'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.

'''






class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # 思路一： 一个笨方法
#         length = 0
#         leng = 10000
#         for s in strs :
#             if leng >= len(s):
#                 leng = len(s)
#                 mins = s

#         if len(strs)<1 or mins == "": return ""       # 考虑字符串列表或者字符串为空的特殊情况

#         for i in range( len(mins) ):
#             for j in range(len(strs)):
#                 print(strs[j][i],mins[i])
#                 if strs[j][i] == mins[i] and j == len(strs)-1:
#                     length += 1
#                     if len(mins)-1 == i :
#                         return mins[:length]
#                 if strs[j][i] != mins[i] :
#                     return mins[:length]


        # 思路二： 排序法，代价不低：
        # if strs == []:
        #     return ''
        # lista = sorted(strs,key=len)  # 可以应用在所有可迭代对象的高阶函数sorted()简化思路一
        # str1=lista[0]
        # str_common = ''               # 直接用字符串存储返回值，然不是返回的整数位数，减少一部转化过程
        # for j in range(len(str1)):
        #     for i in range(1,len(lista)):    # 不用和自己比较，提高一点效率
        #         if lista[i][j] != str1[j]:   # 更简化的判断条件
        #             return str_common
        #     str_common = str_common + str1[j]
        # return str_common



        # 排序法更精简的写法,只需要比较第一个和最后一个的公共前缀：

        if not strs:
            return ''
        strs.sort()                        # sort()函数只用于列表的排序，字符串默认升序
        print(strs)
        res = ''
        for i in range(len(strs[0])):
            if strs[-1][i] != strs[0][i]:   # 省略中间的比较，提高效率
                return res
            res += strs[0][i]
        return res









