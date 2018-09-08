'''


Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

'''


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # method two   遍历速度太慢
        # return  [i for i in range(len(nums)+1) if i not in nums][0]

        # method three   集合操作
        # return  list(set(list(range(len(nums)+1))) - set(nums))[0]


        # method one 从数学角度考虑
        return int(len(nums)*(len(nums)+1)/2 - sum(nums))


        
