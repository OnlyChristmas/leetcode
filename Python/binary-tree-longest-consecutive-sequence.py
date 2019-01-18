'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


'''


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # Approach one
        # left = 0
        # ans = 10000000
        # for i in range(len(nums)):
        #     while sum(nums[left:i+1]) >= s:
        #         ans = min(ans, i - left + 1)
        #         left += 1
        # return ans if ans != 10000000 else 0   # 处理没有答案的特殊情况


        # Approach two
        left,tmp,ans = 0,0,10000000
        for i in range(len(nums)):
            tmp += nums[i]
            while tmp >= s:                # 减少重复的求和操作
                if ans > i - left +1:
                    ans = i - left +1      # min()、max() 函数耗费时间过多
                tmp -= nums[left]
                left += 1
        return ans if ans != 10000000 else 0   # 处理没有答案的特殊情况




            
