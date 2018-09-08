'''


Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101

Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.

Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.

Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.

'''


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # method one  强行一行, 代码效率不够高.    40ms  93%
        # 重复了bin() 操作 , 不符合要求的数字没有提前终止,而是进行了所有比较
        # return   all(bin(n)[2:][i] != bin(n)[2:][i+1]  for  i in  range(len(bin(n)[2:])-1))


        # Approach #2   位运算
        n, curr = divmod(n, 2)
        while n > 0:
            if curr == n % 2:
                return False
            n, curr = divmod(n, 2)
        return True
