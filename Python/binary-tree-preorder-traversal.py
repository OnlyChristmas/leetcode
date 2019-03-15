'''

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?



'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        # Approach one   迭代
        # if not root: return []
        # res = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.right: stack.append(node.right)
        #     if node.left: stack.append(node.left)
        # return res


        # Approach two   递归
        if not root: return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
