'''

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.


'''



class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 将原问题简化为寻找有多少个2*5的个数，只有这样才能出现零。因为2必然比5多，只关注5就好。
        res = 0
        while n >= 5:
            n = n // 5
            res += n
        return res
