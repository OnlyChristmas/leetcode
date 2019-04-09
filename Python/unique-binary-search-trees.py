'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''
class Solution:
    def numTrees(self, n: int) -> int:

        # Approach one  动规
        # 抛开题目的表面表述，确定最小子任务(人人为我)
        # 确定前三个边界值
        # 确当状态转换公式

        # 假设n个节点存在二叉排序树的个数是G(n)，令f(i)
        # 为以i为根的二叉搜索树的个数
        # 即有: G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)
        # n为根节点，当i为根节点时，其左子树节点个数为[1, 2, 3, ..., i - 1]，右子树节点个数为[i + 1, i + 2, ...
        # n]，所以当i为根节点时，其左子树节点个数为i - 1
        # 个，右子树节点为n - i，即f(i) = G(i - 1) * G(n - i),
        # 上面两式可得: G(n) = G(0) * G(n - 1) + G(1) * (n - 2) + ... + G(n - 1) * G(0)


        num = [i if i < 3 else 0 for i in range(n+1) ]
        num[0] = 1
        for i in range(3,n+1):
            for j in range(i):
                num[i] += num[j]*num[i-j-1]
        return num[n]
