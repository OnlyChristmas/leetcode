'''

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        # Approach one
        if not root: return []
        res,q = [], [root]
        while q:
            cur = []
            len_q = len(q)
            for _ in range(len_q):
                node = q.pop(0)
                cur.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(cur)
        return res
