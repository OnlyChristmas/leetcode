'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

'''



class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 相当于一个有限制的字符串逆序，只对字符串中的元音字母进行逆序。

        # Approach #1
        # vowels = ('a','e','i','o','u','A','E','I','O','U')
        # ss = [i for i in s if i in vowels]
        # return ''.join([ss.pop() if i in vowels else i for i in list(s)  ])


        # Approach #2
        # import re
        # ss = re.findall('[aeiouAEIOU]',s)     # 返回一个列表
        # return re.sub('[aeiouAEIOU]',lambda m: ss.pop() ,s)


        # Approach #3  代码效率比上面方法低
        # import re
        # return re.sub('(?i)[aeiou]', lambda m, v=re.findall('(?i)[aeiou]', s): v.pop(), s)  # re.sub(arg1,arg2,arg3)  arg3中找到arg1, 并且替换为arg2(arg2可为函数



        # Approach #4
        vowels = "aeiouAEIOU"
        ss = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if ss[i] not in vowels:
                i += 1
            elif ss[j] not in vowels:
                j -= 1
            else:
                ss[i], ss[j] = ss[j], ss[i]
                i += 1
                j -= 1
        return "".join(ss)

        
