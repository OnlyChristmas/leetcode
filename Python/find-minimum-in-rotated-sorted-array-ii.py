'''

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0

Note:
This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?

'''



class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # method one
        # return min(nums)



        # method two  二分法难点，在于左右节点和中间结点一样的时候，不知道最小值的区间
        left , right = 0 , len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[right]:              # 关键的去重，不能每次舍弃一半的元素，而只能逐个筛选
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
