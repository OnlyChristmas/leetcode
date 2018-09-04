'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''



class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # method one: 用了if 条件语句，不够简洁。
        # res = []
        # for i in range(numRows+1):
        #     if i == 1:
        #         row = [1]
        #         res.append(row)
        #     if i >= 2:
        #         tmp = []
        #         for j in range(len(row)-1):
        #             tmp.append(row[j] + row[j+1])
        #         row = [1] + tmp + [1]
        #         res.append(row)
        # return res


        # method two
        res = [[1]]    # 初始化[1],简化了分类讨论的步骤
        for i in range(1,numRows):
            res.append(list(map(lambda x, y : x + y, res[-1]+[0], [0]+res[-1])))
            # list = map(func, iter)  强制类型转换才能生成list类型的结果
            # res[-1] 前一次迭代得到的列表，拼接[0]之后，反向叠加。就可以得到新的迭代序列，非常漂亮的数学结构
        return res[:numRows]     # 巧妙地避免了n=0 的特殊情况
