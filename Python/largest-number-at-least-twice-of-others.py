'''

In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:
Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


Example 2:
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.


Note:
nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].

'''


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach one   重复遍历,效率偏低
        # max_num = max_id = 0
        # for i,num in enumerate(nums):
        #     if num > max_num:
        #         max_num = num
        #         max_id = i
        # nums.remove(max_num)
        # if nums != [] and max_num < max(nums)*2: return -1    # 防止列表只有一个元素
        # return max_id


        # Approach two  简化代码，但仍重复遍历
        # if len(nums) == 1 : return 0
        # max_num = max(nums)
        # max_id = nums.index(max_num)
        # nums.remove(max_num)
        # if max_num >= max(nums) * 2: return max_id
        # return -1


        # Approach three
        # max_num = max(nums)
        # for num in nums:
        #     if 2*num > max_num and num != max_num:
        #         return -1
        # return nums.index(max_num)

        # Approach four
        # max_num = max(nums)
        # max_loc = nums.index(max_num)
        # nums[max_loc] = 0               # 通过置零，而不是删除，解决只有一个元素的情况。
        # return max_loc if max_num >= max(nums) *2 else -1

        # Approach five  只需一次排序，效率最高
        if len(nums) > 1:
            max_nums = sorted(nums)
            if max_nums[-1] >= max_nums[-2] * 2:
                return nums.index(max_nums[-1])
            return -1
        return 0    # 只有一个元素时需要特殊处理
