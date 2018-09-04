'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

'''



class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 思路一： 整数和字符的转换
        # return  [int(i) for i in str(int(''.join([str(i) for i in digits]))+1)]


        # 思路二： 减少转换次数，提升效率.(用存储空间换取使时间效率)
        num = 0
        for i in range(len(digits)):
            num = num*10 + digits[i]
        return [int(i) for i in str(num+1)]
