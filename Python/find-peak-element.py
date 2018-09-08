'''

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.
'''




class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        # method one 一个笨办法，借助max()函数
#         id = nums.index(max(nums))
#         if id == 0 or id == len(nums)-1:
#             return id
#         if nums[id-1] < nums[id] and nums[id+1] < nums[id]:
#             return id


        # method two 笨办法改良版，考虑了过多的边界条件
        # return nums.index(max(nums)



        # method three 认真学习一下二分查找，提升效率.  仔细考虑左右两个指针的位置变换，很容易死循环

        left , right = 0 , len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid]  > nums[mid+1]:
                right = mid
            elif  nums[mid] < nums[mid + 1]:
                left = mid + 1
        return left
