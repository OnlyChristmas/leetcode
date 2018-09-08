'''


A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.


'''



class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        # method one  思路清晰，但是效率偏低的方法。多次的数据转换，以及多余操作
        # res = []
        # for i in range(left , right+1):
        #     ss = str(i)
        #     if '0' not in ss:
        #         length = len(ss)
        #         for j in range(length):              # 11，222 这样自身元素重复的数是个坑, 容易出错，还影响代码效率
        #             if i % int(ss[j]) != 0:
        #                 break
        #             elif j == length - 1:
        #                 res.append(i)
        # return res


        # method two  在前面代码的基础上，利用数据类型的转换，减少一部分无用的除法操作
#         res = []
#         for i in range(left , right+1):
#             ss = set(str(i))
#             if '0' not in ss:
#                 ll = list(ss)
#                 for j in ll:
#                     if i % int(j) != 0:
#                         break
#                     elif j == ll[-1]:
#                         res.append(i)
#         return res




        # method three   这个方法不用大量的数据类型转换，但是仍有多余的除法
        res = []
        for i in range(left,right+1):
            k=i
            flag=1
            while k!=0:
                val = k % 10
                if val == 0 or i % val != 0:
                    flag=0
                    break
                k//=10
            if(flag==1):
                res.append(i)
        return res
