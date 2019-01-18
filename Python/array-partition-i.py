'''
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

'''

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach one
        # ans = 0
        # new_nums = sorted(nums)
        # for i in range(0,len(new_nums),2):
        #     ans += new_nums[i]
        # return ans

        # Approach two  进一步简化代码，无需新数组
        # ans = 0
        # nums.sort()
        # for i in nums[::2]:
        #     ans += i
        # return ans

        # Approach three: 本问题相当于从小大到排序后，所有偶数之和
        # return sum([num for i, num in enumerate(sorted(nums)) if i % 2 == 0])

        # Approach Four: 利用数组切片，进一步简化操作
        # python 内置的sorted() 的平均/最坏时间复杂度均为 $O(nlog_2(n))$, 可以说是非常威武了。
        return sum(sorted(nums)[::2])
