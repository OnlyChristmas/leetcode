'''

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 思路一： 0 个数多的时候效率低下
#         for i in nums:
#             if i == 0:
#                 nums.remove(i)
#                 nums.append(0)

        # 思路二： 逆向循环避免多余操作（操作次数是，0个数的两倍）
        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i] == 0:
        #         del nums[i]
        #         nums.append(0)


        # 思路三： 移动非零元素（操作次数就是非零元素的个数）
        j = 0   # 记录非零元素应该换到第几个位置
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
