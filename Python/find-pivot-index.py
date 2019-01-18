'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:
Input:
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:
Input:
nums = [1, 2, 3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].

'''


class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach one 低效的方法
        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        # return -1

        # Approach two
        # 注意，中心索引可以为第一个元素，左侧没有元素，其和默认为0
        # leftsum = 0
        # rightsum = sum(nums)
        # for i in range(len(nums)):
        #     if i >= 1: leftsum += nums[i-1]
        #     rightsum -= nums[i]
        #     if leftsum == rightsum: return i
        # return -1


        # Approach three  将中心索引分别算进左右的元素之和，减少判断语句的使用
        leftsum, rightsum = 0, sum(nums)
        for i in range(len(nums)):
            leftsum += nums[i]
            if leftsum == rightsum: return i
            rightsum -= nums[i]
        return -1
