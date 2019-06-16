'''

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?



'''


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 类比于 136 题，将两个只出现一次的数字分类分入两个组别，即可转化为我们的已知问题。
        # 关键在于如何区分两个只出现过一次的数字

        # 当一次遍历异或后得到的是两个只出现过一次的数字的异或值，因为他们不同，最终的key值中至少有一个1，且最高位一定是1。
        # 我们就可以根据最后key值的最高位是否是 1 ，将所有数字分成两组（两个单一的数字必然在不同组，其他出现两次的数字一定同组）。
        # 为了方便检测每个数字的特定位是否为1 ， 可以将其右移到最低位，和1 进行与操作即可检测。

        if not nums : return None
        key = 0
        for i in nums:
            key ^= i
        num = len(bin(key)) - 3

        a,b = 0,0
        for i in nums:
            if (i >> num) & 1:
                a ^= i
            else:
                b ^= i
        return [a,b]
