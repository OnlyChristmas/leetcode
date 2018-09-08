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

        # 思路一:  这种简单的遍历太笨拙了 TLE
        # for i in nums:
        #     n  = nums.count(i)
        #     if n ==1:
        #         return i

        # 思路二: 用python 内置的Counter 函数搞事情 例如：numss = [2,2,1,1,1,3]   得到  {1: 3, 2: 2, 3: 1} . 可以减少遍历的次数。
        # from collections import Counter
        # dict_nums = dict(Counter(nums))
        # nums_list = dict_nums.keys()
        # for i in nums_list:
        #     if dict_nums[i]==1:
        #         return i


        # 思路三: list排序
        # 容易想到的思路,对于所有数字排序,只需比较相邻两个是否相同,步长为二.缺点是排序耗费时间. 因为排序算法的时间复杂度上限为$O(nlog_n)$
        # 为了解决可能存在的越界问题,需要在排序后的数组中添加一个元素.
        # new = sorted(nums)
        # new.append(-0.1)
        # for i in range(0,len(new),2):
        #     if new[i] != new[i+1]:
        #         return new[i]


        # 思路四: 元素异或操作
        # 异或的自反性:对于某个数E ,用相同的运算因子做两次异或操作,最后的结果还是 E 本身. 以下是举例说明:
        # 由于A XOR A = 0 且 ((A^A) ^ (B^B) ^ (C^C) ^ (D^D) ^ E) = ((0^ 0 ^ 0 ^ 0 ^ E) =E
        # 直接把整个数组异或运算，最后的出来的就是只出现一次的数字了。
        # 这个性质常应用在加密，数据传输，校验等领域.
        result = 0
        for x in nums:
            result ^= x
        return result


        # 思路拓展,举一反三!
        # 找出只出现了一次的N个数字 https://www.lijinma.com/blog/2014/05/29/amazing-xor/
        # 在出现在N(2,4.....)次的一堆数字中找出只出现一次的那个数字  http://blademastercoder.github.io/2015/01/27/leetcode-findnum.html
