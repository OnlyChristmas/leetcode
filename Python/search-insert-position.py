'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0

'''




class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Approach #1
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     for index,num in enumerate(nums):
        #         if target < nums[0]:
        #             return 0
        #         if target > nums[-1]:
        #             return len(nums)
        #         if num < target and nums[index+1] > target:
        #             return index+1



        # Approach #2
        # left , right = 0 , len(nums) - 1
        # if target < nums[left]:
        #     return 0
        # if target > nums[right]:
        #     return len(nums)
        # if target in nums:
        #     return nums.index(target)
        # while right - 1 > left :
        #     mid = ( left + right ) // 2
        #     if  target < nums[mid]:
        #         right = mid
        #     elif nums[mid] < target:
        #         left = mid
        #     if nums[mid] == target:
        #         return mid
        # return left + 1


        # Approach #3  简化方法二
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (j - i) // 2 + i
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return i+1 if nums[i] < target else i   # 最后要写nums[i]而不是nums[0]，因为需要处理二分查找失败的输入。



