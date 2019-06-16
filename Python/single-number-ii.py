'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99




'''

# 类似题目 leetcode 136 、260


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 所有数字相加后每个二进制位除以三，会将所有出现三次的数字都消除掉。 需要一个固定的32为的辅助数组空间O(1)
        if not nums : return 0
        length = len(nums)
        res,bitSum = 0, [0 for _ in range(32)]
        for i in nums:
            bitMask = 1
            for j in range(31,-1,-1):
                if i & bitMask != 0:
                    bitSum[j] += 1
                bitMask <<= 1

        for i in range(32):
            res = res << 1
            res += bitSum[i] % 3
        return res




        # 二进制模拟三进制 ，详见  https://cloud.tencent.com/developer/article/1341825
        # if not nums : return 0
        # a, b = 0, 0
        # for i in nums:
        #     a = (a ^ i) & ~b
        #     b = (b ^ i) & ~a
        # return a
