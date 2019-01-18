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
        # Approach #1： 0 个数多的时候效率低下，注意remove（）与del 操作的区别，如果用del操作，列表需要倒序遍历。
        #
#         for i in nums:
#             if i == 0:
#                 nums.remove(i)
#                 nums.append(0)

        # Approach #2   删除0，添加0
        # count, length  = 0, len(nums)
        # while count != length:
        #     if nums[count] == 0:
        #         del nums[count]
        #         nums.append(0)
        #         count -= 1
        #         length -= 1
        #     count += 1

        # Approach #3 复制非0，添加零
        # length, new_id = len(nums), 0
        # for i in range(length):
        #     if nums[i] != 0:
        #         nums[new_id] = nums[i]
        #         new_id += 1
        # nums[new_id:] = [0] * (length - new_id)


        # Approach #4： 删除后一次性补零，减少元素位移
        #
        # idxs = [idx for idx , num in enumerate(nums) if num == 0]
        # for i in idxs[::-1]:
        #     nums.pop(i)
        # nums += len(idxs) *[0]




        # Approach #5： 减少交换次数（操作次数就是非零元素的个数）
        # Time:  O(n)
        # Space: O(1)
        #
        j = 0   # 记录非零元素应该换到第几个位置
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
