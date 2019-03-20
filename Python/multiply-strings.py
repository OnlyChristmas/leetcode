'''


Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # Approach one  不符合题目要求
        # return  str(int(num1) * int(num2))



        # Approach two  采取列竖式乘法的方法， m位数乘以n位数，结果最多为m+n位数。
        if num1 == "0" or num2 == "0": return "0"
        n1 = len(num1)
        n2 = len(num2)
        result = [0 for i in range(n1 + n2)]

        def _sum(value, index):                # 存储每一位相乘的结果
            tmpIndex = n1 + n2 - 1 - index
            tmp = result[tmpIndex] + value
            if tmp > 9:
                result[tmpIndex] = tmp % 10
                _sum(tmp // 10, index + 1)
            else:
                result[tmpIndex] = tmp

        for i in range(n1):
            a = int(num1[n1 - 1 - i])
            for j in range(n2):
                b = int(num2[n2 - 1 - j])
                c = a * b
                _sum(c, i + j)  # 从0开始

        if result[0] == 0:
            return "".join([str(k) for k in result[1:]])    # 最多只有一位零
        else:
            return "".join([str(k) for k in result])
