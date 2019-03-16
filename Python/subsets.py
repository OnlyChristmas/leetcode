'''

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]



'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # Approach one  将nums拆解，递归求解， 相当于每次将nums[0] 添加到其他所有的已有子集中。
        # if not nums: return [[]]
        # res = self.subsets(nums[1:])
        # return res + [[nums[0]] + s for s in res]


        # Approach two 迭代求解, 消耗栈空间少
        # res = [[]]
        # for i in nums:
        #     res += [ n + [i] for n in res]
        # return res


        # Approach three  华丽但不好想到的位运算处理法， 效率较低
        return [[nums[j] for j in range(len(nums)) if i>>j&1] for i in range(2**len(nums))]
