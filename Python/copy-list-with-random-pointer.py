'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.



Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.



'''



"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

#         Approach one  深拷贝不是引用，需要新构造一个链表
#         构造新链表
#         赋值 random 指针

#         pre = pre2 = Node(0, None, None)
#         orig =  orig1 = head
#         dic = {}

#         if not head:  return None
#         while orig:
#             new_node = Node(orig.val , None, None)
#             dic[orig] = new_node
#             pre.next  = new_node
#             pre = pre.next
#             orig = orig.next

#         res = pre2.next
#         while orig1:
#             if orig1 and orig1.random:
#                 res.random = dic[orig1.random]
#             orig1 = orig1.next
#             res = res.next
#         return pre2.next



        # Approach two   O(n)    O(1)

        if not head: return None
        pre = None
        current = head

        while current:
            current.random = Node(current.val, None, current.random)
            if pre:
                pre.random.next = current.random
            pre = current
            current = current.next

        current = head.random
        while current:
            if current.random:
                current.random = current.random.random
            current = current.next
        return head.random
