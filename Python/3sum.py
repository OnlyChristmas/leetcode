'''


Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]



'''

class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':

        # Approach one
#         from collections import Counter
#         dic = Counter(nums)
#         res = []
#         new_nums = []
#         for k,v in dic.items():
#             if k == 0 and v > 2:
#                 res.append([0,0,0])
#                 new_nums.append(0)
#                 continue
#             if v >= 2:
#                 if  k != 0 and -2*k in dic.keys():
#                     res.append([k,k,-2*k])
#                 new_nums.append(k)
#             else:
#                 new_nums.append(k)

#         nums = sorted(new_nums)
#         length = len(nums) - 1
#         for i,n in enumerate(nums):
#             if n > 0 : break
#             l, r = i + 1, length
#             while l < r:
#                 result = nums[l] + nums[r] + n
#                 if result > 0:
#                     r -= 1
#                 elif result == 0:
#                     res.append([n, nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                 else:
#                     l += 1
#         return res






        # Approach two      排序后撞指针  O(n2)
        # nums = sorted(nums)
        # res = []
        # length = len(nums) - 1
        # for i,n in enumerate(nums[:-2]):
        #     if i > 0 and n == nums[i-1]: continue
        #     if n > 0 : break
        #     l, r = i + 1, length
        #     while l < r:
        #         result = nums[l] + nums[r] + n
        #         if result > 0:
        #             r -= 1
        #         elif result == 0:
        #             res.append([n, nums[l], nums[r]])
        #             l += 1
        #             while l < r and nums[l - 1] == nums[l]:
        #                 l += 1
        #             r -= 1
        #             while l < r and nums[r] == nums[r + 1]:
        #                 r -= 1
        #         else:
        #             l += 1
        # return res





        # Approach three    O(j*k)       faster than 98% ，但消耗的内存增加
        from collections import Counter
        dic = Counter(nums)
        pos = [x for x in dic if x > 0]
        neg = [x for x in dic if x < 0]
        res = []

        if dic.get(0, 0) > 2: res.append([0, 0, 0])   # 单独处理特殊的零
        for x in pos:                                 #  a、b、c 三数加和为零，若 a < 0 , b > 0 , 则  a < -c < b
            for y in neg:
                s = -(x + y)
                if s in dic:
                    if s == x and dic[x] > 1:
                        res.append([x, x, y])
                    elif s == y and dic[y] > 1:
                        res.append([x, y, y])
                    elif y < s < x:
                        res.append([x, y, s])
        return res
