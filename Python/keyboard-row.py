'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.


'''

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """


        #　method once  初始化太复杂了
        # Time:  O(n^2)
        # Space: O(n)
        #
#         res = []
#         ref = [['q','w','e','r','t','y','u','i','o','p'],
#               ['a','s','d','f','g','h','j','k','l'],
#                ['z','x','c','v','b','n','m']]
#         for i in words:
#             ss = "".join(set(i.lower()))     # 要处理大小写问题
#             for j in ref:
#                 for k in ss:
#                     if  k not in j:
#                         break
#                     elif k == ss[-1]:
#                         res.append(i)
#         return res


        # method twice  用str的内置函数str.issubset()更加简洁
        # Time:  O(n)
        # Space: O(n)
        #
        # line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        # res = []
        # for word in words:
        #     ss = set(word.lower())
        #     if ss.issubset(line1) or ss.issubset(line2) or ss.issubset(line3):
        #         res.append(word)
        # return res



        # method third  本质上和方法二是一样的，只是用all()函数替换了issubset()函数
        # Time:  O(n)
        # Space: O(n)
        #
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        res = []
        for word in words:
            smallword = word.lower()
            if all([x in line1 for x in smallword]) or all([x in line2 for x in smallword]) or all([x in line3 for x in smallword]):
                res.append(word)
        return res


