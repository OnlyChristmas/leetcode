'''
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:
S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

'''


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # method one 笨方法，计算量大
        # dic = {}
        # res = []
        # for index,s in enumerate(S) :
        #     if s == C:
        #         dic[index] = s
        # for i in range(len(S)):
        #     tmp = []
        #     for key in dic.keys():
        #         tmp.append(abs(key-i))
        #     res.append(min(tmp))
        # return res

        # method one 笨方法的骚操作
        # return [min(abs(i - ll) for ll in [i for i, e in enumerate(S) if e == C]) for i in range(len(S))]

        # method two 寻找每个字符左右相邻的C字符, 简化运算
        # res = []
        # for i in range(len(S)):
        #     left , right = S[i-len(S)::-1].find(C) , S[i:].find(C)
        #     if left == -1: left = 10000
        #     if right == -1: right = 10000
        #     res.append(min(left , right))
        # return res



        # Approach #3 用双指针替代遍历C序列，但是有可能第二个指针不存在。
        Alist = [i   for i,num in enumerate(S) if num == C]
        res, length, L = [] , 0 , len(Alist)
        for i in range(len(S)):
            if L >= 2:
                a , b = abs(Alist[length] - i) , abs(Alist[length + 1] - i)
                if a < b:
                    res.append(a)
                else:
                    res.append(b)
                    if length < L-2:
                        length +=1
            else:
                res.append(abs(Alist[length] - i))
        return res



        
