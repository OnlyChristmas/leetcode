'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



'''



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:



        # Approach two  DP
        res = nums[0]
        num = 0
        for i in range(len(nums)):
            num += nums[i]
            if num > res:
                res = num
            if num < 0:
                num = 0
        return res
