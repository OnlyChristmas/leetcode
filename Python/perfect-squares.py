'''

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


'''






class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Approach one 【失败】  贪心算法不适用，大的数不一定会入选
        # res = [i ** 2  for i in range(1,n//2+1)  if i ** 2 <= n]
        # print(res)
        # tmp_ans = count  = 0
        # ans = []
        # while len(res) > 1:
        #     point = -1
        #     while count != n:
        #         if res[point] <= n - count:
        #             count += res[point]
        #             tmp_ans += 1
        #         else:
        #             point -= 1
        #     ans.append(tmp_ans)
        #     tmp_ans = count = 0
        #     del res[-1]
        # return min(ans) if ans else n


        # Approach two 利用队列和BFS，最先搜索到的结果一定是最短的。 队列中存储（位置,步数） ，效率比较低。
        # q = [[n, 0]]
        # visited = [False for _ in range(n + 1)]
        # visited[n] = True
        # while any(q):
        #     num, step = q.pop(0)   # 出栈，被pop掉的元素将同时返回给两个变量
        #     i = 1
        #     tnum = num - i ** 2
        #     while tnum >= 0:            # 前进一步
        #         if tnum == 0: return step + 1   # 最先到达0的一定是步数最少的
        #         if not visited[tnum]:
        #             q.append((tnum, step + 1))
        #             visited[tnum] = True     # 只添加没有遍历过的节点，减少计算量
        #         i += 1
        #         tnum = num - i ** 2



        # Approach three
        # Lagrange 四平方定理： 任何一个正整数都可以表示成不超过四个整数的平方之和。
        # 也就是说，这个题目返回的答案只有1、2、3、4这四种可能。 我们可以将输入的数字除以4来大大减少计算量，并不改变答案
        # 一个数除以8的余数，如果余数为7， 则其必然由四个完全平方数组成
        # 然后检测是否可以将简化后的数拆分为两个完全平方数，否则一定由三个完全平方数组成。
        import math
        while n % 4 == 0: n = n // 4
        if n % 8 == 7: return 4
        if int(math.sqrt(n)) ** 2 == n: return 1
        i = 1
        while i*i <= n:
            j = math.sqrt(n - i*i)
            if int(j) == j: return 2
            i += 1
        return 3
