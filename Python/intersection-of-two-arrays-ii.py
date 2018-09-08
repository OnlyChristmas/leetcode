'''
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


'''



class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # 巧用python库中的Counter()来构造字典

        # 思路一： 只构造一个字典,nums2比较大时，节省一次构造的时间
        # from collections import Counter
        # result = []
        # dic1 = Counter(nums1)
        # for num in nums2:
        #     if num in dic1.keys():
        #         result.append(num)
        #         dic1[num] -= 1        # 通过字典操作实现检测个数的要求
        #         if dic1[num] == 0:
        #             dic1.pop(num)
        # return result


          # 思路二： 构造两个字典则不用频繁的字典操作
            # from collections import Counter
#         result = []
#         dic1,dic2 = Counter(nums1),Counter(nums2)

#         for num in dic2.keys():
#             if num in dic1.keys():
#                 repeat = min(dic1.get(num),dic2.get(num))
#                 for i in range(repeat):
#                     result.append(num)

#         return result



        # Approach #3   直接对字典操作，注意dic.elements()  返回的是一个迭代器。需要list()才能正常输出。
        # 这里用values()没办法输出重复的值。
        # return list((collections.Counter(nums1)&collections.Counter(nums2)).elements())




        # Approach #4  two pointers solution , don't make count.
        nums1.sort(), nums2.sort()  # Make sure it is sorted, doesn't count in time.
        res = []
        it1, it2 = 0, 0
        while it1 < len(nums1) and it2 < len(nums2):
            if nums1[it1] < nums2[it2]:
                it1 += 1
            elif nums1[it1] > nums2[it2]:
                it2 += 1
            else:
                res += nums1[it1],
                it1 += 1
                it2 += 1

        return res
