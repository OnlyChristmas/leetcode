'''

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # Approach one 转化为数据回文, 引入了额外的存储空间, O(n),O(n)
#         res = []
#         while head:
#             res.append(head.val)
#             head = head.next

#         for i in range(len(res)//2):
#             if res[i] != res[-(i+1)]:
#                 return False
#         return True

        # # Approach 1.5    用列表的性质比较
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        # return res == res[::-1]



        # Approach two 快慢指针，压栈比较，O(n),O(n/2)
#         res = []
#         fast = slow = head
#         while fast and fast.next:
#             fast = fast.next.next
#             res.insert(0,slow.val)
#             slow = slow.next

#         if fast:   # 处理链表长度为奇数的情况
#             slow = slow.next

#         for i in res:
#             if i != slow.val:
#                 return False
#             slow = slow.next
#         return True



        # Approach three  快慢指针，反转后半段，比较O(n),O(1)
#         fast,slow = head,head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next

#         if fast:   # 处理链表长度为奇数的情况
#             slow = slow.next
#         new_slow = self.reverseList(slow)

#         while new_slow and new_slow.val == head.val:
#             new_slow, head = new_slow.next, head.next
#         return not new_slow

#     def reverseList(self,head):
#         res = None
#         while head:
#             curr = head
#             head = head.next
#             curr.next = res
#             res = curr
#         return res

        # Approach 3.5 快慢指针找中点的同时，反转前半段链表
        fast,slow,res = head,head,None
        while fast and fast.next:
            fast = fast.next.next
            res, res.next ,slow = slow, res, slow.next
        if fast:   # 处理链表长度为奇数的情况
            slow = slow.next
        while slow and slow.val == res.val:
            slow, res = slow.next, res.next
        return not slow


        
