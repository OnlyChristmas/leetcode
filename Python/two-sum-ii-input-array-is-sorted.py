'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''



class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Approach one
#         for i,n in enumerate(numbers):
#             ind = target - n
#             if ind in numbers:
#                 index2 = numbers.index(ind)
#                 if index2 == i: return [i+1,i+2]
#                 return [i + 1, index2 +1]

        # Approach two
        # dic = {}
        # for i,n in enumerate(numbers):
        #     s = target - n
        #     if s not in dic:    # 巧妙避免两个相同元素的情况。
        #         dic[n] = i
        #     else:
        #         return [dic[s] +1 , i+1]

        # Approach three 双指针
        if not numbers: return None
        l , r = 0 , len(numbers) -1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
