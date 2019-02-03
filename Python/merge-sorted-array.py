'''

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]


'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # Approach one   效率低
        # a = m - 1
        # b = n - 1
        # k = m+n-1
        # if n > 0:                # List[int] == []
        #     print(nums1,m,nums2,n)
        #     if m == 0: nums1[:] = nums2     # nums1  被赋值必须加上 [:]
        #     else:
        #         while k >= 0:
        #             if  nums1[a] >= nums2[b]:
        #                 nums1[k] = nums1[a]
        #                 if a == 0 and nums2[b] != -10000:
        #                     nums1[0] = -10000
        #                 else:
        #                     a -= 1
        #             else:
        #                 nums1[k] = nums2[b]
        #                 if b == 0 and nums1[a] != -10000:
        #                     nums2[0] = -10000
        #                 else:
        #                     b -= 1
        #             k -= 1

        # Approach two
        nums1[m:] = nums2
        nums1.sort()
