'''
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

'''


# 注意python中，引用和副本的区别

# Approach one
# import random
# class Solution:

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nums = nums[:]   # 没有[:]是，使用的是numsp[:]的引用； 而加上后，使用的是[:]的副本，副本不会改变
#         self.output = nums


#     def reset(self):
#         """
#         Resets the array to its original configuration and return it.
#         :rtype: List[int]
#         """
#         return self.nums


#     def shuffle(self):
#         """
#         Returns a random shuffling of the array.
#         :rtype: List[int]
#         """
#         length = len(self.output)
#         for i in range(length):
#             j = random.randint(0,length-1)
#             self.output[i], self.output[j] = self.output[j], self.output[i]
#         return self.output


# Approach two
import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums



    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        self.output = self.nums.copy()    # 需要打乱顺序的时候，拷贝新的副本，不改变原本的数据
        length = len(self.output)
        for i in range(length):
            j = random.randint(0,length-1)
            self.output[i], self.output[j] = self.output[j], self.output[i]
        return self.output





# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
