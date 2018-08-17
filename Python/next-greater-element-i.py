'''
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

'''





class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # method once 双重循环效率较低
        # Time:  O(nlogn)
        # Space: O(n)
        #
        # res = []
        # length = len(nums2)
        # for i in nums1:
        #     if (nums2.index(i)+1) < length:
        #         for j in range(nums2.index(i)+1,length):
        #             if nums2[j] > i:
        #                 res.append(nums2[j])
        #                 break
        #             elif j == length-1:
        #                 res.append(-1)
        #     else:
        #         res.append(-1)
        # return res

        # method twice  利用字典提升效率
        # Time:  O(nlogn)
        # Space: O(n)
        #
        # if nums2 != []:
        #     dic  = {nums2[-1]:-1}
        #     for index in range(len(nums2)) :
        #         for j in range(index+1,len(nums2)):
        #             if nums2[index] < nums2[j]:
        #                 dic[ nums2[index]] = nums2[j]
        #                 break
        #             elif j == len(nums2)-1:
        #                 dic[nums2[index]] = -1
        #     return [dic.get(i,-1) for i in nums1]
        # return []



        # method third   利用栈结构提升效率
        # Time:  O(n)
        # Space: O(n)
        #
        dic , stack = {} ,[]
        for number in nums2:
            while stack and stack[-1] < number:
                dic[stack.pop()] = number
            stack.append(number)
        return [dic.get(i , -1) for i in nums1]




