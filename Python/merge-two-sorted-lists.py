'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Approach one 递归的方法
#         if l1 == None:
#             return l2
#         elif l2 == None:
#             return l1
#         if l2.val >= l1.val:
#             l1.next =  self.mergeTwoLists(l1.next, l2)
#             return l1
#         else:
#             l2.next =  self.mergeTwoLists(l1, l2.next)
#             return l2




        # Approach two  # 循环的解法需要两个新头结点，并注意拼接尾链
        head =  curr = ListNode(0)
        while l1 and l2:
            if l1.val >= l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return head.next
