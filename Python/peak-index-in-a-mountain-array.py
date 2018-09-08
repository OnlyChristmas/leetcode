'''

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.

'''


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # method one 愚蠢的遍历
        # for i in range(1,len(A)):
        #     if A[i] < A[i+1]:
        #         i += 1
        #     else:
        #         return i


        # method two 改进版本 ,二分查找（比较序列中的相邻元素）
        left = 1
        right = len(A) - 2
        while left < right:
            mid = (right + left) // 2
            # print(mid,A[mid],A[mid+1])
            if A[mid] < A[mid+1]:
                left = mid + 1
            if A[mid] > A[mid+1]:
                right = mid
        return left


    
