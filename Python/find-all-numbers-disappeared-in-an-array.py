'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''



class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

#       method one  集合操作
        # return list(set(range(1, len(nums)+1)) - set(nums))


        # method two   遍历比集合减法要更加高效？
        s = set(nums)  # 不能直接写成一行，效率太低
        return [i for i in range(1, len(nums)+1) if i not in s]
