'''

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?



'''



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Approach two   O(nlogn)
        # dp 列表记录上升序列，可能有多个，我们记录最后一个数最小的上升序列。
        # 每次遍历dp，找出第一个比当前数字大的数字进行替换（二分查找）

        if not nums : return 0
        res = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                l , r = 0 , len(res)-1
                while l < r :
                    mid = l + (r - l) // 2
                    if nums[i] <= res[mid]:
                        r = mid
                    else:
                        l = mid + 1
                res[l] = nums[i]
        return len(res)







        # Approach one 人人为我
        # if not nums : return 0
        # res = [1 for _ in range(len(nums))]
        # for i in range(1,len(nums)):
        #     for j in range(0,i):
        #         if nums[j] < nums[i]:
        #             res[i] = max(res[i], res[j]+1)
        # return max(res)
