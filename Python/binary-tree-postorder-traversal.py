'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?



'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
            self.answer = []
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # Approach one 递归
#         if not root : return []
#         return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


        # Approach two 转化先序迭代, 注意左右子树的顺序
        # if not root : return []
        # stack ,res = [root] , []
        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.left: stack.append(node.left)
        #     if node.right: stack.append(node.right)
        # return res[::-1]


        # Approach three
        if not root:  return self.answer

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.answer.append(root.val)

        return self.answer
