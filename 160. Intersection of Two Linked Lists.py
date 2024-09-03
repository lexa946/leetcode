# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_nodes = []
        b_nodes = []
        peresec = []
        while True:
            a_nodes.append(headA)
            if headA.next:
                headA = headA.next
            else:
                break

        while True:
            b_nodes.append(headB)
            if headB.next:
                headB = headB.next
            else:
                break

        while a_nodes and b_nodes:
            a_node = a_nodes.pop()
            b_node = b_nodes.pop()

            if a_node is b_node:
                peresec.append(a_node)

        if peresec:
            return peresec[-1]
        return None


sol = Solution()

node_one = ListNode(1)
node_two = ListNode(2)
node_tree = ListNode(3)
node_four = ListNode(4)

node_one.next = node_two
node_two.next = node_four

node_tree.next = node_four

print(sol.getIntersectionNode(node_one, node_tree))
