'''
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5


'''




class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 如果分割后左右的数字相等，那么分割点就是我们要找的。
        # 两个数组的总长度一定，确定一个数组的分割点另一个必然随之确定。
        # 那么找第一个分割点在短的数组找效率会更高，二分查找。

        m,n = len(nums1),len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n ,m
        if m == 0:
            return (nums2[n//2] + nums2[(n-1)//2] )/2                # 获取排序数字中位数，考虑奇偶性
        l , r = 0 , m
        k = (m + n + 1)//2
        while l < r:
            c1 = l + (r-l)//2
            c2 = k-c1
            if nums1[c1] < nums2[c2-1]:
                l = c1 +1
            else:
                r = c1
        c1 = l
        c2 = k - c1
        res1 = max(nums1[c1-1] if c1 > 0 else float("-inf"), nums2[c2-1] if c2 > 0 else float("-inf") )
        if (m + n) % 2 == 1:
            return res1
        res2 = min(nums1[c1] if c1 < m else float("inf"), nums2[c2] if c2 <n else float("inf"))
        return (res1 + res2) / 2
