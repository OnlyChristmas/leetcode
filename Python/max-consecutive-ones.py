
'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

'''


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach #1
        # Time:  O(n)
        # Space: O(1)
        #
        # res, MM = 0, 0
        # for i in nums:
        #     if i == 1:
        #         res += 1
        #         if MM < res:
        #             MM = res
        #     else:
        #         res = 0
        # return MM

        # Approach #2
        # Time:  O(n)
        # Space: O(1)
        #
        # ans = 0
        # c = 0
        # for i in nums:
        #     c = i * c + i   # 简化了上述的判断语句，遇0置0，遇1叠加。
        #     if c > ans:
        #         ans = c
        # return ans

        # Approach three 
        ans = count = 0
        for i in nums:
            if i:
                count += 1
            else:
                ans = max(ans ,count)
                count = 0
        return max(ans,count)    # 解决最后一组“1”的统计
