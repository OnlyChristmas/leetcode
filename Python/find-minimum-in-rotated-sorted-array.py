'''

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.
You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
'''



class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # method one
        # return min(nums)

        # method two: 二分法
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2  # 地板除，舍去小数部分
            if nums[mid] < nums[right]:       # 移动右边显然是更安全的选择
                right = mid
            else:
                left = mid + 1
        return nums[left]
