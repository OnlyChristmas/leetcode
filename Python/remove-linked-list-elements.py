'''

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        # Approach one
        last = ListNode(0)
        last.next = first = head
        while first:
            if first.val == val:
                last.next = last.next.next
                if first == head: head = head.next    # 删除头结点特殊处理
            else:
                last = first
            first = first.next
        return head
