'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
'''



class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """




        # 元素异或操作
        # 异或的自反性:对于某个数E ,用相同的运算因子做两次异或操作,最后的结果还是 E 本身. 以下是举例说明:
        # 由于A XOR A = 0 且 ((A^A) ^ (B^B) ^ (C^C) ^ (D^D) ^ E) = ((0^ 0 ^ 0 ^ 0 ^ E) =E
        # 直接把整个数组异或运算，最后的出来的就是只出现一次的数字了。
        # 这个性质常应用在加密，数据传输，校验等领域.
        if not nums: return None
        key = nums[0]
        for i in nums[1:]:
            key = key ^ i
        return key
