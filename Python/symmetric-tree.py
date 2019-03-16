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
        if not root : return True
        qlist=[root.left, root.right]
        while len(qlist)!=0:
            t1=qlist.pop()
            t2=qlist.pop()
            if not t1 and not t2: continue
            if not t1 or not t2: return False
            if t1.val != t2.val : return False
            qlist.append(t1.left)
            qlist.append(t2.right)
            qlist.append(t1.right)
            qlist.append(t2.left)
        return True
