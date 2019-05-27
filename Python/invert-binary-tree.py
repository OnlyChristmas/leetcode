'''

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.


'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        # Approach one  递归求解
        # if not root : return None
        # root.right , root.left = self.invertTree(root.left), self.invertTree(root.right)
        # return root


        # Approach two  栈+循环
        # if not root : return None
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     node.left , node.right = node.right , node.left
        #     if node.left : stack.append(node.left)
        #     if node.right: stack.append(node.right)
        # return root

        # Approach three  队列也是一样
        if not root : return None
        q = [root]
        while q:
            node = q.pop()
            node.left , node.right = node.right , node.left
            if node.left : q.append(node.left)
            if node.right: q.append(node.right)
        return root
