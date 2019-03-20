'''

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.




Follow up:
Can you solve it without using extra space?


'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Approach one
        # 1、快慢指针判断链表是否有环
        # 2、如果有环，根据相交点找出入环节点
        #    设慢指针走的路程为L，则快指针走的路程为2L；设头结点到入环点的长度为K，入环点到相交点的长度为M，环的长度为Q, 快指针一共绕环n圈。
        #    则  L = K + M
        #       2L = K + M + Q*n
        #    根据上面两式，可以得到  K + M = n*Q
        #    进而可以得到  K = (n - 1)*Q + (L - M)
        #    也就是说，当快慢指针相遇后，慢指针回到头结点，快指针同时在相交点出发（但也以步长1），它们再次相遇时会刚好走到入环点。代码如下。


        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast and fast == slow:      # 不可以写成  slow.val == fast.val
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
