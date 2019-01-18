'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''





class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Approach one 最简单的思路，在数组后面先补出来k个数字，然后数组向后移动，再把后面的数字搬到前面，最后去掉后面多余的数字。效率低下的算法
#         length = len(nums)
#         for i in range(k):
#             nums.append(0)

#         for i in range(len(nums)-k-1,-1,-1):
#             nums[i+k] = nums[i]

#         for j in range(len(nums)-1,len(nums)-k-1,-1):
#             nums[k-1] = nums[j]
#             k -= 1

#         for j in range(len(nums)-length):
#             del nums[-1]

    # Approach Two
        # while k:
        #     k -= 1
        #     nums.insert(0, nums.pop(-1))

    # Approach Three：运用数组的切片操作，简洁。并且是一个原地算法。
        i = k % len(nums)
        nums[:] = nums[-i:]+nums[:-i]
