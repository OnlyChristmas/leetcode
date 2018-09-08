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
        # method one 运用set()特性
        # for i in set(nums):
        #     if nums.count(i) * 2 > len(nums):
        #         return i


        # method two 排序中位数
        return  sorted(nums)[ len(nums) // 2 ]
