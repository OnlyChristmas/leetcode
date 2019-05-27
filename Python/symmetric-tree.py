'''

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

      # Approach one  递归法
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root : return True
#         return self.judge_tree(root.left , root.right)


#     def judge_tree(self, left , right):
#         if not left and not right : return True
#         if left and right :
#             if left.val == right.val :
#                 return self.judge_tree(left.left, right.right) and self.judge_tree(left.right , right.left)
#         return False


    #  Approach two 迭代
    def isSymmetric(self, root: TreeNode) -> bool:
        # 循环解法，递归调用函数会有额外的开销。
        if not root : return True
        stack = [root.left,root.right]
        while stack:
            node1,node2 = stack.pop(), stack.pop()
            if not node1 and not node2 : continue
            if not node1 or not  node2 : return False
            if node2.val != node1.val : return False
            stack += [node1.left, node2.right,node1.right,node2.left]
        return True
