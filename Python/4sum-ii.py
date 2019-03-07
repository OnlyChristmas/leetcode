'''

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

'''



class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        # Approach one
        # length = len(A)
        # res = 0
        # dic = {}
        # for i in range(length):
        #     for j in range(length):
        #         twosum = A[i] + B[j]
        #         dic[twosum] = dic.get(twosum, 0) + 1
        # for i in range(length):
        #     for j in range(length):
        #         res += dic.get(- C[i] - D[j], 0)
        # return res


        # Approach two
        from collections import Counter
        dicA , dicB ,dicC ,dicD = Counter(A), Counter(B), Counter(C), Counter(D)
        res = 0
        dic = {}
        for a , a_nember in dicA.items():
            for b , b_nember in dicB.items():
                dic[a+b] = dic.get(a+b,0) + a_nember * b_nember
        for c, c_nember in dicC.items():
            for d, d_nember in dicD.items():
                res += dic.get(-c-d,0) * c_nember * d_nember
        return res
