'''

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
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

    def inorderTraversal(self, root: TreeNode) -> List[int]:

        # Approach one  递归
        # if not root : return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


        # Approach two
        # if not root : return []
        # self.inorderTraversal(root.left)
        # self.answer.append(root.val)
        # self.inorderTraversal(root.right)
        # return self.answer


        # Approach four 不使用类变量的情况
        # def helper(root, res):
        #     if root:
        #         helper(root.left, res)
        #         res.append(root.val)
        #         helper(root.right, res)
        # res = []
        # helper(root, res)
        # return res


        # Approach three  迭代效率稍低
        if not root : return []
        stack, res = [] , []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack : return res
            node = stack.pop()
            res.append(node.val)
            root = node.right













            
