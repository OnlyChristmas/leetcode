'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''




class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach one
        # from collections import Counter
        # import math
        # length = math.ceil(len(nums) / 2)
        # for k,v in Counter(nums).items():
        #     if v >= length:
        #         return k


        # Approach two      巧用max(arg,key)免去反转字典
        # from collections import Counter
        # dic = Counter(nums)
        # return max(dic , key = dic.get)



        # Approach three     利用本文中众数的特殊定义，排序后中间的数字必为答案
        # return sorted(nums)[int(len(nums)/2)]



        # Approach four    定义结合set()特性
        length = len(nums)
        for i in set(nums):
            if nums.count(i) * 2 > length:
                return i
