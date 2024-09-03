# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        while head.next:
            nodes.append(head)
            head = head.next
        nodes.append(head)

        prev_node = None
        for node in nodes:
            node.next = prev_node
            prev_node = node

        return node


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        prev_node = None

        while head.next:
            new_node = ListNode(head.val)
            if prev_node:
                new_node.next = prev_node
            prev_node = new_node
            head = head.next
        head.next = prev_node


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        prev_node = None

        while head:
            curr = head
            head = head.next
            curr.next = prev_node
            prev_node = curr

        return prev_node




sol = Solution()


node_one = ListNode(1)
node_two = ListNode(2)
node_tree = ListNode(3)
node_four = ListNode(4)
node_five = ListNode(5)

node_one.next = node_two
node_two.next = node_tree
node_tree.next = node_four
node_four.next = node_five


sol.reverseList(node_one)
print()
