


'''

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"

'''









class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Approach #1   复杂的逻辑……
        # ans = '1'
        # num = 1
        # while n != num:
        #     loc = []
        #     length = len(ans) - 1
        #     ori_ans = ans
        #     for i in range(length):
        #         if ori_ans[i] != ori_ans[i+1]:
        #             if loc != []:
        #                 ans += str(len(ori_ans[loc[-1]:i+1])) + str(ori_ans[i])
        #             else:
        #                 ans = str( len(ori_ans[:i+1])) + str(ori_ans[0])
        #             loc.append(i+1)
        #             if length == i+1:
        #                 ans += str( len(ori_ans[loc[-1]:i+2])) + str(ori_ans[i+1])
        #         elif loc != [] and length == i+1:
        #             ans += str( len(ori_ans[loc[-1]:i+2])) + str(ori_ans[i+1])
        #         elif i+1 == length:
        #             ans = str(length + 1) + ans[0]
        #     if length == 0: ans = '1' + ans
        #     num += 1
        # return ans





        #Approach #2
        # import itertools
        # ans='1'
        # for i in range(1,n):
        #     v=''
        #     for digit,group in itertools.groupby(ans):         #itertools.groupby(ans)  函数默认将一个字符串按照连续相同的部分分割。返回的迭代器有两个成分，一个是分割的元素，另一部分是分割的字符串
        #         v+=str(len(list(group)))+digit
        #     ans=v
        # return ans



        # Approach #3   相比于Approach 1 新建一个变量let表示字符，就可以避免复杂易错的数组操作; ans只有在每次循环结束时才变化，需要复制一份。
        ans = '1'
        for _ in range(n-1):
            let, temp, count = ans[0], '', 0
            for l in ans:
                if let == l:
                    count += 1
                else:
                    temp += str(count)+let
                    let = l
                    count = 1
            temp += str(count)+let            # 处理最后一个字符串片段
            ans = temp
        return ans
