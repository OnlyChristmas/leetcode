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
#         构造新链表赋值 random 指针

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

#         if not head: return None
#         pre = None
#         current = head

#         while current:
#             current.random = Node(current.val, None, current.random)
#             if pre:
#                 pre.random.next = current.random
#             pre = current
#             current = current.next

#         current = head.random
#         while current:
#             if current.random:
#                 current.random = current.random.random
#             current = current.next
#         return head.random



        # Approach three   O(n)  O(1)
        # 在原链表的每个节点后面插入一个相同的节点
        # 根据现在新节点和旧结点相交叉的状态复制随机指针
        # 最后将两个链表一替一步的交叉前进，分离开来

        if not head: return None

        # 将新结点复制出来，插进原链表
        tmp = head
        while tmp:
            node = Node(tmp.val,tmp.next,None)
            tmp.next, tmp = node , node.next

        # 复制随机指针
        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random  = tmp.random.next
            tmp =  tmp.next.next

        # 拆分两个链表(注意边界条件，插入后的链表一个为偶数，原链表结点为空的时候就可以停止)
        res = new_head = Node(0, None, None)
        origin = head
        while origin:
            new_head.next =  origin.next
            new_head = new_head.next
            origin.next = new_head.next
            origin = origin.next
        return res.next
