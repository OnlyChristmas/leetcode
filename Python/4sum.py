'''

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


'''



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Approach one    O(n3)
        # from collections import Counter
        # dic = Counter(nums)
        # res = []
        # nums = sorted(nums)
        # length = len(nums) - 1
        # for i in range(length-2):
        #     if i != 0 and nums[i] == nums[i - 1]: continue     # 避免重复答案
        #     key = target - nums[i]
        #     for j in range(i + 1, length-1):
        #         if j != i + 1 and nums[j] == nums[j - 1]: continue   # 避免重复答案
        #         twosum = key - nums[j]
        #         l,r = j+1 , length
        #         while l < r:
        #             ans = nums[l] + nums[r]
        #             if twosum < ans:
        #                 r -= 1
        #             elif twosum == ans:
        #                 res.append([nums[i],nums[j],nums[l],nums[r]])
        #                 r -= 1
        #                 while nums[r] == nums[r + 1] and l < r:
        #                     r -= 1
        #                 l += 1
        #                 while nums[l] == nums[l - 1] and l < r:
        #                     l += 1
        #             else:
        #                 l += 1
        # return res



        # Approach two  O(n2)
        res = set()
        nums = sorted(nums)
        length = len(nums)
        dic = {}
        if length < 4 or 4 * nums[0] > target or 4 * nums[-1] < target: return []
        for i in range(length-1):
            for j in range(i+1,length):
                twosum = nums[i] + nums[j]
                if twosum in dic.keys():
                    dic[twosum].append((i,j))
                else:
                    dic[twosum] = [(i,j)]
        for i in range(length-1):
            for j in range(i+1,length):
                ans = target - nums[i] - nums[j]
                if dic.get(ans, 0) != 0:
                    for k in dic.get(ans):
                        if k[0] > j:
                            res.add((nums[i] , nums[j] , nums[k[0]] , nums[k[1]] ))
        return list(res)
