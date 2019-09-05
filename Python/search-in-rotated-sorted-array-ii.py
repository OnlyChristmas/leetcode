''''

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?


'''


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) <= 0 : return False
        l , r = 0 , len(nums) - 1
        while l <= r :
            mid = l + (r - l) // 2
            if target == nums[l] or target == nums[r] or target == nums[mid] : return True
            if nums[l] == nums[mid]: l += 1
            elif nums[l] <  nums[mid]:
                if nums[l] < target < nums[mid]: r = mid -1
                else: l = mid + 1
            else:
                if nums[mid]  < target < nums[r]: l = mid + 1
                else: r = mid - 1
        return False
