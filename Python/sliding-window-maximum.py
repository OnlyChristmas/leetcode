'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?


'''



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # Approach one   O(n) ~ O(kn),  O(1)
#         length = len(nums)
#         if k > length or k <= 0: return []
#         l , r = 0 , k-1
#         res = [max(nums[l:r+1])]
#         r += 1
#         while r < length:
#             if nums[r] >= res[-1]:
#                 res.append(nums[r])
#                 l += 1
#                 r += 1
#             elif nums[l] == res[-1]:
#                 l += 1
#                 res.append(max(nums[l:r+1]))
#                 r += 1
#             else:
#                 res.append(res[-1])
#                 l += 1
#                 r += 1
#         return res



        # Approch two   一个双向队列  O(n) , O(1)
        res , tmp = [] , []
        if k > len(nums) or k <= 0 : return []
        for i in range(len(nums)):
            if len(tmp) > 0 and tmp[0] <= i - k:
                tmp.pop(0)
            while len(tmp) > 0 and nums[tmp[-1]] <= nums[i]:
                tmp.pop()
            tmp.append(i)
            if i >= k-1:
                res.append(nums[tmp[0]])
        return res
