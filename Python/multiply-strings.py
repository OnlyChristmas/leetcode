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

        # 考察大数相乘(两个数相乘结果只可能为n1+n2或者n1+n2-1)
        if num1 == "0" or num2 == "0": return "0"
        n1 = len(num1)
        n2 = len(num2)
        num1 = list(map(int, list(num1)))
        num2 = list(map(int, list(num2)))
        result = [0 for i in range(n1 + n2)]

        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                result[i+j+1] += num1[i] * num2[j]

        for i in range(n1+n2-1,0,-1):
            result[i-1] += result[i] // 10
            result[i] = result[i] % 10


        if result[0] == 0:
            return "".join([str(k) for k in result[1:]])    # 前面最多只有一位零
        else:
            return "".join([str(k) for k in result])
