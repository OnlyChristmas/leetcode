'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

'''





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 尾递归的程序递归是最后一步，进入递归之后相当于进入了一个新的函数，与当前的函数环境不再交互，不用担心栈溢出，比普通递归消耗的资源较少。
        # 所以此函数不是尾递归

        if not root : return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
