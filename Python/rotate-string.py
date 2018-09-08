'''

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false

Note:
A and B will have length at most 100.

'''


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # Approach #1
        # Time:  O(n)
        # Space: O(1)
        # if A != B:
        #     for _ in range(len(A)):
        #         if A == B:
        #             return True
        #         A = A[1:] + A[0]
        #     return False
        # return True


        # Approach #2   不等长的字符串不可能是 True
        # Time:  O(n^2)
        # Space: O(n)
        return len(A) == len(B)  and B in 2 * A
