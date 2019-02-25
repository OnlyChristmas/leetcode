'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false

'''



class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 思路一： 手写替换的字母，显然很蠢……
        # import re
        # ss = re.sub('[:,` ;.@!?#$%^&*\(\)_+=\-\[\]\{\}\\\|\'\"\<\>]' , '' , s.lower())    # 一个详细的去字符操作……决定你的通过次数
        # return ss[::-1] == ss


        # 思路二： 聪明一点的做法（正则表达）
        # import re
        # s = re.sub('[^a-z0-9]','',s.lower())
        # return s == s[::-1]

         # 思路三： 聪明小哥哥的做法 ,但效率不如方法二
        s = list(filter(str.isalnum, s.lower()))
        return s == s[::-1]
        # isalnum() 检测字符串是不是由字母和数字组成（作为arg2的筛选条件）
        # filter()是一个高阶函数，其关键在于arg1的筛选函数。  filter()是一个惰性函数，需要套用list()来迫使其完成运算。
