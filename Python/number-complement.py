'''

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


'''


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # method one   数据类型的转换较多，优雅，但低效
        # return   int(''.join(list(map(lambda x:str(int(x)^1),bin(num)[2:]))) ,2)



        # method two
        # i = 1
        # while i <= num:
        #     i = i << 1    # 比较少用的位移运算符(i自动转换成二进制数)
        # return (i - 1) ^ num     # 通过上述循环，确定了num的二进制数的位数。 通过减一操作，确定这个长度的全一序列进行异或操作。
        #                          # 二进制数和十进制数可以直接异或



        # method three    将方法二的代码浓缩到一行（关键在于确定num的二进制数的长度）
        return  (2**(len(bin(num))-2)-1) ^ num   
