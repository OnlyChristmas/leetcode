'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
      # Approach one 分治的思想两两合并  O(NlogK) , O(1)
    # 想想二叉树，K个有序链表合并可以变成k-1次的“两个有序链表合并问题”
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:


        # def merge2lists(l1,l2):
        #     if not l1: return l2
        #     if not l2: return l1
        #     if l1.val <= l2.val:
        #         l1.next = merge2lists(l1.next , l2)
        #         return l1
        #     else:
        #         l2.next = merge2lists(l1 , l2.next)
        #         return l2



        def merge2lists(l1,l2):
            res = cur = ListNode(None)
            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next , l1 = l1 , l1.next
                else:
                    cur.next , l2 = l2 , l2.next
                cur = cur.next
            cur.next = l1 if l1 else l2
            return res.next

        while len(lists) > 1:
            lists.append(merge2lists(lists.pop(0),lists.pop(0)))
        return lists[0] if lists else None  # 注意输入为空
