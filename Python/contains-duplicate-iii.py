'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false


'''


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        # Approach one    TLE
        # length = len(nums)
        # if length < 2 or t < 0: return False
        # l , r = 0 , 1
        # while l <= r:
        #     if r > length - 1: return False
        #     if abs(nums[r] - nums[l]) <= t:
        #         if 0 < r - l <= k:
        #             return True
        #         else:
        #             if r - l < k and r < length - 1:
        #                 r += 1
        #             elif r - l == k or r == length - 1:
        #                 l += 1
        #                 r = l+1
        #             else:
        #                 l += 1
        #     else:
        #         if r - l < k and r < length - 1:
        #             r += 1
        #         elif r - l == k or r == length - 1:
        #             l += 1
        #             r = l+1
        #         else:
        #             l += 1
        # return False



        # Approach two    低效
        # length = len(nums)
        # if length < 2 or t < 0 or k < 0: return False
        # dic = []
        # for i,n in enumerate(nums):
        #     if t == 0:     # 一个超长的例子需要特殊处理
        #         if n in dic:
        #             return True
        #     else:
        #         for j in dic:
        #             if abs(j - n) <= t:
        #                 return True
        #     dic.append(n)
        #     if len(dic) > k: del dic[0]
        # return False


        # Approach three
        length = len(nums)
        if k <= 0: return False
        if t == 0 and len(set(nums)) == length: return False
        for i in range(length - 1):
            for j in range(i+1, min(i+1+k , length)):
                if j - i <= k and abs(nums[j] - nums[i]) <= t:
                    return True
        return False
