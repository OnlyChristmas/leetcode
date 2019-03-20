'''


You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Approach one   将链表转换为数字相加后再转换为链表
        def trans(listnode):
            res = []
            while listnode:
                res.append(str(listnode.val))
                listnode = listnode.next
            return int(''.join(res[::-1]))

        Sum_ans = [ListNode(i) for i in str(trans(l1) + trans(l2))[::-1]]
        res = Sum_ans[0]
        tmp = res
        for i in range(1,len(Sum_ans)):
            tmp.next = Sum_ans[i]
            tmp = tmp.next
        return res
