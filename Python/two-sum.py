'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''





class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 一个能用，但是效率并不高的算法(因为用了两个循环)
#         dic = {}
#         length = len(nums)
#         for i in range(length):
#             dic[nums[i]] = i

#         for i in range(length):     # 考虑一个target由两个相同的数字组成。例如[3,3] 6
#             res =  target - nums[i]
#             if res in dic.keys() and dic.get(res) != i:
#                 return [i, dic.get(res)]


        # 对数组的两次遍历缩减为一次。边做字典边检测
        hashed = {}
        for i in range(len(nums)):
            if target-nums[i] in hashed: return [hashed[target-nums[i]], i]   # 某对数字是答案的话，先将第一个数字存进去，遍历到第二个数字的时候就会检测成功.
            hashed[nums[i]] = i
            # return 的时候要注意顺序，第一次放入的（target-nums[i]）比较小，要放在前面，否则返回值错误
