'''
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.



Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.


'''



class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:

        # 三种情况
        # 1、 两个字符串长度不相等，必然错误
        # 2、 两个字符串完全一致，需要至少有一个字母存在超过两次
        # 3、 两个字符串恰好只有两个位置不一样（只发生了一次交换）

        # Approach one
        # if len(A) != len(B) : return False
        # if A == B:
        #     for i in range(97,123,1):
        #         if A.count(chr(i)) >= 2 :
        #             return True
        #     return False
        # else:
        #     res = {}
        #     for i,n in enumerate(A):
        #         if len(res.keys()) > 1 :return False
        #         if n != B[i]:
        #             if n not in res.values():
        #                 res[n] = B[i]
        #             if B[i] in res.keys() and n in res.values():
        #                 res[B[i]] = True
        #     for i in res.values():
        #         return  True == i


        # Approach two
        # if len(A) != len(B) : return False
        # if A == B:
        #     for i in range(97,123,1):
        #         if A.count(chr(i)) >= 2 :
        #             return True
        #     return False
        # else:
        #     res = [[i,j] for i,j in zip(A,B) if i != j]
        #     if len(res) != 2: return False
        #     else:  return res[0][::-1] == res[1]



        # Approach three
        if len(A) != len(B) : return False
        if A == B: return len(set(A)) < len(B)
        else:
            res = [[i,j] for i,j in zip(A,B) if i != j]
            return res[0][::-1] == res[1] and len(res) == 2
