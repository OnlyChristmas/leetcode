'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''





class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':


        # Approach one 低效
#         dic = {}
#         length = len(nums)
#         for i in range(length):
#             dic[nums[i]] = i

#         for i in range(length):     # 考虑一个target由两个相同的数字组成。例如[3,3] 6
#             res =  target - nums[i]
#             if res in dic.keys() and dic.get(res) != i:
#                 return [i, dic.get(res)]


        # Approach two
        # dic = {}
        # for i,n in enumerate(nums):
        #     m = target - n
        #     if n not in dic.keys():
        #         dic[m] = i
        #     else:
        #         return [dic.get(n),i]


        # Approach three  细节优化
        hashed = {}
        for i,n in enumerate(nums):
            if n in hashed: return  [hashed[n],i]
            hashed[target-n] = i
           
